import execjs
import requests

with open('exbaidu.js') as f:
    js = f.read()

sign = execjs.compile(js)
print(sign.call('get_sign','tree'))