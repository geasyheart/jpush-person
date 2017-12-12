# -*- coding:utf-8 -*-
"""

__author__ = "zhangyu"

"""


def android(alert, title=None, builder_id=None, priority=None, category=None, style=None, alert_type=None,
            big_text=None, inbox=None, big_pic_path=None, extras=None):
    """
    :type alert: str
    :type title: str
    :type builder_id: int
    :type priority: int
    :type category: str
    :type style: int
    :type alert_type: int
    :type big_text: str
    :type inbox: dict
    :type big_pic_path: str
    :type extras: dict
    :param alert:
    :param title:
    :param builder_id:
    :param priority:
    :param category:
    :param style:
    :param alert_type:
    :param big_text:
    :param inbox:
    :param big_pic_path:
    :param extras:
    :return:
    :rtype: dict
    """
    payload = {"alert": alert}
    if title is not None:
        payload["title"] = title
    if builder_id is not None:
        payload["builder_id"] = builder_id
    if priority is not None:
        payload["priority"] = priority
    if category is not None:
        payload["category"] = category
    if style is not None:
        payload["style"] = style
    if alert_type is not None:
        payload["alert_type"] = alert_type
    if big_text is not None:
        payload["big_text"] = big_text
    if inbox is not None:
        payload["inbox"] = inbox
    if big_pic_path is not None:
        payload["big_pic_path"] = big_pic_path
    if extras is not None:
        payload["extras"] = None
    return payload


def ios(alert, sound=None, badge=1, content_available=None, mutable_content=None, category=None, extras=None):
    """
    :type alert: str, dict
    :type sound: str
    :type badge: int
    :type content_available: bool
    :type mutable_content: bool
    :type category: str
    :type extras: dict
    :param alert:
    :param sound:
    :param badge:
    :param content_available:
    :param mutable_content:
    :param category:
    :param extras:
    :return:
    """
    payload = {"alert": alert}
    if sound is not None:
        payload["sound"] = sound
    if badge is not None:
        payload["badge"] = badge
    if content_available is not None:
        payload["content-available"] = content_available
    if mutable_content is not None:
        payload["mutable-content"] = mutable_content
    if category is not None:
        payload["category"] = category
    if extras is not None:
        payload["extras"] = extras
    return payload


def winphone(alert, title=None, open_page=None, extras=None):
    """
    :type alert: str
    :type title: str
    :type open_page: str
    :type extras:dict
    :param alert:
    :param title:
    :param open_page:
    :param extras:
    :return:
    """
    payload = {"alert": alert}
    if title is not None:
        payload["title"] = title
    if open_page is not None:
        payload["_open_page"] = open_page
    if extras is not None:
        payload["extras"] = extras
    return payload
