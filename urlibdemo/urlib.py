proxies_pool = [
    {'http': '180.123.9.124:888811111'},
    {'http': '180.123.9.124:888822222'}
]
import random

proxies = random.choice(proxies_pool)
url = 'http://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
import urllib.request

request = urllib.request.Request(url=url,headers=headers)
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('uft-8')
with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)