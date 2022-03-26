#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


from common_conf import conf
from common_fun.base import Base
from common_fun import dhcp_fun
import unittest


class Dhcp(Base):

    # def setUp(self):
    #     super(Dhcp, self).setUp()
    #     dhcp_fun.move_to_dhcp_page(self.driver)

    # @unittest.skip("跳过")
    def test_01_change_dhcp(self):
        """【操作】修改Dhcp配置"""
        dhcp_fun.change_dhcp(self.driver,
                             except_lan_ip="192.168.127.1",
                             except_start_ip="108",
                             except_end_ip="190",
                             except_lease_time="1 Week")

    def test_02_check_dhcp(self):
        """【检验】检查Dhcp配置"""
        result = dhcp_fun.check_dhcp(self.driver,
                                     except_lan_ip="192.168.127.1",
                                     except_start_ip="108",
                                     except_end_ip="190",
                                     except_lease_time="1 Week",
                                     repeat_times=5)
        if result:
            print("【成功】修改DHCP成功！！！")
            assert True
        else:
            print("【失败】修改DHCP失败！！！")
            assert False
