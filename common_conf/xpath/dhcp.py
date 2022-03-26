#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  yuchao


"""DHCP"""


class DhcpLocators(object):
    lan_ip = "//div[@class='mesh-settings dhcp']/form/div[1]/div[2]/div/input"

    # 地址池 开始的ip 与 结束的ip
    start_ip = "//div[@class='mesh-settings dhcp']/form/div[2]/div[2]/div[1]/input"
    end_ip = "//div[@class='mesh-settings dhcp']/form/div[3]/div/div/input"

    lease_time = "//div[@class='el-select']/div/input"
    lease_time_all = "//div[@class='el-scrollbar']/div[1]/ul/li//span[text()='{text}']"
    save = "//button[@type='button']"
