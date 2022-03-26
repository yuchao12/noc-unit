import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from common_conf.xpath.wifi_settings import WifiSettingsLocators


def move_to_wifi_settings_page(driver):
    repeat_times = 3
    while repeat_times > 0:
        try:
            driver.find_elements_by_xpath(WifiSettingsLocators.wifi_settings_menus)[1].click()
            driver.find_element_by_xpath(WifiSettingsLocators.wifi_menus).click()
            print('已进入WiFi设置页面')
            print(driver.current_url)
            time.sleep(1)
            if "setting/wifi" in driver.current_url:
                WebDriverWait(driver, 20).until_not(
                    EC.element_to_be_clickable((By.XPATH, "//div[@id='nprogress']"))
                )
                time.sleep(0.5)
                print("当前url", driver.current_url)
                return True
        except:
            driver.refresh()
            time.sleep(2)
        finally:
            repeat_times -= 1
    print("进入wifi设置页面报错")
    assert False


def set_smart_connect(driver,
                      expect_smart_connect,
                      open_expect_ssid=None,
                      open_expect_encryption=None,
                      open_expect_password=None,
                      open_expect_24g_channel_num=None, open_expect_24g_channel_width_num=None,
                      open_expect_5g_channel_num=None, open_expect_5g_channel_width_num=None):
    repeat_times = 3
    while repeat_times > 0:
        move_to_wifi_settings_page(driver)

        print('开始检查')

        # 获取当前双频合一状态

        smart_status_class = driver.find_element_by_xpath(WifiSettingsLocators.smart_button).get_attribute("class")
        print("当前状态", smart_status_class)
        if expect_smart_connect == "on":
            expect_smart_connect_class = 'el-switch is-checked'
            print('期望class', expect_smart_connect_class)
        else:
            expect_smart_connect_class = 'el-switch'
            print('期望class', expect_smart_connect_class)

        try:
            if expect_smart_connect_class != smart_status_class:
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.smart_button))
                ).click()
            print('切换状态')
            time.sleep(1)
            # 双频合一打开时修改所有的配置项
            if expect_smart_connect == "on":
                smart_open_change_wifi(driver, open_expect_ssid, open_expect_encryption,
                                       open_expect_password, open_expect_24g_channel_num,
                                       open_expect_24g_channel_width_num,
                                       open_expect_5g_channel_num, open_expect_5g_channel_width_num)
                return
                # 这里配置打开时的参数
            elif expect_smart_connect == "off":
                smart_close_change_wifi(driver, open_expect_ssid, open_expect_encryption,
                                        open_expect_password, open_expect_24g_channel_num,
                                        open_expect_24g_channel_width_num,
                                        open_expect_5g_channel_num, open_expect_5g_channel_width_num)

                return
                # 这里配置关闭时的参数
            else:
                print("双频合一状态错误")
                assert False
        except:
            pass
        finally:
            repeat_times -= 1


