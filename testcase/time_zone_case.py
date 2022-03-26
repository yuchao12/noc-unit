from noc.common_fun.base import Base
from noc.common_fun import time_zone_fun
from noc.common_conf import conf
import unittest


class TimeZone(Base):
    '''进入到时区页，实时拉取路由器的时区配置【8417】'''

    def test_01_check_time_zone(self):
        result = time_zone_fun.check_time_zone(self.driver, conf.expect_init_timezone_country)
        if result:
            print("【成功】初始化时区显示正确！！！")
            assert True
        else:
            print("【失败】初始化时区显示失败！！！")
            assert False

    """修改国家并检查修改是否正确【8415】"""

    # @unittest.skip("跳过")
    def test_02_change_time_zone(self):
        time_zone_fun.change_time_zone(self.driver, conf.expect_timezone_country)
        result = time_zone_fun.check_time_zone(self.driver, conf.check_expect_timezone_country)
        if result:
            print("【成功】修改及检查时区正确！！！")
            assert True
        else:
            print("【失败】修改及检查时区失败！！！")
            assert False
