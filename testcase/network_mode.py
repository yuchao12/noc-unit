#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


from noc.common_conf import conf
from noc.common_fun.base import Base
from noc.common_fun import network_mode_fun
import unittest


class NetworkSettings(Base):

    # @unittest.skip("跳过")
    def test_01_change_network_settings(self):
        """【操作】修改工作模式"""
        pass
        network_mode_fun.change_network_settings(self.driver, "Router mode")

    # @unittest.skip("跳过")
    def test_02_check_network_settings(self):
        """【检验】检查工作模式"""
        pass
        result = network_mode_fun.check_network_settings(self.driver, "Router mode", repeat_times=12)
        if result:
            print("【成功】修改工作模式成功！！！")
            assert True
        else:
            print("【失败】修改工作模式失败！！！")
            assert False
