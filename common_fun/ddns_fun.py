import time
from common_conf.xpath.ddns import DdnsLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def move_to_ddns_page(driver):
    repeat_times = 3
    while repeat_times > 0:
        print(f'这是进入DDNS页倒数第{repeat_times}次')
        try:
            # 判断当前页面是否为时区页
            if "setting/ddns" in driver.current_url:
                print('刷新')
                driver.refresh()
            else:
                # 鼠标移动到高级设置
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(DdnsLocators.advanced_settings_menu)).perform()
                time.sleep(0.5)
                # 鼠标移动到国家及地区菜单
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(DdnsLocators.ddns_menu)).perform()
                # 点击国家及地区菜单
                driver.find_element_by_xpath(DdnsLocators.ddns_menu).click()
                time.sleep(0.5)
            # 等待进度条加载完成
            WebDriverWait(driver, 20).until_not(
                EC.element_to_be_clickable((By.XPATH, DdnsLocators.loading))
            )
            time.sleep(0.5)
            print('进入ddns页面成功')
            return True
        except:
            driver.refresh()
            time.sleep(2)
        finally:
            repeat_times -= 1
    print("进入ddns页面报错")
    assert False


def change_ddns(driver, expect_server_provider=None, expect_domain=None, expect_username=None, expect_password=None,
                expect_status=None):
    repeat_times = 3
    while repeat_times > 0:
        print(f"这是修改ddns倒数第{repeat_times}次")
        move_to_ddns_page(driver)
        try:
            if expect_server_provider is not None:
                print(11111111)
                # 点击出服务提供商下拉框
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, DdnsLocators.service_provider_input))
                ).click()
                print(2222222222)
                # 选择服务提供商
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, DdnsLocators.service_provider_select.format(expect_server_provider)))
                ).click()

            if expect_domain is not None:
                # 清空域名输入框的内容
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, DdnsLocators.domain_input))
                ).clear()
                # 输入域名
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, DdnsLocators.domain_input))
                ).send_keys(expect_domain)

            if expect_username is not None:
                # 清空用户名输入框
                print(333333333333333333)
                driver.find_element_by_xpath(DdnsLocators.username_ddns_input).clear()

                # WebDriverWait(driver, 10).until(
                # EC.element_to_be_clickable(By.XPATH, DdnsLocators.username_ddns_input)).clear()
                print(44444444444444)
                # 输入用户名
                driver.find_element_by_xpath(DdnsLocators.username_ddns_input).send_keys(
                    expect_username)
                # WebDriverWait.until(EC.element_to_be_clickable(By.XPATH, DdnsLocators.username_ddns_input)).send_keys(
                # expect_username)
                print(6666666666666666)

            if expect_password is not None:
                # 清空密码输入框
                print(77777777777)
                driver.find_element_by_xpath(DdnsLocators.password_ddns_input).clear()
                # 输入密码
                print(8888888888888888888)
                driver.find_element_by_xpath(DdnsLocators.password_ddns_input).send_keys(
                    expect_password)
                print(99999999999999999)
            if expect_status is not None:
                # 获取当前是否开启的状态
                actual_status = driver.find_element_by_xpath(DdnsLocators.status_check).get_attribute('class')
                print(actual_status)
                if 'is-checked' in actual_status:
                    actual_status = "on"
                else:
                    actual_status = "off"
                print(actual_status)
                if expect_status == actual_status:
                    pass
                else:
                    # 点击开启的复选框
                    ActionChains(driver).move_to_element(
                        driver.find_element_by_xpath(DdnsLocators.status_checkbox)).perform()
                    time.sleep(0.1)
                    WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, DdnsLocators.status_checkbox))
                    ).click()
                # 最后保存
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, DdnsLocators.save_button))
                ).click()
            print("修改DDNS成功")
            return
        except:
            pass
        finally:
            repeat_times -= 1
    print("修改DDNS失败")
    assert False


def check_ddns(driver, check_expect_server_provider=None, check_expect_domain=None, check_expect_username=None,
               check_expect_password=None,
               check_expect_status=None, repeat_times=3):
    while repeat_times > 0:
        print(f"这是检查DDNS倒数第{repeat_times}次")
        move_to_ddns_page(driver)
        try:
            if check_expect_server_provider is not None:
                # 获取当前服务商的值
                print(22222222222)
                actual_server_provider = driver.find_element_by_xpath(
                    DdnsLocators.service_provider_input).get_attribute(
                    "value")
                print("实际的服务商：" + actual_server_provider)
                print("期望的服务商：" + check_expect_server_provider)
                if actual_server_provider != check_expect_server_provider:
                    if repeat_times == 1:
                        print('期望的服务商和实际的服务商不一致')
                        return False
                    assert False
            if check_expect_domain is not None:
                actual_domain = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, DdnsLocators.domain_input))
                ).get_attribute("value")
                print("实际的域名:" + actual_domain)
                print("期望的域名:" + check_expect_domain)
                if actual_domain != check_expect_domain:
                    if repeat_times == 1:
                        print('期望的域名和实际的域名不一致')
                        return False
                    assert False

            if check_expect_username is not None:
                actual_username = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, DdnsLocators.username_ddns_input))
                ).get_attribute("value")
                print("实际的用户名:" + actual_username)
                print("期望的用户名:" + check_expect_username)
                if actual_username != check_expect_username:
                    if repeat_times == 1:
                        print('期望的用户名和实际的用户名不一致')
                        return False
                    assert False

            if check_expect_password is not None:
                actual_password = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, DdnsLocators.password_ddns_input))
                ).get_attribute("value")
                print("实际的密码:" + actual_password)
                print("期望的密码:" + check_expect_password)
                if actual_password != check_expect_password:
                    if repeat_times == 1:
                        print('期望的密码和实际的密码不一致')
                        return False
                    assert False
            if check_expect_status is not None:
                actual_status = driver.find_element_by_xpath(DdnsLocators.status_check).get_attribute('class')
                if 'is-checked' in actual_status:
                    actual_status = "on"
                else:
                    actual_status = "off"
                print("实际的状态:" + actual_status)
                print("期望的状态:" + check_expect_status)
                if actual_status != check_expect_status:
                    if repeat_times == 1:
                        print('期望的状态和实际的状态不一致')
                        return False
                    assert False
            print('检查DDNS成功')
            return True

        except:
            time.sleep(5)
        finally:
            repeat_times -= 1
