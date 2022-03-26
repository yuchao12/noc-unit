from noc.common_fun import dmz_fun
from noc.common_conf import conf
from noc.common_fun.base import Base


class Dmz(Base):
    def test_01_change_dmz(self):
        """开启DMZ【8753】，且ip输入正确保存【8752】"""
        a = conf.dmz01
        dmz_fun.change_dmz(self.driver, expect_dmz_host=a["expect_dmz_host"], expect_status=a["expect_status"])
        result = dmz_fun.check_dmz(self.driver, repeat_times=a["repeat_times"],
                                   check_expect_dmz_host=a['check_expect_dmz_host'],
                                   check_expect_status=a['check_expect_status'])
        if result:
            print("【成功】DMZ开启状态，输入ip配置正确！！！")
            assert True
        else:
            print("【失败】DMZ开启状态，输入ip配置失败！！！")
            assert False

    def test_02_change_dmz(self):
        """开启DMZ【8753】，且编辑ip保存【9000】"""
        a = conf.dmz02
        dmz_fun.change_dmz(self.driver, expect_dmz_host=a["expect_dmz_host"], expect_status=a["expect_status"])
        result = dmz_fun.check_dmz(self.driver, repeat_times=a["repeat_times"],
                                   check_expect_dmz_host=a['check_expect_dmz_host'],
                                   check_expect_status=a['check_expect_status'])
        if result:
            print("【成功】DMZ编辑ip配置正确！！！")
            assert True
        else:
            print("【失败】DMZ编辑ip配置失败！！！")
            assert False

    def test_03_change_dmz(self):
        """关闭DMZ【8754】"""
        a = conf.dmz03
        dmz_fun.change_dmz(self.driver, expect_status=a["expect_status"])
        result = dmz_fun.check_dmz(self.driver, repeat_times=a["repeat_times"],
                                   check_expect_status=a['check_expect_status'])
        if result:
            print("【成功】关闭DMZ配置正确！！！")
            assert True
        else:
            print("【失败】关闭DMZ配置失败！！！")
            assert False
