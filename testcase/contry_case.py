from noc.common_fun.base import Base
from noc.common_fun import country_fun
from noc.common_conf import conf


class Country(Base):
    def test_01_check_country(self):
        """进入到国家及地区页，实时拉取路由器的国家及地区配置【8401】"""
        result = country_fun.check_country(self.driver, conf.expect_init_country)
        if result:
            print("【成功】初始化国家显示正确！！！")
            assert True
        else:
            print("【失败】初始化国家显示失败！！！")
            assert False

    def test_02_change_country(self):
        """修改国家并检查修改是否正确【8411】"""
        country_fun.change_country(self.driver, conf.expect_country)
        result = country_fun.check_country(self.driver, conf.check_expect_country,repeat_times=5)
        if result:
            print("【成功】修改国家及地区成功！！！")
            assert True
        else:
            print("【失败】修改国家及地区失败！！！")
            assert False
