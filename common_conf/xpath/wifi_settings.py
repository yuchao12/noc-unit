class WifiSettingsLocators():
    # wifi设置主菜单
    wifi_settings_menus = '//h3[@class="menus-parent__title"]'

    # wifi子菜单
    wifi_menus = '//span[text()="Wi-Fi"]'

    # 双频合一开关
    smart_button = '//div[@role="switch"]'

    # 双屏开启时xpath
    # ssid
    ssid_input = '//div[@class="form"]/div[1]/div[2]/div/input'

    # 加密方式
    encryption_input = '//div[@class="form"]/div[2]/div[2]/div/div[1]/input'
    select_encryption = '//span[text()="{num}"]/..'
    # 密码
    password_input = '//div[@class="form"]/div[3]/div[2]/div/input'

    # 2.4信道
    channel_24g = '//div[@class="form"]/div[4]/div[2]/div/div/input'  #//div[1]/div[4]/div[2]//div/input
    select_channel_24g = '//span[text()="{num}"]/..'
    # 2.4频宽
    channel_width_input_24g = '//div[@class="form"]/div[5]/div[2]/div/div/input' #//form/div[2]/div[1]/div[5]/div[2]//div/input
    select_channel_width_24g = '//span[text()="{num}"]/..'

    # 5g信道
    channel_5g = '//div[@class="form"]/div[6]/div[2]/div/div/input'  #//div[2]/div[4]//div[1]/input
    select_channel_5g = '//span[text()="{num}"]/..'
    # 5g频宽
    channel_width_input_5g = '//div[@class="form"]/div[7]/div[2]/div/div/input'  #//form/div[2]/div[2]/div[5]/div[2]//div/input
    select_channel_width_5g = '//span[text()="{num}"]/..'

    # 保存按钮
    save_button = '//button[@type="button"]'
