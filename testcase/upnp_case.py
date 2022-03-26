from noc.common_fun import upnp_fun
from noc.common_conf import conf
from noc.common_fun.base import Base


class Upnp(Base):
    def test_01_change_upnp(self):
        """开启UPnP保存【8764】"""
        a = conf.upnp01
        upnp_fun.change_upnp(self.driver, expect_status=a['expect_status'])
        result = upnp_fun.check_upnp(self.driver, check_expect_status=a['check_expect_status'],
                                     repeat_times=a['repeat_times'])
        if result:
            print("【成功】开启UPnp状态配置正确！！！")
            assert True
        else:
            print("【失败】开启UPnp状态配置失败！！！")
            assert False

    def test_02_change_upnp(self):
        """关闭UPnP保存【8764】"""
        a = conf.upnp02
        upnp_fun.change_upnp(self.driver, expect_status=a['expect_status'])
        result = upnp_fun.check_upnp(self.driver, check_expect_status=a['check_expect_status'],
                                     repeat_times=a['repeat_times'])
        if result:
            print("【成功】关闭UPnp状态配置正确！！！")
            assert True
        else:
            print("【失败】关闭UPnp状态配置失败！！！")
            assert False
