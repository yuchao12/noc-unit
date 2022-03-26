import time
from common_conf.xpath.blocklist import BlockList
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def move_to_blocklist_page(driver):
    repeat_times = 3
    while repeat_times > 0:
        try:
            driver.find_elements_by_xpath('//h3[@class="menus-parent__title"]')[3].click()
            driver.find_element_by_xpath("//span[text()='Blocklist']").click()
            print('进入到黑名单设置页面')
            time.sleep(1)
            if "setting/blacklist" in driver.current_url:
                WebDriverWait(driver, 20).until_not(
                    EC.element_to_be_clickable((By.XPATH, "//div[@id='nprogress']"))
                )
                time.sleep(0.5)
                print('进度条找到了')
                return True
        except:
            driver.refresh()
            time.sleep(2)
        finally:
            repeat_times -= 1
    print("进入黑名单页面报错")
    assert False


def add_new_blocklist(driver, expect_mac=None, expect_name=None):
    repeat_time = 3
    while repeat_time > 0:
        move_to_blocklist_page(driver)
        try:
            print('开始添加新的黑名单')
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, BlockList.add_button))).click()
            driver.find_elements_by_xpath(BlockList.input)[0].send_keys(expect_mac)
            driver.find_elements_by_xpath(BlockList.input)[1].send_keys(expect_name)
            driver.find_element_by_xpath(BlockList.save_button).click()
            return True
        except:
            print('出错了')
        finally:
            repeat_time -= 1
    print('添加黑名单失败')
    assert False


def delete_blocklist(driver, num):
    # //tbody/tr[{i}]/td[1]/div
    repeat_time = 3
    while repeat_time > 0:
        move_to_blocklist_page(driver)
        try:
            print("开始删除黑名单")
            button_del = BlockList.delete_button.format(num)

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_del))).click()
            print('黑名单按钮')

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, BlockList.delete_ok_button))).click()
            print('确定')
            driver.refresh()
            return True
        except:
            pass
        finally:
            repeat_time -=1
    print('删除黑名单失败')
    assert False


def check_blocklist(driver, expect_mac=None, expect_name=None, repeat_times=3):
    # 获取列表的行
    while repeat_times > 0:
        print("这是倒数第%d次" % repeat_times)
        move_to_blocklist_page(driver)
        try:
            # 检查mac地址
            if expect_mac is not None:
                tr = driver.find_elements_by_xpath('//tbody/tr')
                mac_list = []
                if len(tr) > 0:
                    for i in range(1, len(tr) + 1):
                        mac = driver.find_element_by_xpath(f'//tbody/tr[{i}]/td[1]/div').text
                        mac_list.append(mac)
                    print(mac_list)
                if expect_mac not in mac_list:
                    if repeat_times == 1:
                        print("失败")
                        return False
                    driver.refresh()
                    assert False
                print("mac在列表中")
            # 检查Name
            if expect_name is not None:
                tr = driver.find_elements_by_xpath('//tbody/tr')
                name_list = []
                if len(tr) > 0:
                    for num in range(1, len(tr) + 1):
                        name = driver.find_element_by_xpath(f'//tbody/tr[{num}]/td[2]/div').text
                        name_list.append(name)
                    print(name_list)
                if expect_name not in name_list:
                    if repeat_times == 1:
                        print("失败")
                        return False
                    assert False

                print("name在列表中")
            return True

        except:
            time.sleep(5)
        finally:
            repeat_times -= 1
    assert False
