#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Author:  yuchao


"""Network Setting"""


class NetworkSettingsLocators(object):
    mode = "//span[text()='{mode}']/../span[1]/span"
    save = "//button[@type='button']"
    save_ok = "//div[@class='el-message-box__btns']/button[2]"
