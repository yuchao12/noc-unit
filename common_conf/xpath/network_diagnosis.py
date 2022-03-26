class NetworkDiagnosisLocators(object):
    # 高级设置菜单栏
    advanced_settings_menu = '//div[text()="Advanced settings"]'
    # 页面加载进度条
    loading = "//div[@id='nprogress']"
    # DMZ菜单栏
    network_diagnosis_menu = '//body/div[@class="el-menu--horizontal menus__popper-menu"]/ul/li[text()=" Network Diagnosis "]'
    # 工具输入框
    tool_input = '//div[@class="el-input el-input--medium el-input--suffix"]/input'
    # 工具下拉选择框
    tool_select = '//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li/span[text()="{}"]'
    # 地址输入框
    address_input = '//div[@class="el-input el-input--medium"]/input'
    # 保存按钮
    save_button = '//button[@class="el-button el-button--primary el-button--medium"]'
    # tolst提示
    
