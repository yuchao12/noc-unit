#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:  yuchao
class TimeLocators(object):
    # other settings 菜单栏
    other_setting_menu = '//div[text()="Other settings"]'
    # time zone菜单栏
    time_zone_menu = '//body/div[@class="el-menu--horizontal menus__popper-menu"]/ul/li[text()=" Time zone "]'
    # 时区输入框
    time_zone_input = '//input[@class="el-input__inner"]'
    # 时区下拉选择项
    select_timezone_coutry = '//li[@class="el-select-dropdown__item"]/div[@class="timezone-coutry"]/div[text()="{}"]'
    # 保存按钮
    save_button = '//button[@class="el-button el-button--primary"]'
    # 被选中的时区
    selected_timezone_country = '//li[@class="el-select-dropdown__item selected"]'
    # 页面加载进度条
    loading="//div[@id='nprogress']"
