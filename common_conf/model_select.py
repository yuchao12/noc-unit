#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:  yuchao

from .args import argss

noc_information = {
    "99999": {
        "isp_name": "Mercku",
        "customer_id": "0001",
        "noc_url": "https://noc.merckuwifi.net/",
        "username": "123456",
        "password": "12345678"
    },
    "00003": {
        "isp_name": "Startca",
        "customer_id": "0003",
        "noc_url": "",
        "username": "",
        "password": ""
    },
    "00004": {
        "isp_name": "Inverto",
        "customer_id": "0004",
        "noc_url": "https://noc-inverto.merckuwifi.com/",
        "username": "",
        "password": ""
    },
    "00005": {
        "isp_name": "Orion",
        "customer_id": "0005",
        "noc_url": "https://noc-orion.merckuwifi.com/",
        "username": "",
        "password": ""
    },
    "00006": {
        "isp_name": "Realnett",
        "customer_id": "0006",
        "noc_url": "https://noc-realnett.merckuwifi.com/",
        "username": "",
        "password": ""
    },
    "00007": {
        "isp_name": "Altima",
        "customer_id": "0007",
        "noc_url": "https://noc-altima.merckuwifi.com/",
        "username": "",
        "password": ""
    },
    "00008": {
        "isp_name": "45networks",
        "customer_id": "0001",
        "noc_url": "https://noc-45networks.merckuwifi.com/",
        "username": "",
        "password": ""
    },
    "00009": {
        "isp_name": "Solufi",
        "customer_id": "0001",
        "noc_url": "https://noc-solufi.merckuwifi.com/",
        "username": "",
        "password": ""
    },
    "00010": {
        "isp_name": "Campcomm",
        "customer_id": "0001",
        "noc_url": "https://noc-campcomm.merckuwifi.com/",
        "username": "",
        "password": ""
    },
    "00011": {
        "isp_name": "Kelcom",
        "customer_id": "0001",
        "noc_url": "https://noc-kelcom.merckuwifi.com/",
        "username": "",
        "password": ""
    },
    "00012": {
        "isp_name": "Test",
        "customer_id": "0001",
        "noc_url": "https://noc-test.merckuwifi.com/",
        "username": "",
        "password": ""
    },
    "00013": {
        "isp_name": "FibreStream",
        "customer_id": "0001",
        "noc_url": "https://noc-fibrestream.merckuwifi.com",
        "username": "",
        "password": ""
    }
}

if argss.noc_id in noc_information:
    url = noc_information[argss.noc_id]["noc_url"]
    root_password = noc_information[argss.noc_id]["username"]
    root_username = noc_information[argss.noc_id]["password"]
else:
    print("\n\n\n-----------------------------------------")
    print("|       当前运营商有noc的如下：          |")
    print("|    noc_id:99999， isp: Mercku         |")
    print("|    noc_id:00003， isp: Startca        |")
    print("|    noc_id:00004， isp: Inverto        |")
    print("|    noc_id:00005， isp: Orion          |")
    print("|    noc_id:00006， isp: Realnett       |")
    print("|    noc_id:00007， isp: Altima         |")
    print("|    noc_id:00008， isp: 45networks     |")
    print("|    noc_id:00009， isp: Solufi         |")
    print("|    noc_id:00010， isp: Campcomm       |")
    print("|    noc_id:00011， isp: Kelcom         |")
    print("|    noc_id:00012， isp: Test           |")
    print("|    noc_id:00013， isp: FibreStream    |")
    print("|                                       |")
    print("| 后续有新运营商时，补充这里的描述即可... |")
    print("-----------------------------------------")
    print("请输入运营商对应的正确noc_id！！！\n\n\n")
    assert False
