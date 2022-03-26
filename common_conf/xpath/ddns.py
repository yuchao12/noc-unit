class DdnsLocators(object):
    # 高级设置
    advanced_settings_menu = '//div[text()="Advanced settings"]'
    # 页面加载进度条
    loading = "//div[@id='nprogress']"
    # DDNS菜单栏
    ddns_menu = '//body/div[@class="el-menu--horizontal menus__popper-menu"]/ul/li[text()=" DDNS "]'
    # 服务提供商输入框
    service_provider_input = '//div[@class="el-select"]/div[@class="el-input el-input--suffix"]/input'
    # 服务提供商下拉选择框
    service_provider_select = '//span[text()="{}"]'
    # 被选择的服务提供商
    service_provider_is_selected = '//li[@class="el-select-dropdown__item selected hover"]/span'
    # 域名输入框
    domain_input = '//form/div[2]/div/div/input'
    # 用户名输入框
    username_ddns_input = '//form/div[3]/div/div/input'
    # 密码输入框
    password_ddns_input = '//form/div[4]/div/div/input'
    # 状态选择框
    status_checkbox = '//span[@class="el-checkbox__label"]'
    # 判断状态是否启用
    status_check = '//form/div[@class="el-form-item is-no-asterisk"][2]/div[@class="el-form-item__content"]/label'
    # 保存按钮
    save_button = '//button[@class="el-button el-button--primary"]'
