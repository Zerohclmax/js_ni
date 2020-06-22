import time
import random
import hashlib
import requests


class Ydspider:
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.head = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '236',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=1695451255@10.108.160.18; OUTFOX_SEARCH_USER_ID_NCOO=1704931666.0429537; _ga=GA1.2.1690161787.1590836536; JSESSIONID=aaajPlrY8tzie5ri6HBlx; ___rl__test__cookies=1592822724102',
            'Host': 'fanyi.youdao.com',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',

        }

    def get_ts_salt_sign(self, word):
        ts = str(int(time.time() * 1000))
        salt = ts + str(random.randint(0, 9))
        string = "fanyideskweb{}{}mmbP%A-r6U3Nw(n]BjuEU"
        sign = hashlib.md5(string.format(word, salt).encode()).hexdigest()
        data = {
            'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'ts': ts,
            'bv': 'a9c3483a52d7863608142cc3f302a0ba',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        return data

    def req_transale(self, data):
        html = requests.post(url=self.url, headers=self.head, data=data).json()
        return html
    def parse_html(self, html):
        data=html['translateResult'][0][0]
        tgt = data['tgt']
        src = data['src']
        print("您要翻译的单词是："+src)
        print("翻译结果是："+tgt)
    def main(self, word):
        data = self.get_ts_salt_sign(word)
        html = self.req_transale(data)
        self.parse_html(html)


if __name__ == '__main__':
    spiders = Ydspider()
    spiders.main('')
