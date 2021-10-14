# 非Python自带库 需要安装
# pip install requests

import requests
query = input('Input name:')

url = f"https://www.sogou.com/web?query={query}"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}

try:
    res = requests.get(url)
    res.raise_for_status()
    res.encoding = res.apparent_encoding
    with open('res.html', encoding="utf-8", mode="w") as f:
        f.write(res.text)
    print('Done')
except:
    print("Error")
