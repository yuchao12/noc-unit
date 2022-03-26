class AdminPasswordLocators(object):
    # 高级设置菜单栏
    other_settings_menu = '//div[text()="Other settings"]'
    # 页面加载进度条
    loading = "//div[@id='nprogress']"
    # 管理密码菜单
    admin_password_menu = '//body/div[@class="el-menu--horizontal menus__popper-menu"]/ul/li[text()=" Admin password "]'
    # 新密码输入框
    new_password_input = '//form/div[1]/div[2]/div/input'
    # 确认密码框
    confirm_input = '//form/div[2]/div[2]/div/input'
    # 保存按钮
    save_button = '//button[@class="el-button el-button--primary"]'
