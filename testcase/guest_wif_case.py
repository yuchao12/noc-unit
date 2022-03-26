from noc.common_fun import guest_wifi_fun
from noc.common_conf import conf
from noc.common_fun.base import Base
import unittest


class GuestWifi(Base):
    def test01_change_guest_wifi(self):
        guest_wifi_fun.change_guest_wifi(self.driver, expect_wifi_opened_status='on', expect_duration='1 day',
                                         expect_ssid="gtt_Mercku Guest",
                                         expect_encryption="WPA2-PSK", expect_password='987654321',
                                         expect_smart_connect_status='off')
