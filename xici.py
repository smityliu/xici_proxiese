import requests
import traceback
import re
import random
import time

url ='https://www.xicidaili.com/wn/'
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }

def get_ip(web):
    try:
        patterns_port = '<td>(\d{1,5})</td>'
#匹配端口
        patterns_ip = '<td>((?:(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d))</td>'
#匹配ip
        ip = re.findall(patterns_ip,web)
        port = re.findall(patterns_port,web)
        #print(ip)
        #print(port)
        list_ip = []
#整合端口和ip
        for i in range(len(ip)):
            list_ip.append("http://"+ip[i]+ ':' +port[i])
        return list_ip
    except Exception:
        traceback.print_exc()

def main():
    try:
        web = requests.get(url, headers=headers)
        web.encoding = web.apparent_encoding
        #获取网页编码格式，requests的返回结果对象里有个apparent_encoding函数, apparent_encoding通过调用chardet.detect()来识别文本编码. 但是需要注意的是，这有些消耗计算资源.
        if web.status_code == 200:
            result = get_ip(web.text)
            for i in result:
                print(check(i))
                print('\n')
        else:
            raise ConnectionError
    except Exception:
        traceback.print_exc()
        

def check(example):
    url="https://www.cip.cc/"
    proxies={'https':example}
    print(proxies)
    try:
        r=requests.get(url=url,headers=headers,proxies=proxies,timeout=5)
        return "sccuess"
    except Exception:
        return "failed"

if __name__ == '__main__':
    while(1):
        main()