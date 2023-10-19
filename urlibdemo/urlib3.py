import urllib.request
# 网页
url_page = 'http://www.baidu.com'

urllib.request.urlretrieve(url_page, 'resource/baidu.html')

# 图片
url_img = "https://t7.baidu.com/it/u=1595072465,3644073269&fm=193&f=GIF"
urllib.request.urlretrieve(url=url_img, filename='resource/pic.png')
# 视频
url_video = ''
urllib.request.urlretrieve(url=url_img, filename='v.mp4')