def smart_open_change_wifi(driver, open_expect_ssid=None, open_expect_encryption=None, open_expect_password=None,
                           open_expect_24g_channel_num=None, open_expect_24g_channel_width_num=None,
                           open_expect_5g_channel_num=None, open_expect_5g_channel_width_num=None):
    try:
        # 配置ssid
        if open_expect_ssid is not None:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.ssid_input))
            ).clear()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.ssid_input))
            ).send_keys(open_expect_ssid)

        # 配置加密方式
        if open_expect_encryption is not None:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.encryption_input))
            ).click()
            encryption_xpath = WifiSettingsLocators.select_encryption
            expect_encryption = encryption_xpath.format(num=open_expect_encryption)
            print(expect_encryption)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, expect_encryption))
            ).click()

        # 配置密码
        if open_expect_password is not None:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.password_input))
            ).click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.password_input))
            ).send_keys(open_expect_password)

        # 配置2.4g信道
        if open_expect_24g_channel_num is not None:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.channel_24g))
            ).click()
            channel_xpath = WifiSettingsLocators.select_channel_24g
            expect_channel = channel_xpath.format(num=open_expect_24g_channel_num)
            print(expect_channel)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, expect_channel))
            ).click()

        # 配置2.4g频宽
        if open_expect_24g_channel_width_num is not None:
            # WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.open_24g_channel_width_input))
            # ).click()
            # channel_width_xpath = WifiSettingsLocators.select_24g_channel_width
            # expect_channel_width = channel_width_xpath.format(num=open_expect_24g_channel_width_num)
            # print(expect_channel_width)
            # driver.find_elements_by_xpath(expect_channel_width)[1].click()
            print('2222222222222222')
            driver.find_element_by_xpath(WifiSettingsLocators.channel_width_input_24g).click()
            print('2222222222222')
            channel_width_xpath = WifiSettingsLocators.select_channel_width_24g
            expect_channel_width = channel_width_xpath.format(num=open_expect_24g_channel_width_num)
            print('2.4' + expect_channel_width)
            if open_expect_24g_channel_width_num == "20":
                driver.find_elements_by_xpath(expect_channel_width)[1].click()
            elif open_expect_24g_channel_width_num == "40":
                driver.find_elements_by_xpath(expect_channel_width)[2].click()

        # 配置5g信道
        if open_expect_5g_channel_num is not None:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.channel_5g))
            ).click()
            channel_xpath = WifiSettingsLocators.select_channel_5g
            expect_channel = channel_xpath.format(num=open_expect_5g_channel_num)
            driver.find_elements_by_xpath(expect_channel)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, expect_channel))
            ).click()

        # 配置5g频宽
        if open_expect_5g_channel_width_num is not None:
            # WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.open_24g_channel_width_input))
            # ).click()
            # channel_width_xpath = WifiSettingsLocators.select_5g_channel_width
            # expect_channel_width = channel_width_xpath.format(num=open_expect_5g_channel_width_num)
            # driver.find_elements_by_xpath(expect_channel_width)[1].click()
            time.sleep(0.5)
            driver.find_element_by_xpath(WifiSettingsLocators.channel_width_input_5g).click()
            print('3333')
            channel_width_xpath = WifiSettingsLocators.select_channel_width_5g
            expect_channel_width = channel_width_xpath.format(num=open_expect_5g_channel_width_num)
            print('5' + expect_channel_width)
            if open_expect_5g_channel_width_num == "20":
                print(20)
                driver.find_elements_by_xpath(expect_channel_width)[1].click()
            elif open_expect_5g_channel_width_num == "40":
                print(40)
                driver.find_elements_by_xpath(expect_channel_width)[2].click()
            elif open_expect_5g_channel_width_num == "80":
                print(80)
                driver.find_element_by_xpath(expect_channel_width).click()
                print(111111)

        # 保存按钮
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.save_button))
        ).click()
    except:
        print('WiFi设置失败')
        assert False


