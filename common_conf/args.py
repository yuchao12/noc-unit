#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:  yuchao


import argparse

parser = argparse.ArgumentParser(description='NOC Test.')
# 这是指定noc_id
# e.g. -n 99999  需要在python设置的参数  根据不同 的运营商来确定后面的数字
parser.add_argument('-n', dest='noc_id', action='store', help='isp noc_id', required=True)

argss = parser.parse_args()
