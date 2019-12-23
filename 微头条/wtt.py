# -*- coding: utf-8 -*-
import requests


def get_sinature(uid, ua, max_behot_time="0"):
    data = {"uid": uid, "ua": ua, "max_behot_time": max_behot_time}
    resp = requests.post("http://122.152.215.131:8090/wtt", json=data)
    print(resp.json())


if __name__ == '__main__':
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
    uid = "50025817786"
    get_sinature(uid, useragent)
