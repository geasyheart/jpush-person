# -*- coding:utf-8 -*-
"""

__author__ = "zhangyu"

"""
import json

from jpush import abc


class Push(object):
    def __init__(self, jpush, url=abc.JPUSH_URL):
        """
        :param jpush:
        :param url
        """
        self.jpush = jpush  # type: Jpush
        self.platform = None
        self.audience = None
        self.notification = None
        self.message = None
        self.sms_message = None
        self.options = None
        self.cid = None

    @property
    def payload(self):
        """
        要发送的消息体
        :return:
        """
        if not (self.platform and self.audience):
            raise ValueError("platform and audience error!")
        payload = {
                "platform": self.platform,
                "audience": self.audience,
        }
        for key in ("notification", "message", "sms_message", "options", "cid"):
            value = getattr(self, key)
            if value is not None:
                payload[key] = value
        return payload

    def send(self):
        """
        进行推送
        :return:
        """
        # todo:

    def send_validate(self):
        body = json.dumps(self.payload)
        response = self.jpush._request('POST', body, abc.VALIDATE_PUSH_URL)
        return response

