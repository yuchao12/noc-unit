import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common_fun import user_public_fun
from common_conf.xpath.guest_wifi import GuestWifiLocators
from selenium.webdriver import ActionChains


def move_to_guest_wifi_page(driver):
    repeat_times = 3
    while repeat_times > 0:
        print(f'这是进入Guest Wi-Fi页倒数第{repeat_times}次')
        try:
            # 判断当前页面是否为guest_wifi页
            if "setting/diagnosis" in driver.current_url:
                print('刷新')
                driver.refresh()
            else:
                # 鼠标移动到wifi设置
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(GuestWifiLocators.wifi_settings_menu)).perform()
                time.sleep(0.5)
                # 鼠标移动到guest_wifi菜单
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(GuestWifiLocators.guest_wifi_menu)).perform()
                # 点击guest_wifi菜单
                driver.find_element_by_xpath(GuestWifiLocators.guest_wifi_menu).click()
                time.sleep(0.5)
            # 等待进度条加载完成
            WebDriverWait(driver, 20).until_not(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.loading))
            )
            time.sleep(0.5)
            print('进入guest_wifi页面成功')
            return True
        except:
            driver.refresh()
            time.sleep(2)
        finally:
            repeat_times -= 1
    print("进入guest_wifi页面报错")
    assert False


def change_guest_wifi(driver, expect_wifi_opened_status=None, expect_duration=None, expect_ssid=None,
                      expect_encryption=None, expect_password=None, expect_smart_connect_status=None):
    repeat_times = 3
    while repeat_times > 0:
        move_to_guest_wifi_page(driver)
        try:
            # 获取当前访客wifi是否被开启的状态
            actual_wifi_opened_status = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.wifi_opened_button))).get_attribute("class")
            print('实际wifi',actual_wifi_opened_status)
            if actual_wifi_opened_status == 'el-switch is-checked':
                actual_wifi_opened_status = 'on'
                print('实际wifi', actual_wifi_opened_status)
            else:
                actual_wifi_opened_status = 'off'
                print('实际wifi', actual_wifi_opened_status)
            print("修改WiFi开启状态")
            if expect_wifi_opened_status is not None:
                # 判断状态，如果状态相同就不用改变，如果不相同就点击按钮
                if expect_wifi_opened_status != actual_wifi_opened_status:
                    WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.wifi_opened_button))).click()

            print("修改有效时间")
            if expect_duration is not None:
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.duration_input))).click()
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, GuestWifiLocators.duration_select.format(expect_duration)))).click()
            print("修改ssid")
            if expect_ssid is not None:
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.ssid_input))).clear()
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.ssid_input))).send_keys(expect_ssid)
            print('修改加密方式')
            if expect_encryption is not None:
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.encryption_input))).click()
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, GuestWifiLocators.encryption_select.format(expect_encryption)))).click()
            print('修改密码')
            if expect_password is not None:
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.password_input))).clear()
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.password_input))).send_keys(expect_password)

            print('修改双频合一状态')
            if expect_smart_connect_status is not None:
                actual_smart_connect_status = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.smart_connect_button))).get_attribute("class")
                print('实际smart',actual_smart_connect_status)
                if actual_smart_connect_status == 'el-switch is-checked':
                    actual_smart_connect_status = 'on'
                    print('实际smart', actual_smart_connect_status)
                else:
                    actual_smart_connect_status = 'off'
                    print('实际smart', actual_smart_connect_status)
                # 判断状态，如果状态相同就不用改变，如果不相同就点击按钮
                if expect_smart_connect_status != actual_smart_connect_status:
                    WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.smart_connect_button))).click()
            print("修改Guest Wifi成功")
            return
        except:
            time.sleep(30)
        finally:
            repeat_times-=1
    print("修改Guest Wifi失败")
    assert False

