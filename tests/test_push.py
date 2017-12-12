# -*- coding:utf-8 -*-
"""

__author__ = "zhangyu"

"""

from unittest import TestCase

from jpush import Jpush, platform, audience, notification, tag, alias, android, ios, winphone, message, sms_message, \
    options, cid
from jpush.exception import ValidateError

# from jpush-sdk,it is not belong to me!
appkey = "6be9204c30b9473e87bad4dc"
appsecret = "cae22120eed6835e486399a7"


class JpushTest(TestCase):
    def setUp(self):
        self.jpush = Jpush(appkey, appsecret)
        self.push = self.jpush.create_push()

    def test_basic_push(self):
        self.push.platform = platform("ios", "android")
        self.push.audience = audience()
        with self.assertRaises(ValidateError):
            self.push.send_validate()
        self.push.notification = notification(alert="alert")
        self.push.send_validate()

    def test_audience(self):
        self.push.platform = platform("all")
        self.push.audience = audience(**{
            "tag": tag("tcc", "test", "深圳")
        })
        self.assertTupleEqual(self.push.payload['audience']["tag"], ("tcc", "test", "深圳"))

        audiences = audience(**{
            "tag": tag("tcc", "test", "深圳"),
            "alias": alias(*["alias{}".format(i) for i in range(5)])
        })
        self.assertIsInstance(audiences, dict)
        self.assertDictEqual(audiences, {
            "tag": ("tcc", "test", "深圳"),
            "alias": tuple(["alias{}".format(i) for i in range(5)])
        })

        self.push.notification = notification(alert="alert")
        self.push.send_validate()

        with self.assertRaises(ValueError):
            audience(**{
                "tags": tag("tcc", "all")
            })

    def test_notification(self):
        noti = notification(alert="hello,jpush")
        self.assertIsInstance(noti, dict)
        self.assertEqual(noti['alert'], 'hello,jpush')

        noti = notification(
            alert="alert",
            android=android("alert android!"),
            ios=ios("alert ios!"),
            winphone=winphone("alert winphone!")
        )
        self.assertEqual(noti['alert'], 'alert')
        self.assertEqual(noti['android']['alert'], 'alert android!')
        self.assertEqual(noti['ios']['alert'], 'alert ios!')
        self.assertEqual(noti['winphone']['alert'], 'alert winphone!')

        self.push.platform = platform("all")
        self.push.notification = noti
        self.push.audience = audience(**{
            "tag": tag("tcc", "all")
        })
        self.push.send_validate()

    def test_message(self):
        msg = message("hello world")
        sms_msg = sms_message("content", 20)
        noti = notification(alert="hello,jpush")
        self.push.notification = noti
        self.push.platform = platform("all")
        self.push.audience = audience(**{
            "tag": tag("tcc", "all")
        })
        self.push.message = msg
        self.push.sms_message = sms_msg
        self.push.send_validate()

    def test_options_and_cid(self):
        option = options()
        c = cid("cid")
        self.assertDictEqual(option, {})
        self.assertDictEqual(c, {"cid": "cid"})

    def tearDown(self):
        self.jpush.session.close()
