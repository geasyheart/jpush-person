# -*- coding:utf-8 -*-
"""

__author__ = "zhangyu"

"""


def tag(*tags):
    """
    :param tags
    :return:
    :rtype: list
    """
    # pass verify
    return tags


def tag_and(*tag_ands):
    """
    :param tag_ands:
    :return:
    :rtype: list
    """
    # pass verify
    if len(tag_ands) > 20:
        raise ValueError("tag_and error, max: 20")
    return tag_ands


def tag_not(*tag_nots):
    """
    :param tag_nots
    :return:
    """
    # pass verify
    if len(tag_nots) > 20:
        raise ValueError("tag_nots error, max: 20")
    return tag_nots


def alias(*aliases):
    """
    :param aliases
    :return:
    :rtype: list
    """
    # pass verify
    for alias in aliases:
        if len(alias) > 40:
            raise ValueError("alias error!")
    return aliases


def registration_id(*register_ids):
    """
    :param register_ids:
    :return:
    """
    # pass verify
    if len(register_ids) > 1000:
        raise ValueError("regiseter_ids error!")
    return register_ids


def segment(*segments):
    """
    :param segments:
    :return:
    :rtype: list
    """
    # pass verify
    if len(segments) > 1:
        raise ValueError("segments error!")
    return segments


def abtest(*abtests):
    """
    :param abtests:
    :return:
    :rtype: list
    """
    # pass verify
    if len(abtests) > 1:
        raise ValueError("abtest error!")
    return abtests
