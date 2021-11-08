import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}

params = {
    'type': 'tv',
    'tag': '国产剧',
    'page_limit': 50,
    'page_start': 0
}

url = 'https://movie.douban.com/j/search_subjects'

try:
    r = requests.get(url, headers=headers, params=params)
    # print(r.url)
    r.raise_for_status()
    # print(r.headers)  # 访问服务器返回给我们的响应头部信息
    # print(r.request.headers)  # 发送到服务器的请求的头部
    r.encoding = r.apparent_encoding
    with open('res.json', mode='w', encoding='utf-8') as f:
        f.write(json.dumps(r.json(), ensure_ascii=False, indent=4))
    print('done')
except:
    print('error')

