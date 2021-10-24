import requests

url = 'https://fanyi.baidu.com/sug'

wd = input('Please input English word:\t')

data = {
    'kw': wd
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}

try:
    r = requests.post(url, data=data, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.json())
except:
    print('error')
