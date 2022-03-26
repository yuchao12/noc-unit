from telnetlib import EC
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from common_conf.conf import except_sn
from common_conf.xpath.speed import Speed_test_Locators
from selenium.webdriver.support import expected_conditions as EC

def move_to_speed_test_page(driver):
    """移动到网络测速页面"""
    repeat_times = 1
    while repeat_times < 4:
        print(f'这是第{repeat_times}次进入')
        try:
            if Speed_test_Locators.expect_url in driver.current_url:
                # 判断是否已经在网络测速的页面
                print('刷新页面')
                driver.refresh()
            else:
                print('开始进入到网络测速页面')
                driver.find_element(By.XPATH, Speed_test_Locators.net_seting).click()
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, Speed_test_Locators.speed))
                ).click()
                # 进入到网络测速的页面
                sleep(2)
            actul_url = driver.current_url
            # 获取当前页面的url
            if actul_url == Speed_test_Locators.expect_url.format(except_sn):
                print('进入网络测速页面成功')
                sleep(3)
                return True
        except:
            driver.refresh()
            sleep(2)
        finally:
            repeat_times += 1
    print('进入网络测速页面失败')
    assert False

def speed_test(driver):
    #网络测速功能
    move_to_speed_test_page(driver)
    repeat_times = 1
    while repeat_times < 4:
        print(f'这是第{repeat_times}次进入')
        try:
            a = driver.find_element(By.CLASS_NAME, Speed_test_Locators.speed_total).text
            # 获取测速记录的总条数
            b = a[0:6]
            c = a[6:]
            except_total = b + str(int(c) + 1)
            # 测速记录的总条数+1
            sleep(3)
            driver.find_element(By.XPATH, Speed_test_Locators.speed_button).click()
            sleep(150)
            # 测速需要的时间
            actul_total = driver.find_element(By.CLASS_NAME, Speed_test_Locators.speed_total).text
            if actul_total == except_total:
                print('进入网络测速页面成功')
                sleep(2)
                return True
        except:
            driver.refresh()
            sleep(2)
        finally:
            repeat_times += 1
    print('进入网络测速页面失败')
    assert False

def check_speed_test(driver):
    print(1)