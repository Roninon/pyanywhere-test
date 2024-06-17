from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    deeplink = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    return render(
        request,
        "nevergonnagiveyouup/index.html",
        context=dict(deeplink=deeplink)
    )
