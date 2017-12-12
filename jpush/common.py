# -*- coding:utf-8 -*-
"""

__author__ = "zhangyu"

"""

import logging

import requests

from jpush.exception import RequestError, ValidateError
from jpush.push.common import Push

logger = logging.getLogger("jpush")


class Jpush(object):
    def __init__(self, appkey, appsecret):
        """

        :param appkey:
        :param appsecret:
        """
        self.appkey = appkey
        self.appsecret = appsecret
        self.session = requests.Session()
        self.session.auth = (appkey, appsecret)

    def _request(self, method, body, url, params=None, headers=None, timeout=5):
        if headers is None:
            headers = {}
        headers.setdefault('content-type', 'application/json;charset:utf-8')
        try:
            response = self.session.request(method=method, url=url, data=body, params=params,
                                            headers=headers, timeout=timeout)
        except requests.RequestException as e:
            raise RequestError(details=str(e))
        else:
            if not (200 <= response.status_code < 400):
                body = response.json()
                raise ValidateError(details=body)
            return response

    def create_push(self):
        return Push(self)
