class GuestWifiLocators(object):
    # Wi-Fi settings菜单栏
    wifi_settings_menu = '//div[text()="Wi-Fi settings"]'
    # 页面加载进度条
    loading = "//div[@id='nprogress']"
    # Guest Wi-Fi菜单栏
    guest_wifi_menu = '//body/div[@class="el-menu--horizontal menus__popper-menu"]/ul/li[text()=" Guest Wi-Fi "]'
    # 访客wifi开启关闭开关
    wifi_opened_button = '//form[@class="el-form forms mesh-settings__content el-form--label-top"]/div[1]/div/div'
    # 有效时长输入框
    duration_input = '//div[@class="el-form-item"][1]/div/div/div[1]/input'
    # 有效时常下拉框
    duration_select = '//div[@class="el-select-dropdown el-popper"][2]/div[1]/div[1]/ul/li/span[text()="{}"]'
    # 无线名称输入框
    ssid_input = '//div[@class="el-form-item"][2]/div/div/input'
    # 加密方式输入框
    encryption_input = '//div[@class="el-form-item"][3]/div/div/div/input'
    # 加密方式下拉框
    encryption_select = '//div[@class="el-select-dropdown el-popper"][2]/div[1]/div[1]/ul/li/span[text()="{}"]'
    # 密码输入框
    password_input='//div[@class="el-form-item"][4]/div/div/input'
    # 双频合一开关
    smart_connect_button = '//div[@class="el-form-item switch-wrap"][2]/div/div'
    # 双频合一开关状态
    smart_connect_status = '//div[@class="el-form-item switch-wrap"][2]/div/div'
    # 保存按钮
    save_button = '//button[@class="el-button el-button--primary el-button--medium"]'
