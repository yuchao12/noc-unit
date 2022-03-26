#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:  yuchao


import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from common_conf.xpath.dhcp import DhcpLocators


def move_to_dhcp_page(driver):
    repeat_times = 3
    while repeat_times > 0:
        print(f'这是{repeat_times}次进入')
        try:
            # driver.refresh()
            # driver.find_elements_by_xpath('//h3[@class="menus-parent__title"]')[2].click()
            # driver.find_element_by_xpath("//span[text()='DHCP']").click()
            # print('11111111111111111111111111111111111111111')
            # time.sleep(1)
            # if "setting/dhcp" in driver.current_url:
            #     WebDriverWait(driver, 20).until_not(
            #         EC.element_to_be_clickable((By.XPATH, "//div[@id='nprogress']"))
            #     )
            #     time.sleep(0.5)
            #     return True
            if "setting/dhcp" in driver.current_url:
                driver.refresh()
            else:
                driver.find_elements_by_xpath('//h3[@class="menus-parent__title"]')[2].click()
                driver.find_element_by_xpath("//span[text()='DHCP']").click()
                print('11111111111111111111111111111111111111111')
                time.sleep(1)
            WebDriverWait(driver, 20).until_not(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='nprogress']"))
            )
            time.sleep(0.5)
            return True
        except:
            time.sleep(2)
        finally:
            repeat_times -= 1
    print("进入DHCP页面报错")
    assert False


def change_dhcp(driver, except_lan_ip=None, except_start_ip=None, except_end_ip=None, except_lease_time=None):
    repeat_times = 3
    while repeat_times > 0:
        move_to_dhcp_page(driver)
        # driver.refresh()
        try:
            # 设置lan ip
            if except_lan_ip is not None:
                driver.find_element_by_xpath(DhcpLocators.lan_ip).clear()
                driver.find_element_by_xpath(DhcpLocators.lan_ip).send_keys(except_lan_ip)
            # 设置开始ip
            if except_start_ip is not None:
                driver.find_element_by_xpath(DhcpLocators.start_ip).clear()
                driver.find_element_by_xpath(DhcpLocators.start_ip).send_keys(except_start_ip)
            # 设置结束ip
            if except_end_ip is not None:
                driver.find_element_by_xpath(DhcpLocators.end_ip).clear()
                driver.find_element_by_xpath(DhcpLocators.end_ip).send_keys(except_end_ip)
            # 设置租赁时间
            if except_lease_time is not None:
                lease_time = DhcpLocators.lease_time_all.format(text=except_lease_time)
                driver.find_element_by_xpath(DhcpLocators.lease_time).click()
                driver.find_element_by_xpath(lease_time).click()
            # 保存
            driver.find_element_by_xpath(DhcpLocators.save).click()
            return
        except:
            pass
        finally:
            repeat_times -= 1
    print("修改DHCP失败")
    assert False


def check_dhcp(driver, except_lan_ip=None, except_start_ip=None, except_end_ip=None, except_lease_time=None,
               repeat_times=3):

    while repeat_times > 0:
        print("这是第%d次" % repeat_times)
        move_to_dhcp_page(driver)
        # driver.refresh()
        try:
            # 检查lan ip
            if except_lan_ip is not None:
                actual_lan_ip = driver.find_element_by_xpath(DhcpLocators.lan_ip).get_attribute("value")
                if actual_lan_ip != except_lan_ip:
                    if repeat_times == 1:
                        print("【备注】期望lan ip为：%s，实际lan ip为：%s ！！！" % (except_lan_ip, actual_lan_ip))
                        return False
                    assert False

            # 检查开始ip
            if except_start_ip is not None:
                actual_start_ip = driver.find_element_by_xpath(DhcpLocators.start_ip).get_attribute("value")
                if actual_start_ip != except_start_ip:
                    if repeat_times == 1:
                        print("【备注】期望开始ip为：%s，实际开始ip为：%s ！！！" % (except_start_ip, actual_start_ip))
                        return False
                    assert False

            # 检查结束ip
            if except_end_ip is not None:
                actual_end_ip = driver.find_element_by_xpath(DhcpLocators.end_ip).get_attribute("value")
                if actual_end_ip != except_end_ip:
                    if repeat_times == 1:
                        print("【备注】期望开始ip为：%s，实际开始ip为：%s ！！！" % (except_end_ip, actual_end_ip))
                        return False
                    assert False

            # 检查租赁时间
            if except_lease_time is not None:
                # 找到当前选中租赁时间的xpath
                actual_lease_time = DhcpLocators.lease_time_all.format(
                    text=except_lease_time) + "/../../li[contains(@class,'selected')]/span"
                driver.find_element_by_xpath(DhcpLocators.lease_time).click()
                WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, actual_lease_time))
                )
                actual_lease_time = driver.find_element_by_xpath(actual_lease_time).text
                if actual_lease_time != except_lease_time:
                    if repeat_times == 1:
                        print("【备注】期望租赁时间为：%s，实际租赁时间为：%s ！！！" % (except_lease_time, actual_lease_time))
                        return False
                    assert False

            return True

        except:
            time.sleep(5)
        finally:
            repeat_times -= 1
    print("检查DHCP失败")
    assert False
