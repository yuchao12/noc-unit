import time
from common_conf.xpath.upnp import UpnpLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def move_to_upnp_page(driver):
    repeat_times = 3
    while repeat_times > 0:
        print(f'这是进入UPnp页倒数第{repeat_times}次')
        try:
            # 判断当前页面是否为UPnp页
            if "setting/upnp" in driver.current_url:
                print('刷新')
                driver.refresh()
            else:
                # 鼠标移动到高级设置
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(UpnpLocators.advanced_settings_menu)).perform()
                time.sleep(0.5)
                # 鼠标移动到UPnp菜单
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(UpnpLocators.upnp_menu)).perform()
                # 点击UPnp菜单
                driver.find_element_by_xpath(UpnpLocators.upnp_menu).click()
                time.sleep(0.5)
            # 等待进度条加载完成
            WebDriverWait(driver, 20).until_not(
                EC.element_to_be_clickable((By.XPATH, UpnpLocators.loading))
            )
            time.sleep(0.5)
            print('进入upnp页面成功')
            return True
        except:
            driver.refresh()
            time.sleep(2)
        finally:
            repeat_times -= 1
    print("进入upnp页面报错")
    assert False


def change_upnp(driver, expect_status=None):
    repeat_times = 3
    while repeat_times > 0:
        print(f"这是修改upnp倒数第{repeat_times}次")
        move_to_upnp_page(driver)
        try:
            if expect_status is not None:
                print('获取状态')
                # 获取当前是否开启状态
                actual_status = driver.find_element_by_xpath(UpnpLocators.status_checkbox).get_attribute('class')
                print(actual_status)
                if 'is-checked' in actual_status:
                    actual_status = "on"
                else:
                    actual_status = "off"
                print(actual_status)
                if expect_status != actual_status:
                    # 点击开启的复选框
                    WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, UpnpLocators.status_checkbox))
                    ).click()
                    print('点击复选框完成')
                # 最后保存
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, UpnpLocators.save_button))
            ).click()
            print("修改upnp成功")
            return

        except:
            time.sleep(60)
        finally:
            repeat_times -= 1
        print("修改upnp失败")
        assert False


def check_upnp(driver, repeat_times=3, check_expect_status=None):
    while repeat_times > 0:
        print(f"这是检查dmz倒数第{repeat_times}次")
        move_to_upnp_page(driver)
        try:
            if check_expect_status is not None:
                actual_status = driver.find_element_by_xpath(UpnpLocators.status_checkbox).get_attribute('class')
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
            print('检查upnp成功')
            return True
        except:
            time.sleep(5)
        finally:
            repeat_times -= 1
