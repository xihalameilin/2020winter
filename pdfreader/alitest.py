import urllib.request
import urllib.parse
import json
import time
import base64

# 本地图片
image_path = '2.png'

with open(image_path, 'rb') as f:  # 以二进制读取本地图片
    data = f.read()
    encodestr = str(base64.b64encode(data), 'utf-8') # base64编码图片
# 请求头
headers = {
         'Authorization': ' aa3ac11f7b624e539fbaffb4588275c7 ',  # APPCODE +你的appcod,一定要有空格！！！
         'Content-Type': 'application/json; charset=UTF-8'         # 根据接口的格式来
    }

def posturl(url,data={}):
    try:
        params=json.dumps(dict).encode(encoding='UTF8')
        req = urllib.request.Request(url, params, headers)
        r = urllib.request.urlopen(req)
        html =r.read()
        r.close()
        return html.decode("utf8")
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))
    time.sleep(1)


if __name__=="__main__":

    url_request = "https://form.market.alicloudapi.com/api/predict/ocr_table_parse"   # 对照官网API改
    dict = {'img': encodestr}
    html = posturl(url_request, data=dict)
    print('识别的结果：', html)