import time
from common_conf.xpath.network_diagnosis import NetworkDiagnosisLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common_fun import user_public_fun


def move_to_network_diagnosis_page(driver):
    repeat_times = 3
    while repeat_times > 0:
        print(f'这是进入Network Diagnosis页倒数第{repeat_times}次')
        try:
            # 判断当前页面是否为Network Diagnosis页
            if "setting/diagnosis" in driver.current_url:
                print('刷新')
                driver.refresh()
            else:
                # 鼠标移动到高级设置
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(NetworkDiagnosisLocators.advanced_settings_menu)).perform()
                time.sleep(0.5)
                # 鼠标移动到Network Diagnosis菜单
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(NetworkDiagnosisLocators.network_diagnosis_menu)).perform()
                # 点击Network Diagnosis菜单
                driver.find_element_by_xpath(NetworkDiagnosisLocators.network_diagnosis_menu).click()
                time.sleep(0.5)
            # 等待进度条加载完成
            WebDriverWait(driver, 20).until_not(
                EC.element_to_be_clickable((By.XPATH, NetworkDiagnosisLocators.loading))
            )
            time.sleep(0.5)
            print('进入network_diagnosis页面成功')
            return True
        except:
            driver.refresh()
            time.sleep(2)
        finally:
            repeat_times -= 1
    print("进入network_diagnosis页面报错")
    assert False


def change_network_diagnosis(driver, expect_tool=None, expect_addres=None):
    repeat_times = 3
    while repeat_times > 0:
        print(f"这是网络分析倒数第{repeat_times}次")
        move_to_network_diagnosis_page(driver)
        try:
            if expect_tool is not None:
                # 点击工具输入框
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, NetworkDiagnosisLocators.tool_input))
                ).click()
                # 选择工具模式
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, NetworkDiagnosisLocators.tool_select.format(expect_tool)))).click()

            if expect_addres is not None:
                # 输入地址
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, NetworkDiagnosisLocators.address_input))
                ).send_keys(expect_addres)

            # 最后保存
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, NetworkDiagnosisLocators.save_button))
            ).click()
            print("修改network_diagnosis成功")
            return
        except:
            time.sleep(60)
        finally:
            repeat_times -= 1
        print("修改network_diagnosis失败")
        assert False


def check_network_diagnosis(driver, expect_tool, repeat_times=2):
    while repeat_times > 0:
        print(f"这是检查network_diagnosis倒数第{repeat_times}次")
        # 移动到消息中心页
        operation_type, message_status = user_public_fun.move_to_message_center(driver, 'View')
        try:
            if operation_type != expect_tool:
                if repeat_times == 1:
                    print('检查操作类型失败')
                    return False
                assert False
            if message_status == 'Succeeded':
                print('检查状态成功')
            else:
                if repeat_times == 1:
                    print('检查状态失败')
                    return False
                assert False
            result_text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, NetworkDiagnosisLocators.result_text))
            ).text

            if expect_tool == "ping":
                if 'rtt min/avg/max/mdev' in result_text:
                    print('ping检查结果成功')
                else:
                    if repeat_times == 1:
                        print('ping检查结果失败')
                        return False
                    assert False

            elif expect_tool == 'nslookup':
                if 'Addresses' in result_text:
                    print('nslookup检查结果成功')
                else:
                    if repeat_times == 1:
                        print('nslookup检查结果失败')
                        return False
                    assert False

            elif expect_tool == 'traceroute':
                if '1  10.70.0.1 (10.70.0.1)' in result_text:
                    print('traceroute检查结果成功')
                else:
                    if repeat_times == 1:
                        print('traceroute检查结果失败')
                        return False
                    assert False
            return True
        except:
            time.sleep(5)
        finally:
            repeat_times -= 1
