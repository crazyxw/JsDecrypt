# -*- coding: utf-8 -*-


def detail(arg1):
    arr = [15, 35, 29, 24, 33, 16, 1, 38, 10, 9, 19, 31, 40, 27, 22, 23, 25, 13, 6,11,39,18,20,8,14,21,32,26,2,30,7,4,17,5,3,28,34,37,12,36]
    temp = list(range(40))
    for i in range(len(arg1)):
        value = arg1[i]
        for j in range(len(arr)):
            if arr[j] == i+1:
                temp[j] = value
    return "".join(temp)


def generate_cookie(key, arg1):
    value = detail(arg1)
    temp = ""
    i = 0
    while i < len(value) and i < len(key):
        a = int(value[i: i+2], 16)
        b = int(key[i: i+2], 16)
        c = hex(a ^ b)[2:]
        if len(c) == 1:
            c = '\x30' + c
        temp += c
        i += 2
    return temp


if __name__ == '__main__':
    import requests
    import re
    url = "https://blog.csdn.net/liangyao_/article/details/96460496"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    result = re.search(r"arg1='(.*?)';", resp.text)
    arg1 = result.group(1)
    key = "3000176000856006061501533003690027800375"
    acw_sc__v2 = generate_cookie(key, arg1)
    print(acw_sc__v2)

