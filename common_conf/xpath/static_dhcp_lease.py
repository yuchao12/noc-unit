#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:  yuchao
class StaticDhcpLeaseLocators(object):
    # 高级设置菜单栏
    advanced_settings_menu = '//div[text()="Advanced settings"]'
    # 页面加载进度条
    loading = "//div[@id='nprogress']"
    # mac绑定ip菜单栏
    sdl_menu = '//body/div[@class="el-menu--horizontal menus__popper-menu"]/ul/li[text()=" Static DHCP Lease "]'
    # add按钮
    add_button = '//button[@class="el-button rsvdip__header-button el-button--default"]'
    # name输入框
    name_input = '//form/div[1]/div/div/input'
    # mac输入框
    mac_input = '//form/div[2]/div/div/input'
    # ip输入框
    ip_input = '//form/div[3]/div/div/input'
    # 保存按钮
    save_button = '//button[@class="el-button el-button--primary"]'
    # 列表中name获取({}内添加ip)
    name_list = '//tr/td[3]/div[contains(.,"{}")]/../../td[1]/div'
    # 列表中mac获取
    mac_list = '//tr/td[3]/div[contains(.,"{}")]/../../td[2]/div'
    # 列表中的ip获取
    ip_list = '//tr/td[3]/div[contains(.,"{}")]'
    # 编辑按钮
    edit_button = '//tr/td[3]/div[contains(.,"{}")]/../../td[4]/div/button[1]'
    # 删除按钮
    delete_button = '//tr/td[3]/div[contains(.,"{}")]/../../td[4]/div/button[2]'
    # 删除弹框的确定按钮
    ok_button = '//div[@class="el-message-box__btns"]/button[@class="el-button el-button--default el-button--small el-button--primary "]'
