from noc.common_fun.base import Base
from noc.common_fun import ddns_fun
from noc.common_conf import conf


class Ddns(Base):
    def test_01_change_ddns(self):
        a = conf.ddns01
        """修改所有的配置【9308】，且服务提供商为'DynDN'【8617】，且启用勾选【8620】"""
        ddns_fun.change_ddns(self.driver, expect_server_provider=a["expect_dyndns_server_provider"],
                             expect_domain=a["expect_domain"],
                             expect_username=a["expect_username"],
                             expect_password=a["expect_password"],
                             expect_status=a["expect_status"]
                             )

        result = ddns_fun.check_ddns(self.driver, check_expect_server_provider=a["expect_dyndns_server_provider"]
                                     , check_expect_domain=a["expect_domain"],
                                     check_expect_password=a["check_expect_password"],
                                     check_expect_username=a["check_expect_username"], repeat_times=a["repeat_times"],
                                     check_expect_status=a["check_expect_status"])
        if result:
            print("【成功】修改DDNS所有的配置正确！！！")
            assert True
        else:
            print("【失败】修改DDNS所有的配置失败！！！")
            assert False

    def test_02_change_ddns(self):
        """修改提供商为"花生壳"【8618】，启用状态不勾选【8621】"""
        a = conf.ddns02
        ddns_fun.change_ddns(self.driver, expect_server_provider=a["expect_dyndns_server_provider"],
                             expect_status=a["expect_status"])

        result = ddns_fun.check_ddns(self.driver, check_expect_server_provider=a["expect_dyndns_server_provider"],
                                     check_expect_status=a["check_expect_status"], repeat_times=a["repeat_times"])
        if result:
            print("【成功】修改DDNS提供商为'花生壳'、启用状态不勾选配置正确！！！")
            assert True
        else:
            print("【失败】修改DDNS提供商为'花生壳'、启用状态不勾选配置失败！！！")
            assert False

    def test_03_change_ddns(self):
        """修改域名，用户名，密码【8619】"""
        a = conf.ddns03
        ddns_fun.change_ddns(self.driver, expect_domain=a["expect_domain"],
                             expect_username=a["expect_username"],
                             expect_password=a["expect_password"])

        result = ddns_fun.check_ddns(self.driver, check_expect_domain=a["expect_domain"],
                                     check_expect_password=a["check_expect_password"],
                                     check_expect_username=a["check_expect_username"], repeat_times=a["repeat_times"])
        if result:
            print("【成功】修改DDNS修改域名，用户名，密码配置正确！！！")
            assert True
        else:
            print("【失败】修改DDNS修改域名，用户名，密码配置失败！！！")
            assert False
