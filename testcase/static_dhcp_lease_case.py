from noc.common_fun import static_dhcp_lease_fun
from noc.common_conf import conf
from noc.common_fun.base import Base
import unittest


class StaticDhcpLease(Base):
    # @unittest.skip
    def test_01_add_sdl(self):
        """新增mac/ip绑定，路由器配置保存正确【8796】"""
        a = conf.static_dhcp_lease01
        static_dhcp_lease_fun.add_static_dhcp_lease(self.driver, expect_name=a['expect_name'],
                                                    expect_mac=a['expect_mac'],
                                                    expect_ip=a['expect_ip'])
        result = static_dhcp_lease_fun.check_static_dhcp_lease(self.driver,
                                                               check_expect_operation_type=a[
                                                                   'check_expect_operation_type'],
                                                               check_expect_name=a['expect_name'],
                                                               check_expect_mac=a['check_expect_mac'],
                                                               check_expect_ip=a['expect_ip'])
        if result:
            print("【成功】新增mac/ip绑定检测正确！！！")
            assert True
        else:
            print("【失败】新增mac/ip绑定检测失败！！！")
            assert False

    # @unittest.skip
    def test_02_edit_sdl(self):
        '''编辑mac/ip绑定，路由器配置保存正确【9328】'''
        a = conf.static_dhcp_lease02
        static_dhcp_lease_fun.edit_static_dhcp_lease(self.driver, expect_edit_ip=a['expect_edit_ip'],
                                                     expect_name=a['expect_name'],
                                                     expect_mac=a['expect_mac'],
                                                     expect_ip=a['expect_ip'])
        result = static_dhcp_lease_fun.check_static_dhcp_lease(self.driver,
                                                               check_expect_operation_type=a[
                                                                   'check_expect_operation_type'],
                                                               check_expect_name=a['expect_name'],
                                                               check_expect_mac=a['check_expect_mac'],
                                                               check_expect_ip=a['expect_ip'])
        if result:
            print("【成功】编辑mac/ip绑定检测正确！！！")
            assert True
        else:
            print("【失败】编辑mac/ip绑定检测失败！！！")
            assert False

    def test_03_check_sdl(self):
        '''删除mac/ip绑定，成功删除，列表中该项消失【8839】'''
        a = conf.static_dhcp_lease03
        static_dhcp_lease_fun.delete_static_dhcp_lease(self.driver,
                                                       expect_delete_ip=a['expect_delete_ip'])
        result = static_dhcp_lease_fun.check_delete_static_dhcp_lease(self.driver,
                                                                      check_expect_operation_type=a[
                                                                          'check_expect_operation_type'],
                                                                      check_delete_ip=a['check_delete_ip'])
        if result:
            print("【成功】删除mac/ip绑定检测正确！！！")
            assert True
        else:
            print("【失败】删除mac/ip绑定检测失败！！！")
            assert False
