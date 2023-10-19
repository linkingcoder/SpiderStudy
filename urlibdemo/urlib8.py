import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers = {
 'Cookie': 'BAIDUID=E19F86F68808A630B3ED1C09FD590114:FG=1; BIDUPSID=E19F86F68808A630B3ED1C09FD590114; PSTM=1690943955; BAIDUID_BFESS=E19F86F68808A630B3ED1C09FD590114:FG=1; ZFY=72KfJ4F2671ajLmtF9Fsw3EEhed2LTUTdBw0sBZ2aT4:C; APPGUIDE_10_6_5=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=mFLSFhhSkVreGJsWWNPUFR4YmJRalZobnFLTElhTXMxamZNdFVYN09tdTI1bEJsRVFBQUFBJCQAAAAAAAAAAAEAAACH05rrMTU5TUhrSkQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALZZKWW2WSllS; BDUSS_BFESS=mFLSFhhSkVreGJsWWNPUFR4YmJRalZobnFLTElhTXMxamZNdFVYN09tdTI1bEJsRVFBQUFBJCQAAAAAAAAAAAEAAACH05rrMTU5TUhrSkQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALZZKWW2WSllS; APPGUIDE_10_6_6=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1695540606,1695540786,1697439368; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1697439535; ab_sr=1.0.1_ZmQzZjUyMjQxMGY5Y2Y2NWY3OTliN2IxOGNkZjhmNmYxMzJjOGQ3YzA1ZWViZDFjYTk3MjY1YjhiYThkM2FiNmVmOTczMDdjZmIwOTdjNTJkN2NkMTJkMDA3MzEzZmVlNjU3ZjliMmFmY2RiNTExNWZiOTA3ZmQzMGNmYzNiYWI5N2MxODAwNDhlMTQyODg4Y2MwYTA1NTE2MTVlMjcxMTFhNTQyZjgyZTBkNzU0ODZlMDNlNTJmNjE2Mjk2MTRj',
'Acs-Token':'1697439534658_1697439573103_hYteuS3ht5AKcCD3xUSAClI5efFw6scvVRsEx18CGmYsiL0lXPjUPV5Y49AaIP/28F+E4TiUoumJGOz4OwAxfmWjnjZzsIG9WAGcCowZbbKfsOQSZYQ3i8d7p2/bdEsjVL0d5MFVqjhlerfY0jHI8/h9rFgAf6YLF6AO7UHGZm989yxYyC85IG8dYBTQeC0mNvL+AzGl6jRB7gfBpMdZT5vTOz5s884oWzOoVXsKRqfJi0148iCIK7DnRhhhP9zUhM/CdZppeIH0cupfzwEYThFett3Z0TLh4Kqq8iqwzoXnNB7/vcFiLp/E6xBYpYI1UZig0DhlvPMQ98ojxCxKbumIeI9OuYzTPjlaxF7c+UlfZHfZKSXFf8ZfOiEalSe3cbWHAyZcWy4oRw8UZN2EOEVvug2IzPH1EILqLSmHx1PPgADHjdNRbWj3KH+6RK+Nx2TooIdvONctFpXaCD+8mVoJvTM+9NyHax2RvuXxZbMq4gBZQqsfGPHTuQLSAZb+'
}
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'spider',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '63766.268839',
    'token': 'e58b2bac0d9586c8dac94336cf1d38ec',
    'domain': 'common',
    'ts': '1697439573093',
}
data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
import json

obj = json.loads(content)
print(obj)