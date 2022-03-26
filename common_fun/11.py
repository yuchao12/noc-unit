# a='Total 8499'
# b=a[0:6]
# c=a[6:]
# print(b)
# print(c)
# print(b+str(int(c)+1))
from email._header_value_parser import get_attribute
# from time import sleep
#
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
#
# a=WebDriver()
# a.get('https://noc.merckuwifi.net/login')
# sleep(3)
# c=a.current_url
# print(c)
# a.quit()
# from common_conf.conf import port_forwarding
#
# expect_sn=15125121
#
# expect_url="https://noc.merckuwifi.net/mesh/"+f'{expect_sn}'+"/setting/portforwarding"#预期网址
# a='https://noc.merckuwifi.net/mesh/'+str(expect_sn)+'/setting/portforwarding'
# print(a,expect_url)
#
#
# portname='//div[text()=1212432]'
# b = '//div[text()='+port_forwarding["name"]+']'
# print(port_forwarding["name"])
# print(b)
# from common_conf.conf import port_forwarding
# #
# # a=['1212432', '0.0.0.0/1-5', '192.168.127.39/1-5', 'TCP', '', 'Edit Delete']
# # b=a[0:3]
# # print(b)
# #
#c=[port_forwarding["name"],port_forwarding['remote_ip']+'/'+port_forwarding["port_num1"]+'-'+port_forwarding["port_num2"],port_forwarding['local_ip']+'/'+port_forwarding["port_num3"]+'-'+port_forwarding["port_num4"]]
# # print(c)
# # if b==c:
# #     print(111111111111111)
# # else:
# #     print(444)
# # d=['1212432', '0.0.0.0/1-5', '192.168.127.39/1-5', 'TCP', '', 'Edit Delete', 'sasda', '0.0.0.0/6-9', '192.168.127.11/6-9', 'TCP&UDP', '', 'Edit Delete']
# #
# # if c in d:
# #     print(1)
# # else:print(2)
# a=1
# print('//tbody/tr['+str(a)+']')
# from common_conf.conf import Port_forwarding
#
# a='//span[text()=TCP"]'
# print('//span[text()="'+Port_forwarding["Protocol_TCP"]+'"]')
# "//div[text()=' 192.168.127.99/10-50 ']/following::button[@class='el-button button button--setting el-button--text']"
# a='192.168.127.99/10-50'
# print(a.split('/'))
# b=a.split('/')[0]
# print(b)
# expect_local_ip='192.168.127.126/10-20'
# row2 = '//div[text()=' + "' " + expect_local_ip + " '" +']'+'/preceding::td[2]/div'
# print(row2)
# expect_ip='192.168.127.139'
# # expect_portnum3='21'
# # expect_portnum4='30'
# # # print('//div[text()=' + "' " + expect_ip + "/" +expect_portnum3+'-'+expect_portnum4+" ']")
# expect_Protocol='TCP'
# print('//span[text()="{}"]'.format(expect_Protocol))
# expect_ip='192'
# expect_portnum3='20'
# expect_portnum4='30'
# a=f"{expect_ip}/{expect_portnum3}-{expect_portnum4}"
# print(a)
expect_local_ip='192.168.127.126/10-20'
# udp_port3='10'
# udp_port4='20'
# print("//div[text()=' {}/{}-{} ']/following::button[1]".format(pd_ip,udp_port3,udp_port4))

a="//div[text()=' {} ' ]/preceding::td[2]/div"
print(a.format(expect_local_ip))