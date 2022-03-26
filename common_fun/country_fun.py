import time
from common_conf.xpath.country import CountryLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def move_to_country(driver):
    repeat_times = 3
    while repeat_times > 0:
        print(f'这是{repeat_times}次进入')
        try:
            if "setting/region" in driver.current_url:
                driver.refresh()
            else:
                driver.find_elements_by_xpath(CountryLocators.other_setting_menu)[4].click()
                driver.find_element_by_xpath(CountryLocators.country_menu).click()
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
    print("进入国家页面报错")
    assert False


def change_country(driver, expect_country=None):
    repeat_times = 3
    while repeat_times > 0:
        move_to_country(driver)
        try:
            if expect_country is not None:
                WebDriverWait(driver, 10).until_not(
                    EC.element_to_be_clickable((By.XPATH, CountryLocators.country_input))
                ).click()
                WebDriverWait(driver, 10).until_not(
                    EC.element_to_be_clickable((By.XPATH, CountryLocators.country_select.format(expect_country)))
                ).click()

        except:
            pass
