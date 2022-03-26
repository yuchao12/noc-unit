from common_conf import conf
from common_fun.base import Base
from common_fun import wifi_settings_fun


class WifiSettings(Base):
    # def setUp(self):
    #     super(WifiSettings, self).setUp()
    #     wifi_settings_fun.move_to_wifi_settings_page(self.driver)

    def test_01_wifi_setting(self):
        """双频合一开启,修改所有值保存"""
        wifi_settings_fun.set_smart_connect(self.driver, "on", "22222222", "WPA2-PSK", "22222222", "2", "20", "153",
                                            "40")

    def test_02_check_wifi_settings(self):
        """双频合一开启,检查所有值保存"""
        wifi_settings_fun.check_wifi_settings(self.driver, "on","22222222", "WPA2-PSK", "2", "20", "153",
                                              "40")
