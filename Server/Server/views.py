import json
from django.http import HttpResponse
import os

def entrance(request):
    print("Get Request～")
    # body = str(request.body, encoding="utf-8")
    # print("Body:", body)
    imgData = base64.b64decode(request.body)
    with open("/home/luminshe/lightPictures/lights.png", "wb") as f:
        f.write(imgData)
    log_path = "/home/luminshe/lightPictures/results/result.json"
    print("logs' path: " + log_path)
    print("Start to listening ...")
    heartbeat = 0
    while True:
        if os.path.exists(log_path):
            print("succeed to get log!")
            os.remove(imgData)
            with open(log_path, "r") as f2:
                res = json.load(f2)
            os.remove(log_path)
            for light in res["res"]:
                if light['label'] == "1":
                    return HttpResponse({"msg": "failed"})
            break
        time.sleep(0.1)
        heartbeat += 1
        if heartbeat % 20 == 0:
            print("Having listen " + str(int(heartbeat / 10)) + "s ...")
    return HttpResponse({"msg": "success"})
