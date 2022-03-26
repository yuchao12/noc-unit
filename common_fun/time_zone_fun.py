import time

from selenium.webdriver import ActionChains

from common_conf.xpath.time_zone import TimeLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def move_to_time_zone_page(driver):
    repeat_times = 3
    while repeat_times > 0:
        print(f'这是进入时区页倒数第{repeat_times}次')
        try:
            # 判断当前页面是否为时区页
            if "setting/timezone" in driver.current_url:
                print('刷新')
                driver.refresh()
            else:
                # 鼠标移动到其他设置
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(TimeLocators.other_setting_menu)).perform()
                time.sleep(0.5)
                # 鼠标移动到国家及地区菜单
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(TimeLocators.time_zone_menu)).perform()
                # 点击国家及地区菜单
                driver.find_element_by_xpath(TimeLocators.time_zone_menu).click()
                time.sleep(0.5)
            # 等待进度条加载完成
            WebDriverWait(driver, 20).until_not(
                EC.element_to_be_clickable((By.XPATH, TimeLocators.loading))
            )
            time.sleep(0.5)
            print('进入时区页面成功')
            return True
        except:
            time.sleep(2)
        finally:
            repeat_times -= 1
    print("进入时区页面报错")
    assert False


def change_time_zone(driver, expect_timezone_country=None):
    repeat_times = 3
    while repeat_times > 0:
        print(f"这是修改时区倒数第{repeat_times}次")
        move_to_time_zone_page(driver)
        try:
            if expect_timezone_country is not None:
                # 点击出时区下拉框
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, TimeLocators.time_zone_input))
                ).click()
                # 选择时区
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, TimeLocators.select_timezone_coutry.format(expect_timezone_country)))
                ).click()
                # 点击保存按钮
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, TimeLocators.save_button))).click()
                print('修改时区完成')
                return
        except:
            pass
        finally:
            repeat_times -= 1


def check_time_zone(driver, check_expect_timezone_country=None, repeat_times=3):
    while repeat_times > 0:
        print(f"这是检查时区倒数第{repeat_times}次")
        move_to_time_zone_page(driver)
        try:
            if check_expect_timezone_country is not None:
                time.sleep(2)
                print("点击出下拉框")
                # 点击出时区下拉框
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, TimeLocators.time_zone_input))
                ).click()
                # 获取当前被选中的国家
                timezone_country = driver.find_element_by_xpath(
                    TimeLocators.selected_timezone_country).get_attribute("title")
                print("实际的时区城市：" + timezone_country)
                print("期望的时区城市：" + check_expect_timezone_country)
                if check_expect_timezone_country != timezone_country:
                    if repeat_times == 1:
                        print("检查时区失败")
                        return False
                    assert False
            print("检查时区成功")
            return True
        except:
            time.sleep(5)
        finally:
            repeat_times -= 1
    print('检查时区失败')
    assert False
