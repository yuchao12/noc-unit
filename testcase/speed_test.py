import unittest
from common_fun import speed_test_fun
from common_fun.base import Base
class Speed_Test(Base):

    def test_1_speed_test(self):
        """【正确性检测】能成功进行测速，测速成功新增一条历史记录数据【NOC-9430】"""
        result=speed_test_fun.speed_test(self.driver)
        if result:
            print('测速成功')
            assert True
        else:
            print('测速失败')
            assert False

if __name__ == '__main__':
    unittest.main()