def smart_close_change_wifi(driver, expect_ssid=None, expect_encryption=None, expect_password=None,
                            expect_24g_channel_num=None, expect_24g_channel_width_num=None,
                            expect_5g_channel_num=None, expect_5g_channel_width_num=None):
    try:
        # 配置ssid
        if expect_ssid is not None:
            driver.find_elements_by_xpath(WifiSettingsLocators.ssid_input)[0].clear()
            driver.find_elements_by_xpath(WifiSettingsLocators.ssid_input)[0].send_keys(expect_ssid)
            driver.find_elements_by_xpath(WifiSettingsLocators.ssid_input)[1].clear()
            driver.find_elements_by_xpath(WifiSettingsLocators.ssid_input)[1].send_keys(expect_ssid + "-5g")

        # 配置加密方式
        if expect_encryption is not None:
            driver.find_elements_by_xpath(WifiSettingsLocators.encryption_input)[0].click()
            encryption_xpath = WifiSettingsLocators.select_encryption
            expect_encryption = encryption_xpath.format(num=expect_encryption)
            print(expect_encryption)

            driver.find_elements_by_xpath(expect_encryption)[1].click()
            driver.find_elements_by_xpath(WifiSettingsLocators.encryption_input)[1].click()
            driver.find_elements_by_xpath(expect_encryption)[1].click()
            print('加密方式结束')

        # 配置密码
        if expect_password is not None:
            print(expect_password)
            driver.find_elements_by_xpath(WifiSettingsLocators.password_input)[0].click()
            driver.find_elements_by_xpath(WifiSettingsLocators.password_input)[0].send_keys(expect_password)
            driver.find_elements_by_xpath(WifiSettingsLocators.password_input)[1].click()
            driver.find_elements_by_xpath(WifiSettingsLocators.password_input)[1].send_keys(expect_password)
            print('配置密码完成')

        # 配置信道
        if expect_24g_channel_num is not None:
            driver.find_elements_by_xpath(WifiSettingsLocators.channel_24g)[0].click()
            channel_xpath = WifiSettingsLocators.select_channel_24g
            expect_channel = channel_xpath.format(num=expect_24g_channel_num)
            print(expect_channel)
            driver.find_elements_by_xpath(expect_channel)[0].click()
            time.sleep(1)
            channel_xpath = WifiSettingsLocators.select_channel_24g
            expect_channel_5 = channel_xpath.format(num=expect_5g_channel_num)
            print(expect_channel_5)
            driver.find_elements_by_xpath(WifiSettingsLocators.channel_24g)[1].click()
            print('23232323')
            driver.find_elements_by_xpath(expect_channel_5)[0].click()
            print('配置信道完成')

        # 配置频宽
        if expect_24g_channel_width_num is not None:
            driver.find_elements_by_xpath(WifiSettingsLocators.channel_width_input_24g)[0].click()
            channel_width_xpath = WifiSettingsLocators.select_channel_width_24g
            expect_channel_width = channel_width_xpath.format(num=expect_24g_channel_width_num)
            print('2.4' + expect_channel_width)
            if expect_24g_channel_width_num == "20":
                driver.find_elements_by_xpath(expect_channel_width)[1].click()
            elif expect_24g_channel_width_num == "40":
                driver.find_elements_by_xpath(expect_channel_width)[2].click()
            print('设置5g频宽')
            channel_width_xpath = WifiSettingsLocators.select_channel_width_5g
            expect_channel_width = channel_width_xpath.format(num=expect_5g_channel_width_num)
            print("5g" + expect_channel_width)
            time.sleep(0.5)
            driver.find_elements_by_xpath(WifiSettingsLocators.channel_width_input_24g)[1].click()
            if expect_5g_channel_width_num == "20":
                print(20)
                driver.find_elements_by_xpath(expect_channel_width)[1].click()
            elif expect_5g_channel_width_num == "40":
                print(40)
                driver.find_elements_by_xpath(expect_channel_width)[2].click()
            elif expect_5g_channel_width_num == "80":
                print(80)
                driver.find_element_by_xpath(expect_channel_width).click()
                print(111111)
        # 保存按钮
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.save_button))
        ).click()
    except:
        print('wifi设置失败')
        assert False


