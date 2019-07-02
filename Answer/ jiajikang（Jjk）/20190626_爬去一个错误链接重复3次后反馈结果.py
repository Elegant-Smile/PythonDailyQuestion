"""
 author:jjk
 datetime:2019/5/2
 coding:utf-8
 project name:Pycharm_workstation
 Program function: 爬取一个错误的URL网页，当请求失败时，再次发出请求，最多重复3次，若3次均请求失败，返回None
 
"""
# !/usr/bin/env python
# coding:UTF-8

import requests
from requests.exceptions import *
from time import sleep
from collections import ChainMap

def exit_on_multiple_fail(fail_counter):
    def decorator(func):
        def wrapper(*key, **args):
            for i in range(fail_counter):
                response = func(*key, **args)
                if response:
                    break
                print(f'failed for {i+1} time(s)\n')
                sleep(1)
            else:
                print(f'Failed for {fail_counter} time(s), exiting!')
            return response

        return wrapper

    return decorator


@exit_on_multiple_fail(3)
def file_get_content(path, custom_headers={}):
    # 代理服务器
    base_headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    }

    headers = ChainMap(custom_headers, base_headers)

    try:
        response = requests.get(path, headers=headers)
        return response
    except ConnectionError as e:
        print(f'Unable to connect: {str(e)}')
        return False
    except HTTPError as e:
        print(f'Http Error: {str(e)}')
        return False
    except Timeout as e:
        print(f'Connection timeout')
        return False
    except RequestException as e:
        print(f'Other error: {str(e)}')
        return False
# 请求链接
response = file_get_content('https://www.16fdafdas3.com')

if response:
    print(response.text)
    print(response.status_code)
