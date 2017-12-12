# -*- coding:utf-8 -*-
"""

__author__ = "zhangyu"

"""


def platform(*types):
    """

    :param types:
    :rtype: str, tuple
    :return:
    """
    if len(types) == 1 and types[0] == "all":
        return "all"
    __platforms__ = ("android", "ios", "winphone")
    for pf in types:
        if pf not in __platforms__:
            raise ValueError("platform {} error!".format(pf))
    return [i for i in types]


def audience(**audiences):
    """

    :param audiences:
    :return:
    :rtype: dict
    """
    if len(audiences) == 0:
        return "all"

    payload = {}
    __attr__ = ("tag", "tag_and", "tag_not", "alias", "registration_id", "segment", "abtest")
    for k, v in audiences.items():
        if k not in __attr__:
            raise ValueError("audience {} not in {}".format(k, __attr__))
        payload.setdefault(k, v)
    return payload


def notification(alert, android=None, ios=None, winphone=None):
    """
    :type alert: str
    :type android: android
    :type ios: ios
    :type winphone: winphone
    :param alert:
    :param android:
    :param ios:
    :param winphone:
    :return:
    :rtype: dict
    """
    payload = {}
    payload.setdefault("alert", alert)
    if android:
        payload.setdefault("android", android)
    if ios:
        payload.setdefault("ios", ios)
    if winphone:
        payload.setdefault("winphone", winphone)
    return payload


def message(msg_content, title=None, content_type=None, extras=None):
    """
    :type msg_content: str
    :type title: str
    :type content_type: str
    :type extras: dict
    :param msg_content:
    :param title:
    :param content_type:
    :param extras:
    :return:
    :rtype: dict
    """
    payload = {"msg_content": msg_content}
    if title is not None:
        payload["title"] = title
    if content_type is not None:
        payload["content_type"] = content_type
    if extras is not None:
        payload["extras"] = extras

    return payload


def sms_message(content, delay_time):
    """
    :type content: str
    :type delay_time: int

    :param content:
    :param delay_time:
    :return:
    :rtype: dict
    """
    return {
        "content": content,
        "delay_time": delay_time
    }


def options(sendno=None, time_to_live=None, override_msg_id=None, apns_production=None, apns_collapse_id=None,
            big_push_duration=None):
    """

    :param sendno:
    :param time_to_live:
    :param override_msg_id:
    :param apns_production:
    :param apns_collapse_id:
    :param big_push_duration:
    :return:
    """
    payload = {}
    if sendno:
        payload["sendno"] = sendno
    if time_to_live:
        payload["time_to_live"] = time_to_live
    if override_msg_id:
        payload["override_msg_id"] = override_msg_id
    if apns_production:
        payload["apns_production"] = apns_production
    if apns_collapse_id:
        payload["apns_collapse_id"] = apns_collapse_id
    if big_push_duration:
        payload["big_push_duration"] = big_push_duration
    return payload


def cid(cid):
    """

    :return:
    """
    return {
        "cid": cid
    }