def check_wifi_settings(driver, expect_smart_connect=None, expect_ssid=None, expect_encryption=None,
                        expect_24g_channel_num=None, expect_24g_channel_width_num=None,
                        expect_5g_channel_num=None, expect_5g_channel_width_num=None, repeat_times=6):
    while repeat_times > 0:
        driver.refresh()
        print("这是倒数第%d次" % repeat_times)
        move_to_wifi_settings_page(driver)
        try:
            smart_status_class = driver.find_element_by_xpath(WifiSettingsLocators.smart_button).get_attribute("class")
            print("当前状态", smart_status_class)

            if expect_smart_connect == "on":
                expect_smart_connect_class = 'el-switch is-checked'
                print('期望class', expect_smart_connect_class)
            else:
                expect_smart_connect_class = 'el-switch'
                print('期望class', expect_smart_connect_class)

            # 检查双频合一状态
            if expect_smart_connect is not None:
                if smart_status_class != expect_smart_connect_class:
                    if repeat_times == 1:
                        print("【备注】期望状态为：%s，实际状态为：%s ！！！" % (expect_smart_connect_class, smart_status_class))
                        return False
                    assert False

            # 双频合一状态开启时验证
            if expect_smart_connect == "on":
                # 检查SSID
                if expect_ssid is not None:
                    print('1111111111111')
                    ssid = driver.find_element_by_xpath(WifiSettingsLocators.ssid_input).get_attribute("value")
                    print(ssid)
                    if ssid != expect_ssid:
                        if repeat_times == 1:
                            print("【备注】期望ssid为：%s，实际ssid为：%s ！！！" % (expect_ssid, ssid))
                            return False
                        assert False

                # 检查加密方式
                if expect_encryption is not None:
                    encryption = driver.find_element_by_xpath(WifiSettingsLocators.encryption_input).get_attribute(
                        "value")
                    print(encryption)
                    if encryption != expect_encryption:
                        if repeat_times == 1:
                            print("【备注】期望加密方式为：%s，实际加密方式为：%s ！！！" % (expect_encryption, encryption))
                            return False
                        assert False

                # 检查2.4g信道
                if expect_encryption is not None:
                    channel_24g = driver.find_element_by_xpath(WifiSettingsLocators.channel_24g).get_attribute(
                        "value")
                    print(channel_24g)
                    if channel_24g != expect_24g_channel_num:
                        if repeat_times == 1:
                            print("【备注】期望2.4g信道为：%s，实际2.4g信道为：%s ！！！" % (expect_24g_channel_num, channel_24g))
                            return False
                        assert False

                # 检查2.4g频宽
                if expect_encryption is not None:
                    channel_width_24g = driver.find_element_by_xpath(
                        WifiSettingsLocators.channel_width_input_24g).get_attribute(
                        "value")
                    print(channel_width_24g)
                    if channel_width_24g != expect_24g_channel_width_num:
                        if repeat_times == 1:
                            print(
                                "【备注】期望2.4g频宽为：%s，实际2.4g频宽为：%s ！！！" % (expect_24g_channel_width_num, channel_width_24g))
                            return False
                        assert False

                # 检查5g信道
                if expect_encryption is not None:
                    channel_5g = driver.find_element_by_xpath(WifiSettingsLocators.channel_5g).get_attribute(
                        "value")
                    print(channel_5g)
                    if channel_5g != expect_5g_channel_num:
                        if repeat_times == 1:
                            print("【备注】期望5g信道为：%s，实际5g信道为：%s ！！！" % (expect_5g_channel_num, channel_5g))
                            return False
                        assert False

                # 检查5g频宽
                if expect_encryption is not None:
                    channel_width_5g = driver.find_element_by_xpath(
                        WifiSettingsLocators.channel_width_input_5g).get_attribute(
                        "value")
                    print(channel_width_5g)
                    if channel_width_5g != expect_5g_channel_width_num:
                        if repeat_times == 1:
                            print("【备注】期望5g频宽为：%s，实际5g频宽为：%s ！！！" % (expect_24g_channel_width_num, channel_width_5g))
                            return False
                        assert False


            #双频合一关闭的情况
            if expect_smart_connect == "off":
                # 检查2.4gSSID
                if expect_ssid is not None:
                    print(232323)
                    ssid_24g = driver.find_elements_by_xpath(WifiSettingsLocators.ssid_input)[0].get_attribute("value")
                    print(ssid_24g)
                    if ssid_24g != expect_ssid:
                        if repeat_times == 1:
                            print("【备注】期望2.4gssid为：%s，实际2.4gssid为：%s ！！！" % (expect_ssid, ssid_24g))
                            return False
                        assert False
                # 检查5gSSID
                if expect_ssid is not None:
                    ssid_5g = driver.find_elements_by_xpath(WifiSettingsLocators.ssid_input)[1].get_attribute("value")
                    print(ssid_5g)
                    if ssid_5g != expect_ssid + "_5g":
                        if repeat_times == 1:
                            print("【备注】期望5gssid为：%s，实际5gssid为：%s ！！！" % (expect_ssid + "_5g", ssid_5g))
                            return False
                        assert False

                # 检查2.4g加密方式
                if expect_encryption is not None:
                    encryption_24g = driver.find_elements_by_xpath(WifiSettingsLocators.encryption_input)[
                        0].get_attribute(
                        "value")
                    print(encryption_24g)
                    if encryption_24g != expect_encryption:
                        if repeat_times == 1:
                            print("【备注】期望2.4g加密方式为：%s，实际2.4g加密方式为：%s ！！！" % (expect_encryption, encryption_24g))
                            return False
                        assert False

                # 检查5g加密方式
                if expect_encryption is not None:
                    encryption_5g = driver.find_elements_by_xpath(WifiSettingsLocators.encryption_input)[
                        1].get_attribute(
                        "value")
                    print(encryption_5g)
                    if encryption_5g != expect_encryption:
                        if repeat_times == 1:
                            print("【备注】期望5g加密方式为：%s，实际5g加密方式为：%s ！！！" % (expect_encryption, encryption_5g))
                            return False
                        assert False

                # 检查2.4g信道
                if expect_encryption is not None:
                    channel_24g = driver.find_elements_by_xpath(WifiSettingsLocators.channel_24g)[0].get_attribute(
                        "value")
                    print(channel_24g)
                    if channel_24g != expect_24g_channel_num:
                        if repeat_times == 1:
                            print("【备注】期望2.4g信道为：%s，实际2.4g信道为：%s ！！！" % (expect_24g_channel_num, channel_24g))
                            return False
                        assert False

                # 检查5g信道
                if expect_encryption is not None:
                    channel_5g = driver.find_elements_by_xpath(WifiSettingsLocators.channel_24g)[1].get_attribute(
                        "value")
                    print(channel_5g)
                    if channel_5g != expect_5g_channel_num:
                        if repeat_times == 1:
                            print("【备注】期望5g信道为：%s，实际5g信道为：%s ！！！" % (expect_5g_channel_num, channel_5g))
                            return False
                        assert False

                # 检查2.4g频宽
                if expect_encryption is not None:
                    channel_width_24g = driver.find_elements_by_xpath(
                        WifiSettingsLocators.channel_width_input_24g)[0].get_attribute(
                        "value")
                    print(channel_width_24g)
                    if channel_width_24g != expect_24g_channel_width_num:
                        if repeat_times == 1:
                            print(
                                "【备注】期望2.4g频宽为：%s，实际2.4g频宽为：%s ！！！" % (expect_24g_channel_width_num, channel_width_24g))
                            return False
                        assert False


                # 检查5g频宽
                if expect_encryption is not None:
                    channel_width_5g = driver.find_elements_by_xpath(
                        WifiSettingsLocators.channel_width_input_24g)[1].get_attribute(
                        "value")
                    print(channel_width_5g)
                    if channel_width_5g != expect_5g_channel_width_num:
                        if repeat_times == 1:
                            print(
                                "【备注】期望2.4g频宽为：%s，实际2.4g频宽为：%s ！！！" % (expect_5g_channel_width_num, channel_width_5g))
                            return False
                        assert False

            print('测试通过')
            return True

        except:
            time.sleep(5)
        finally:
            repeat_times -= 1
