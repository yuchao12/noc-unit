from common_conf.conf import add_web_wan_access, change_web_wan_access
from common_fun import remote_management_fun
from common_fun.base import Base
import unittest
class Remote_Management(Base):

    def test_1_add_web_wan_access(self):
        """【保存】开关打开时，且当端口号和IP地址格式都正确，点击“保存”后有toast提示【NOC-7391】"""
        remote_management_fun.add_web_wan_access(self.driver,expect_status=add_web_wan_access["swith_on"],# web wan access 开启的状态
                                                 expect_port=add_web_wan_access["port_num"],#端口号
                                                 expect_ip=add_web_wan_access["ip_ad"])#ip地址
        result = remote_management_fun.check_web_wan_access(self.driver, expect_status=add_web_wan_access["swith_on"],# web wan access 开启的状态
                                                            expect_port=add_web_wan_access["port_num"],#端口号
                                                            expect_ip=add_web_wan_access["ip_ad"],#ip地址
                                                            expect_operation_type=add_web_wan_access["type"]) #操作类型
        if result:
            print('配置的预期值与实际值相同，添加成功')
            assert True
        else:
            print('配置的预期值与实际值不同，添加失败')
            assert False

    def test_2_edit_web_wan_access(self):
        """【正确性检查】能正常修改配置，并下发成功【NOC-10087】"""
        remote_management_fun.change_web_wan_access(self.driver,expect_status=change_web_wan_access["swith_on"],# web wan access 开启的状态
                                                 expect_port=change_web_wan_access["port_num"],#端口号
                                                 expect_ip=change_web_wan_access["ip_ad"])#ip地址)
        result = remote_management_fun.check_web_wan_access(self.driver, expect_status=change_web_wan_access["swith_on"],# web wan access 开启的状态
                                                            expect_port=change_web_wan_access["port_num"],#端口号
                                                            expect_ip=change_web_wan_access["ip_ad"],#ip地址
                                                            expect_operation_type=change_web_wan_access["type"]) #操作类型
        if result:
            print('修改的预期值与实际值相同，修改成功')
            assert True
        else:
            print('修改的预期值与实际值不同，修改失败')
            assert False

if __name__ == '__main__':
    unittest.main()
