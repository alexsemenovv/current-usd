from unittest.mock import patch

from django.core.cache import cache
from django.http import HttpResponseBadRequest
from django.test import TestCase, Client
from django.urls import reverse

from api.models import ExchangeRate


class CurrentUsdTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("api:current_usd")
        cache.clear()

    @patch("requests.get")
    def test_successful_api_call_creates_rate_and_returns_json(self, mock_get):
        """Тест на успешный статус код и нахождение полей: rate и last_10_rate - в ответе"""
        mock_response = {
            "Valute": {
                "USD": {"Value": 92.34}
            }
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn("rate", data)
        self.assertIn("last_10_rate", data)
        self.assertEqual(float(data["rate"]), 92.34)

    @patch("requests.get")
    def test_cache_is_used_on_second_request(self, mock_get):
        """Тест на проверку работы кёша при повторном запросе"""
        mock_response = {
            "Valute": {
                "USD": {"Value": 91.11}
            }
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        response1 = self.client.get(self.url)
        self.assertEqual(mock_get.call_count, 1)

        response2 = self.client.get(self.url)
        self.assertEqual(mock_get.call_count, 1)

        data1 = response1.json()
        data2 = response2.json()
        self.assertEqual(data1, data2)

    @patch("requests.get")
    def test_api_error_raises_exception(self, mock_get):
        """Тест на проверку плохого ответа от сервера"""
        mock_get.return_value.status_code = 500
        with self.assertRaises(HttpResponseBadRequest):
            self.client.get(self.url)

    @patch("requests.get")
    def test_last_10_rates_limit(self, mock_get):
        """Тест на проверку получения 10 последних записей"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "Valute": {"USD": {"Value": 90.0}}
        }

        for _ in range(12):
            cache.clear()
            self.client.get(self.url)

        self.assertEqual(ExchangeRate.objects.count(), 12)

        response = self.client.get(self.url)
        data = response.json()
        self.assertEqual(len(data["last_10_rate"]), 10)
