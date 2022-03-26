import time
from common_conf.xpath.static_dhcp_lease import StaticDhcpLeaseLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common_fun import user_public_fun


def move_to_static_dhcp_lease_page(driver):
    repeat_times = 3
    while repeat_times > 0:
        print(f'这是进入mac绑定ip页倒数第{repeat_times}次')
        try:
            # 判断当前页面是否为Static DHCP Lease页
            if "setting/rsvdip" in driver.current_url:
                print('刷新')
                driver.refresh()
            else:
                # 鼠标移动到高级设置
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(StaticDhcpLeaseLocators.advanced_settings_menu)).perform()
                time.sleep(0.5)
                # 鼠标移动到Static DHCP Lease菜单
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(StaticDhcpLeaseLocators.sdl_menu)).perform()
                # 点击Static DHCP Lease菜单
                driver.find_element_by_xpath(StaticDhcpLeaseLocators.sdl_menu).click()
                time.sleep(0.5)
            # 等待进度条加载完成
            WebDriverWait(driver, 20).until_not(
                EC.element_to_be_clickable((By.XPATH, StaticDhcpLeaseLocators.loading))
            )
            time.sleep(0.5)
            print('进入mac绑定ip页面成功')
            return True
        except:
            driver.refresh()
            time.sleep(2)
        finally:
            repeat_times -= 1
    print("进入mac绑定ip页面报错")
    assert False


def add_static_dhcp_lease(driver, expect_name, expect_mac, expect_ip):
    repeat_times = 3
    while repeat_times > 0:
        print(f"这是添加mac绑定ip倒数第{repeat_times}次")
        move_to_static_dhcp_lease_page(driver)
        try:
            # print('点击add按钮')
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, StaticDhcpLeaseLocators.add_button))
            ).click()
            # print('输入name')
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, StaticDhcpLeaseLocators.name_input))).send_keys(expect_name)
            # print('输入mac')
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, StaticDhcpLeaseLocators.mac_input))
            ).send_keys(expect_mac)
            # print('输入ip')
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, StaticDhcpLeaseLocators.ip_input))
            ).send_keys(expect_ip)
            # print('最后保存')
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, StaticDhcpLeaseLocators.save_button))
            ).click()
            print("添加mac绑定ip成功")
            return
        except:
            time.sleep(30)
        finally:
            repeat_times -= 1
        print("添加mac绑定ip失败")
        assert False


def edit_static_dhcp_lease(driver, expect_edit_ip, expect_name=None, expect_mac=None, expect_ip=None):
    repeat_times = 3
    while repeat_times > 0:
        print(f"这是编辑mac绑定ip倒数第{repeat_times}次")
        move_to_static_dhcp_lease_page(driver)
        try:
            # 点击编辑按钮
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, StaticDhcpLeaseLocators.edit_button.format(expect_edit_ip)))
            ).click()
            if expect_name is not None:
                # 清空name输入框d
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, StaticDhcpLeaseLocators.name_input))).clear()
                # 输入name
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, StaticDhcpLeaseLocators.name_input))).send_keys(expect_name)
            if expect_mac is not None:
                # 清空mac输入框
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, StaticDhcpLeaseLocators.mac_input))
                ).clear()
                # 输入mac
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, StaticDhcpLeaseLocators.mac_input))
                ).send_keys(expect_mac)
            if expect_ip is not None:
                # 清空ip输入框
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, StaticDhcpLeaseLocators.ip_input))
                ).clear()
                # 输入ip
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, StaticDhcpLeaseLocators.ip_input))
                ).send_keys(expect_ip)
            # 最后保存
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, StaticDhcpLeaseLocators.save_button))
            ).click()
            print("编辑mac绑定ip成功")
            return
        except:
            time.sleep(60)
        finally:
            repeat_times -= 1
    print("编辑mac绑定ip失败")
    assert False


def check_static_dhcp_lease(driver, check_expect_operation_type, check_expect_name=None,
                            check_expect_mac=None, check_expect_ip=None):
    repeat_times = 3
    while repeat_times > 0:
        print(f"这是检查mac绑定ip倒数第{repeat_times}次")
        # 移动到消息中心页
        operation_type, message_status = user_public_fun.move_to_message_center(driver)
        print(operation_type, message_status)
        # 判断操作类型是否正确，当操作类型正确且状态为成功时切换到mac/ip绑定页面查看数据
        if operation_type == check_expect_operation_type and message_status == 'Succeeded':
            move_to_static_dhcp_lease_page(driver)
        else:
            print('检查mac绑定ip消息中心操作类型或状态错误')
            return False
        try:
            # 检查ip
            EC.presence_of_element_located((By.XPATH, StaticDhcpLeaseLocators.ip_list.format(check_expect_ip)))
            # 检查name
            if check_expect_name is not None:
                actual_name = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, StaticDhcpLeaseLocators.name_list.format(check_expect_ip)))).text
                print('实际的name', actual_name)
                if actual_name != check_expect_name:
                    if repeat_times == 1:
                        print('检查名称失败')
                        return False
                    assert False
            # 检查mac
            if check_expect_mac is not None:
                actual_mac = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, StaticDhcpLeaseLocators.mac_list.format(check_expect_ip)))).text
                print('实际的mac', actual_mac)
                if check_expect_mac != actual_mac:
                    if repeat_times == 1:
                        print('检查mac失败')
                        return False
                    assert False
            print('检查mac绑定ip成功')
            return True
        except:
            time.sleep(2)
        finally:
            repeat_times -= 1
    print("检查mac绑定ip失败")
    assert False


def delete_static_dhcp_lease(driver, expect_delete_ip):
    repeat_times = 3
    while repeat_times > 0:
        print(f"这是删除mac绑定ip倒数第{repeat_times}次")
        move_to_static_dhcp_lease_page(driver)
        try:
            # 点击删除按钮
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, StaticDhcpLeaseLocators.delete_button.format(expect_delete_ip)))
            ).click()
            # 点击确定删除按钮
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, StaticDhcpLeaseLocators.ok_button))).click()
            print('删除mac绑定ip完成')
            return
        except:
            time.sleep(10)
        finally:
            repeat_times -= 1
    print("删除mac绑定ip失败")
    assert False


def check_delete_static_dhcp_lease(driver, check_delete_ip, check_expect_operation_type):
    # 移动到消息中心页
    repeat_times = 3
    while repeat_times > 0:
        try:
            print(f"这是检查删除mac绑定ip倒数第{repeat_times}次")
            operation_type, message_status = user_public_fun.move_to_message_center(driver)
            print(operation_type, message_status)
            # 判断操作类型是否正确，当操作类型正确且状态为成功时切换到mac/ip绑定页面查看数据
            if operation_type == check_expect_operation_type and message_status == 'Succeeded':
                move_to_static_dhcp_lease_page(driver)
            else:
                print('检查mac绑定ip消息中心操作类型或状态错误')
                return False
            # 等待进度条加载完成
            WebDriverWait(driver, 20).until_not(
                EC.element_to_be_clickable((By.XPATH, StaticDhcpLeaseLocators.ip_list.format(check_delete_ip)))
            )
            print('删除成功')
            return True
        except:
            time.sleep(10)
            if repeat_times == 1:
                print('删除失败')
                return False
        finally:
            repeat_times -= 1
    print("检查删除mac绑定ip失败")
    assert False
