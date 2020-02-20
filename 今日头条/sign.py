# -*- coding: utf-8 -*-
import requests
import os
import urllib


def get_signature(url):
    url = url.replace("com/", "com/toutiao/")
    cwd = os.path.dirname(__file__)
    p = os.popen('cd %s && node signature.js %s' % (cwd, urllib.parse.quote(url)))
    return p.readlines()[-1].strip()


def test_req():
    url = "https://www.toutiao.com/api/pc/feed/"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "referer": "https://www.toutiao.com/ch/news_tech/",
        "x-requested-with": "XMLHttpRequest",
        "accept": "text/javascript, text/html, application/xml, text/xml, */*"
    }
    params = {
        "category": "news_tech",
        "utm_source": "toutiao",
        "widen": "1",
        "max_behot_time": "0",
        "max_behot_time_tmp": "0",
        "tadrequire": "true",
        "as": "A1556EA48DB4FE9",
        "cp": "5E4D342F4EE98E1",
    }
    wait_key = url + "?" + urllib.parse.urlencode(params)
    params["_signature"] = get_signature(wait_key)
    resp = requests.get(url, headers=headers, params=params)
    print(resp.text)


if __name__ == '__main__':
    test_req()
