# -*- coding:utf-8 -*-

def _utf8(lst):
    if lst:
        result = ''
        for item in lst:
            result += item.encode("utf8")
            return result
    else:
        return ''