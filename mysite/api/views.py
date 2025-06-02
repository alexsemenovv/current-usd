from django.http import HttpRequest, HttpResponse


def get_current_usd(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Hello world!<h1>")