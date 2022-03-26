class DmzLocators(object):
    # 高级设置菜单栏
    advanced_settings_menu = '//div[text()="Advanced settings"]'
    # 页面加载进度条
    loading = "//div[@id='nprogress']"
    # DMZ菜单栏
    dmz_menu = '//body/div[@class="el-menu--horizontal menus__popper-menu"]/ul/li[text()=" DMZ host "]'
    # DMZ host 输入框
    dmz_input = '//div[@class="el-input"]/input[@class="el-input__inner"]'
    # status 选择框
    status_checkbox = '//div[@class="el-form-item__content"]/label'
    # 保存按钮
    save_button = '//button[@class="el-button el-button--primary"]'

