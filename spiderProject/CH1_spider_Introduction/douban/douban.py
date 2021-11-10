import requests
import json
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}

params = {
    'type': 'tv',
    'tag': '热门',
    'page_limit': 50
}

url = 'https://movie.douban.com/j/search_subjects'

total_page = int(input('input page:'))

for page in range(total_page):
    params['page_start'] = page
    try:
        r = requests.get(url, headers=headers, params=params)
        # print(r.url)
        r.raise_for_status()
        # print(r.headers)  # 访问服务器返回给我们的响应头部信息
        # print(r.request.headers)  # 发送到服务器的请求的头部
        r.encoding = r.apparent_encoding
        if os.path.isfile('res.txt') and page == 0:
            os.remove('res.txt')
        with open('res.txt', mode='a', encoding='utf-8') as f:
            f.write(json.dumps(r.json(), ensure_ascii=False, indent=4))
            f.write('\n')
        print(f'done {page}')
    except:
        print('error')

