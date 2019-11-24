#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/12/8

import time

from rest_framework import fields


class DurationDateField(fields.Field):
    """
    自定义日期字段
    """
    def to_representation(self, value):
        # serializers.DateTimeField

        minute = 60
        hour = minute * 60
        day = hour * 24
        month = day * 30
        current_time = time.time()
        diff_val = current_time - time.mktime(value.timetuple())
        if diff_val < 0:
            return
        month_c = diff_val / month
        week_c = diff_val / (7 * day)
        day_c = diff_val / day
        hour_c = diff_val / hour
        min_c = diff_val / minute
        if month_c >= 1:
            pub_date = "%s月前" % int(month_c)
        elif week_c >= 1:
            pub_date = "%s周前" % int(week_c)
        elif day_c >= 1:
            pub_date = "%s天前" % int(day_c)
        elif hour_c >= 1:
            pub_date = "%s小时前" % int(hour_c)
        elif min_c >= 1:
            pub_date = "%s分钟前" % int(min_c)
        else:
            pub_date = "刚刚"
        return pub_date

    def to_internal_value(self, data):
        if not data:
            return None

        return data


class CustomCharField(fields.Field):

    def to_representation(self, value):
        return "{}第{}期".format(value.course, value.semester)

    def to_internal_value(self, data):
        return data
