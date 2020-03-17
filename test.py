
import requests
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
url="https://www.xicidaili.com/wt"
proxies={'http':'http://127.0.0.1:10809'}
r=requests.get(url=url,headers=headers,proxies=proxies,timeout=5)
r.encoding='utf-8'

print(r.text)
