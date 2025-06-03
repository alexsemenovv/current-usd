import requests
from django.core.cache import cache
from django.core.exceptions import BadRequest
from django.http import HttpRequest, HttpResponse, JsonResponse

from .models import ExchangeRate

BASE_URL = "https://www.cbr-xml-daily.ru/daily_json.js"


def get_current_usd(request: HttpRequest) -> HttpResponse:
    """Получение текущего курса USD"""
    cache_key = "current_usd"
    data = cache.get(cache_key)
    if data is None:
        response = requests.get(BASE_URL)
        if response.status_code != 200:
            raise BadRequest(f"Сервер временно недоступен. Код ошибки: {response.status_code}")
        rate = response.json().get("Valute", {}).get("USD", {}).get("Value")
        obj = ExchangeRate.objects.create(rate=rate)
        obj.save()

        last_rate = ExchangeRate.objects.filter(pk=obj.pk).first()
        last_10_rate = ExchangeRate.objects.order_by("-pk").all()[:10]

        last_10_rate_dict = {
            i_rate.pk: [i_rate.rate, i_rate.timestamp]
            for i_rate in last_10_rate
        }

        data = {
            "date": last_rate.timestamp,
            "rate": last_rate.rate,
            "last_10_rate": last_10_rate_dict,
        }
        cache.set(cache_key, data, 10)
    return JsonResponse(data, safe=False)
