import time
from common_conf.xpath.admin_password import AdminPasswordLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common_fun import user_public_fun


def move_to_admin_password_page(driver):
    repeat_times = 3
    while repeat_times > 0:
        print(f'这是进入管理密码页倒数第{repeat_times}次')
        try:
            # 判断当前页面是否为Network Diagnosis页
            if "setting/safe" in driver.current_url:
                print('刷新')
                driver.refresh()
            else:
                # 鼠标移动到其他设置
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(AdminPasswordLocators.other_settings_menu)).perform()
                time.sleep(0.5)
                # 鼠标移动到管理密码菜单
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(AdminPasswordLocators.admin_password_menu)).perform()
                # 点击管理密码菜单
                driver.find_element_by_xpath(AdminPasswordLocators.admin_password_menu).click()
                time.sleep(0.5)
            # 等待进度条加载完成
            WebDriverWait(driver, 20).until_not(
                EC.element_to_be_clickable((By.XPATH, AdminPasswordLocators.loading))
            )
            time.sleep(0.5)
            print('进入管理密码页面成功')
            return True
        except:
            driver.refresh()
            time.sleep(2)
        finally:
            repeat_times -= 1
    print("进入管理密码页面报错")
    assert False


def change_admin_password(driver, expect_password):
    repeat_times = 3
    while repeat_times > 0:
        print(f"这是管理密码倒数第{repeat_times}次")
        move_to_admin_password_page(driver)
        try:
            # 输入新密码
            print(11111111111111111)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, AdminPasswordLocators.new_password_input))
            ).send_keys(expect_password)
            # 输入确认密码
            print(22222222222222)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, AdminPasswordLocators.confirm_input))
            ).send_keys(expect_password)
            # 最后保存
            print(333333333333333333333)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, AdminPasswordLocators.save_button))
            ).click()
            print("修改管理密码成功")
            return
        except:
            time.sleep(60)
        finally:
            repeat_times -= 1
    print("修改管理密码失败")
    assert False


def check_admin_password(driver, repeat_times=3):
    while repeat_times > 0:
        print(f"这是检查密码管理倒数第{repeat_times}次")
        # 移动到消息中心页
        operation_type, message_status = user_public_fun.move_to_message_center(driver)
        try:
            if operation_type != 'Modify the administrator password':
                if repeat_times == 1:
                    print('管理密码检查操作类型失败')
                    return False
                assert False
            if message_status != 'Succeeded':
                if repeat_times == 1:
                    print('检查管理密码失败状态失败')
                    return False
                assert False
            return True
        except:
            time.sleep(5)
        finally:
            repeat_times -= 1
