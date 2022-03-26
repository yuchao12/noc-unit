#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:  yuchao

class Speed_test_Locators(object):
    net_seting='//div[text()="Network"]' # 网络设置模块
    speed= '//li[contains(text(), " Speed test ")]' #网络测速入口
    speed_button= '//button[@class="el-button action__btn el-button--default el-button--medium"]' #网络测速按钮
    speed_total='el-pagination__total' #网络测速记录的总条数
    expect_url = 'https://noc.merckuwifi.net/mesh/{}/setting/speed_test'  # 网络测速的网址
    speed_status = '//div[@class="action__line action__line--pending"]'  #测速的状态
