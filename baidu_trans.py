import requests

class Baidusper:
    def __init__(self):
        self.sign_url= 'http://127.0.0.1:3000/get_sign'
        self.url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
        self.head={
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'content-length': '135',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': 'BIDUPSID=C29888BCDFF422372481AFCF6980C120; PSTM=1584162176; BAIDUID=C29888BCDFF422374D21D00AE176E632:SL=0:NR=10:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1592825921,1592825932; H_PS_PSSID=32099_1438_21125_31660_32045_31845_22157; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1592830631; __yjsv5_shitong=1.0_7_ed025362778e6a24d86613f7e9bc1d702059_300_1592830630755_116.136.20.144_4da0744a; yjs_js_security_passport=581b6b54d9a9703b51a44b6fafb691d0b1059567_1592830631_j',
            'origin': 'https://fanyi.baidu.com',
            'referer': 'https://fanyi.baidu.com/?aldtype=16047',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.44',
            'x-requested-with': 'XMLHttpRequest',
        }

    def get_data(self,word):
        datar={'word': word}
        sign = requests.post(url=self.sign_url,data=datar).text
        data = {
            'from': 'en',
            'to': 'zh',
            'query': word,
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': sign,
            'token': '1483eb30d68d5194910409fcddf49304',
            'domain': 'common',
        }
        print(sign)
        return data
    def req_trans(self,data):
        html = requests.post(url=self.url,headers=self.head,data=data).json()
        return html
    def parse_html(self,html):
        data = html['trans_result']['data'][0]
        dst = data['dst']
        print(dst)

    def main(self,word):
        data = self.get_data(word)
        html = self.req_trans(data)
        self.parse_html(html)
if __name__ == '__main__':
    spider=Baidusper()
    spider.main('boot')
