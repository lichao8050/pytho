# _*_ coding: utf-8 _*_
# @Time     : 2022/4/25 20:24
# @Author   : Mr_Li
# @FileName :

import requests


class HttpRequest:
    sess = requests.session()

    def all_send_request(self, method, url, **kwargs):
        res = HttpRequest.sess.request(method, url, **kwargs)
        return res
