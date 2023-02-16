import requests
from lxml import etree


def connect(stuId:str, pwd:str):

    url = "http://10.255.248.9/webauth.do?wlanacname=WJ-BRAS-Main"

    payload = f'pageid=164&userId={stuId}&passwd={pwd}'
    headers = {
      'Origin': 'http://10.255.248.9'
      'Content-Type': 'application/x-www-form-urlencoded'
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    h = etree.HTML(response.text)
    msg = '  '.join(h.xpath('//div[@class="succ-content"]/p/text()'))
    print(msg)
    if '内网认证成功外网失败' in msg:
        dis_connect()


def dis_connect():

    url = "http://10.255.248.9/webdisconn.do?wlanacname=yatelcom"

    payload = 'distoken=94f8e2e14775dee1376db5053aa8472a'
    headers = {
        'Origin': 'http://10.255.248.9',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        }

    response = requests.request("POST", url, headers=headers, data=payload)

    h = etree.HTML(response.text)
    print('返回消息:', ''.join(h.xpath('//span[@id="command.errors"]/text()')))


def is_online():
    url = 'https://www.baidu.com'

    try:
        a = requests.get(url, timeout=3)
        if a.status_code == 200:
            return True
        else:
            return False
    except :
        return False


if __name__ == '__main__':
    stuId = '校园网登录账号'
    pwd = '密码'
    while True:
        if is_online():
            print('无需连接网络...')
            break
        else:
            print('正在尝试连接校园网...')
            try:
                connect(stuId, pwd)
            except:
                print('检查网络是否连接正确后，重试!')
