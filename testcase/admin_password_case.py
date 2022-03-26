from noc.common_fun import admin_password_fun
from noc.common_conf import conf
from noc.common_fun.base import Base
import unittest


class AdminPassword(Base):
    """新密码和确认密码输入正确，保存成功【9173】"""

    def test_01_change_password(self):
        a = conf.admin_password01
        # admin_password_fun.change_admin_password(self.driver, a['expect_password'])
        result = admin_password_fun.check_admin_password(self.driver, repeat_times=4)
        if result:
            print("【成功】修改管理密码检测正确！！！")
            assert True
        else:
            print("【失败】修改管理密码检测失败！！！")
            assert False
