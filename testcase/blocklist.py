from common_fun.base import Base
from common_fun import blocklist_fun
import unittest


class BlockList(Base):
    def test01_add_blocklist(self):
        print('添加11111111111111111111111111')
        blocklist_fun.add_new_blocklist(self.driver, '123456789045', "黑名单3")

    def test02_check_add_blocklist(self):
        print('检查222222222222222222222222222')
        blocklist_fun.check_blocklist(self.driver, '12:34:56:78:90:45', '黑名单3')

    # @unittest.skip("跳过")
    def test03_del_blocklist(self):
        print('删除3333333333333333333333333333333')

        blocklist_fun.delete_blocklist(self.driver, 1)

    def test04_check_del_blocklist(self):
        print('检查4444444444444444444444444444444444444')
        result = blocklist_fun.check_blocklist(self.driver, '12:34:56:78:90:45', '黑名单')
        print(result)
        if not result:
            print("【成功】！！！！！！1")
            assert True
        else:
            assert False
