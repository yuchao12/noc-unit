import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from common_conf.conf import *
from common_conf.xpath.login import LoginLocators

"""登录页"""


def login_successfully(driver, except_username, except_password):
    # 等待页面进入到登录页
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, LoginLocators.login_button))
    )
    # 输入用户名
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable([By.XPATH, LoginLocators.username])
    ).send_keys(except_username)
    # 输入密码
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, LoginLocators.pssword))
    ).send_keys(except_password)
    # 点击登录按钮
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, LoginLocators.login_button))
    ).click()
    time.sleep(4)
    # 判断设备状态、固件版本分布等元素是否存在，存在登录成功，不存在登陆失败
    if driver.find_element_by_xpath(LoginLocators.chart_name).is_displayed():
        print('登录成功')
        return True
    else:
        print('登陆失败')
        return False


