# -*- coding:utf-8 -*-
"""

__author__ = "zhangyu"

"""
from pprint import pprint


class JPushError(Exception):
    code = 0
    message = ''
    details = ''

    def __init__(self, message=None, details=None):
        """
        :type message: str
        :type details: str,dict
        :param message:
        :param details:
        """
        if message:
            self.message = message
        if details:
            self.details = details

    def to_json(self):
        return {
            "code": self.code,
            "message": self.message,
            "details": self.details
        }

    def __str__(self):
        return repr(self.details)


class RequestError(JPushError):
    code = 100
    message = "request error!"


class ValidateError(JPushError):
    code = 101
    message = "format error!"
