import urllib.request
# 定义url
url = 'http://www.baidu.com'
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)
# 获取响应中的页面的源码
# 二进制--》字符串--》解码
content = response.read().decode('utf-8')
print(content)