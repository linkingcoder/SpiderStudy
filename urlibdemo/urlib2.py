import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)
# print(type(response))
# 按照字节读
# content = response.read()
# 返回5个字节
# content = response.read(5)
# 读取一行
# content = response.readline()
content = response.readlines()
print(content)
# 返回状态码 200正确
print(response.getcode())
print(response.geturl())
# 状态信息
print(response.getheaders())