import time
from common_conf.xpath.dmz import DmzLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def move_to_dmz_page(driver):
    repeat_times = 3
    while repeat_times > 0:
        print(f'这是进入DMZ页倒数第{repeat_times}次')
        try:
            # 判断当前页面是否为DMZ页
            if "setting/dmz" in driver.current_url:
                print('刷新')
                driver.refresh()
            else:
                # 鼠标移动到高级设置
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(DmzLocators.advanced_settings_menu)).perform()
                time.sleep(0.5)
                # 鼠标移动到DMZ菜单
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(DmzLocators.dmz_menu)).perform()
                # 点击DMZ菜单
                driver.find_element_by_xpath(DmzLocators.dmz_menu).click()
                time.sleep(0.5)
            # 等待进度条加载完成
            WebDriverWait(driver, 20).until_not(
                EC.element_to_be_clickable((By.XPATH, DmzLocators.loading))
            )
            time.sleep(0.5)
            print('进入dmz页面成功')
            return True
        except:
            driver.refresh()
            time.sleep(2)
        finally:
            repeat_times -= 1
    print("进入dmz页面报错")
    assert False


def change_dmz(driver, expect_dmz_host=None, expect_status=None):
    repeat_times = 3
    while repeat_times > 0:
        print(f"这是修改dmz倒数第{repeat_times}次")
        move_to_dmz_page(driver)
        try:
            if expect_dmz_host is not None:

                # 清空dmz主机的内容
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, DmzLocators.dmz_input))
                ).clear()
                # 输入DMZ主机号
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, DmzLocators.dmz_input))).send_keys(
                    expect_dmz_host)
                print('主机号完成')
            if expect_status is not None:
                print('获取状态')
                # 获取当前是否开启状态
                actual_status = driver.find_element_by_xpath(DmzLocators.status_checkbox).get_attribute('class')
                print(actual_status)
                if 'is-checked' in actual_status:
                    actual_status = "on"
                else:
                    actual_status = "off"
                print(actual_status)
                if expect_status != actual_status:
                    # 点击开启的复选框
                    WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, DmzLocators.status_checkbox))
                    ).click()
                    print('点击复选框完成')
                # 最后保存
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, DmzLocators.save_button))
            ).click()
            print("修改dmz成功")
            return

        except:
            time.sleep(60)
        finally:
            repeat_times -= 1
        print("修改dmz失败")
        assert False


def check_dmz(driver, repeat_times=3, check_expect_dmz_host=None, check_expect_status=None):
    while repeat_times > 0:
        print(f"这是检查dmz倒数第{repeat_times}次")
        move_to_dmz_page(driver)
        try:
            if check_expect_dmz_host is not None:
                # 获取dmz主机的值
                actual_dmz_host = driver.find_element_by_xpath(
                    DmzLocators.dmz_input).get_attribute(
                    "value")
                print("实际的dmz主机：" + actual_dmz_host)
                print("期望的dmz主机：" + check_expect_dmz_host)
                if actual_dmz_host != check_expect_dmz_host:
                    if repeat_times == 1:
                        print('期望的dmz主机和实际的dmz主机不一致')
                        return False
                    assert False
            if check_expect_status is not None:
                actual_status = driver.find_element_by_xpath(DmzLocators.status_checkbox).get_attribute('class')
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
            print('检查dmz成功')
            return True
        except:
            time.sleep(5)
        finally:
            repeat_times -= 1
