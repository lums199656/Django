import json
from django.http import HttpResponse


def entrance(request):
    print("收到了请求～")
    body = str(request.body, encoding="utf-8")
    print("Body:", body)
    return HttpResponse({"msg": "success"})
