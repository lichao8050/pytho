# _*_ coding: utf-8 _*_
# @Time     : 2022/4/25 20:24
# @Author   : Mr_Li
# @FileName : test_case.py
from urllib import response

import requests


class HttpReQuest:
    cookie = ""
    cookie_data = ""
    sess = requests.session()

    def test_login_api(self):
        url = "http://kbs.matrixdesign.cn/api/pmtapi/base_Account/login"
        data = {
            'username': 'heqiangming',
            'password': 'abc123456'
        }
        # 实例化请求
        # res = requests.post(url=url, data=data)
        res = HttpReQuest.sess.request(method='post', url=url, data=data)
        print(res.headers)
        print(res.status_code)
        HttpReQuest.cookie = res.headers["Set-Cookie"]
        HttpReQuest.cookie_data = res.cookies
        print(HttpReQuest.cookie)

    def test_action_view(self):
        url = "http://kbs.matrixdesign.cn/api/authapi/bsProInfo/getSWById"
        headers = {"Set-Cookie": HttpReQuest.cookie}
        data = {"id": "1518864408166666241"}
        # res = requests.post(url=url, headers=headers, data=data, cookies=HttpReQuest.cookie_data)
        res = HttpReQuest.sess.request(method='post', url=url, data=data)
        print(res.headers)
        print(res.status_code)
        print(res.json())


if __name__ == '__main__':
    HttpReQuest().test_login_api()
    HttpReQuest().test_action_view()
