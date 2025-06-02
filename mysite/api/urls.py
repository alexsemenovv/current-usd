from django.urls import path

from api.views import get_current_usd

app_name = "api"

urlpatterns = [
    path('get-current-usd/', get_current_usd, name="current_usd"),
]
