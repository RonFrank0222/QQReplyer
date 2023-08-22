import json,requests,re,urllib
from characterai import PyCAI


def ownthink(msg):
    url = 'https://api.ownthink.com/bot?spoken={}'.format(urllib.parse.quote(msg))
    html = requests.get(url)
    return html.json()["data"]['info']['text']

def send(uid,nickname,msg):
    requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid,msg),params={"param":1},headers={"Connection":"close"})

def deal(uid,nickname,msg,ai=1):
    if ai:
        msg=ownthink(msg)
        send(uid,nickname,msg)
    else:
        send(uid,nickname,msg)