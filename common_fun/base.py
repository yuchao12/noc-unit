import unittest
import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from common_conf import conf
from common_fun import login_fun
from common_fun import user_public_fun
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Base(unittest.TestCase):
    driver = webdriver.Chrome(executable_path=r'E:\software\webdriver\chromedriver.exe')

    # 初始化准备：启动浏览器、进入网站、放大窗口
    @classmethod
    def setUpClass(cls):
        cls.driver.get(conf.url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        # 用户登录
        login_fun.login_successfully(cls.driver, conf.root_username, conf.root_password)
        time.sleep(3)

        # 进入设备列表
        js = 'document.getElementsByClassName("el-menu-item")[2].click()'
        cls.driver.execute_script(js)
        time.sleep(3)
        user_public_fun.search_sn_and_click(cls.driver, conf.except_sn, "online", 3)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
