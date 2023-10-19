import urllib.request
# get请求
heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'

}

import urllib.parse
import urllib.request

def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    request = urllib.request.Request(url=url, headers=heads)
    return request
def getContent(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content
def download(page,content):
    with open('douban'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)





if __name__ == '__main__':
    start_page = int(input('起始页码'))
    end_page = int(input('结束页码'))
    for page in range(start_page, end_page + 1):
        # 定制每一页请求
        request = create_request(page)
        content = getContent(request)
        download(page,content)