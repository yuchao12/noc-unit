#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from ..common_conf.xpath.network_mode import NetworkSettingsLocators


def move_to_network_settings_page(driver):
    repeat_times = 3
    while repeat_times > 0:
        try:
            print('进入设备详情页面')
            driver.find_elements_by_xpath('//h3[@class="menus-parent__title"]')[2].click()
            driver.find_element_by_xpath("//span[text()='Network Mode']").click()
            time.sleep(1)
            if "setting/mode" in driver.current_url:
                WebDriverWait(driver, 20).until_not(
                    EC.element_to_be_clickable((By.XPATH, "//div[@id='nprogress']"))
                )
                time.sleep(0.5)
                return True
        except:
            driver.refresh()
            time.sleep(2)
        finally:
            repeat_times -= 1
    print("进入工作模式页面报错")
    assert False


def change_network_settings(driver, except_mode):
    repeat_times = 3
    while repeat_times > 0:
        move_to_network_settings_page(driver)
        try:
            except_mode_option = NetworkSettingsLocators.mode.format(mode=except_mode)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, except_mode_option))
            ).click()
            # 保存
            driver.find_element_by_xpath(NetworkSettingsLocators.save).click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, NetworkSettingsLocators.save_ok))
            ).click()

            return
        except:
            pass
        finally:
            repeat_times -= 1
    print("修改工作模式失败")
    assert False


def check_network_settings(driver, except_mode, repeat_times=3):
    move_to_network_settings_page(driver)
    while repeat_times > 0:
        driver.refresh()
        print("这是第%d次\n" % repeat_times)
        try:
            actual_mode_xpath = NetworkSettingsLocators.mode.format(
                mode=except_mode) + "/../../../label[contains(@class,'checked')]/span[2]"
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, actual_mode_xpath))
            )
            actual_mode = driver.find_element_by_xpath(actual_mode_xpath).text
            if actual_mode != except_mode:
                if repeat_times == 1:
                    print("【备注】期望工作模式为：%s，实际工作模式为：%s ！！！" % (except_mode, actual_mode))
                    return False
                assert False
        except:
            time.sleep(5)
        finally:
            repeat_times -= 1
    print("检查工作模式失败")
    assert False
