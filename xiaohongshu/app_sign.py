# -*- coding: utf-8 -*-
import hashlib
from urllib.parse import quote


def generate_md5(data):
    return hashlib.md5(data.encode("utf-8")).hexdigest()


def get_sign(data):
    keys = list(data.keys())
    keys.sort()
    r1 = "".join([i+"="+data[i] for i in keys])
    r2 = quote(r1)

    deviceId = data["deviceId"].encode("utf-8")
    v1 = ""
    v2 = 0
    for i in r2.encode("utf-8"):
        v1 += str(i ^ deviceId[v2])
        v2 = (v2+1) % len(deviceId)
    r3 = generate_md5(v1)
    sign = generate_md5(r3 + data["deviceId"])
    return sign


if __name__ == '__main__':
    params = {
            "page": "1",
            "num": "5",
            "fetch_mode": "1",
            "source": "explore",
            "ads_track_id": "",
            "platform": "android",
            "device_fingerprint": "2019070511014360c1095e3a9c5b2b125182ac4ef9047e01e4b93ed21011a2",
            "device_fingerprint1": "2019070511014360c1095e3a9c5b2b125182ac4ef9047e01e4b93ed21011a2",
            "versionName": "6.6.0",
            "channel": "Xiaomi",
            "sid": "session.1562295755790077877502",
            "lang": "zh-Hans",
            "t": "1563431372",
            "fid": "156335654100d23f4fa1c5ba3929f39cb79289ec3d29",
            "deviceId": "075daade-4c51-3804-8331-c63274c465g7"
            }
    print(get_sign(params))
