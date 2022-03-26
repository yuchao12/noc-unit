from testcase.admin_password import AdminPassword
from testcase.port_forwarding import Port_Forwarding
from testcase.remote_management import Remote_Management
from testcase.speed_test import Speed_Test
from testcase.vpn import Vpn
from testcase.wifi_settings import WifiSettings
from testcase.dhcp import Dhcp
from testcase.blocklist import BlockList
from testcase.network_settings import NetworkSettings
import unittest
from unittest import TestLoader
from BeautifulReport import BeautifulReport
import os

"""
suit=unittest.TestSuite
suit.addTests(unittest.TestLoader.loadTestsFromModule(login))
rest=unittest.TestResult()
suit.run(rest)
print(rest.__dict__)
"""

def core():
    s = []
    # 将要执行模块的用例添加到列表
    class_tests = [
 Remote_Management,Port_Forwarding,Vpn
    ]
    # 循环遍历用例列表
    for t in class_tests:
        suite = TestLoader().loadTestsFromTestCase(t)
        s.append(suite)
    t_s = unittest.TestSuite(s)
    return t_s


if __name__ == "__main__":
    t_suites = core()
    result = BeautifulReport(t_suites)
    report_dir = r'./report/'
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    result.report(filename="noc-功能自动化测试报告",
                  description="noc-功能自动化测试报告",
                  report_dir=report_dir)
