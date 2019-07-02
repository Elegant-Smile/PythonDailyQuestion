"""
 author:jjk
 datetime:2019/5/2
 coding:utf-8
 project name:Pycharm_workstation
 Program function:
 
"""
# !/usr/bin/env python
# coding:UTF-8

import requests
from requests.exceptions import *
from collections import ChainMap

target_url = 'https://www.163.com/'
base_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
}
custom_headers = {}

headers = ChainMap(base_headers, custom_headers)

try:
    response = requests.get(target_url, headers=headers)
    print(response.text)

except ConnectionError as e:
    print(f'Unable to connect: {str(e)}')
except HTTPError as e:
    print(f'Http Error: {str(e)}')
except Timeout as e:
    print(f'Connection timeout')
except RequestException as e:
    print(f'Other error: {str(e)}')
