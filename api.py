import json,requests,re,urllib
from characterai import PyCAI

from transformers import AutoTokenizer, AutoModel

def chatglm(msg):
    tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
    model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().cuda()
    model = model.eval()
    response, history = model.chat(tokenizer,msg,history=[])

def ownthink(msg):
    url = 'https://api.ownthink.com/bot?spoken={}'.format(urllib.parse.quote(msg))
    html = requests.get(url)
    return html.json()["data"]['info']['text']

def send(uid,nickname,msg):
    requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid,msg),params={"param":1},headers={"Connection":"close"})

def getai(ainame,msg):
    if ainame=="chatglm":
        return chatglm(msg)
    elif ainame=="ownthink":
        return ownthink(msg)

def deal(uid,nickname,msg,ai=""):
    if ai!="":
        msg=getai(ai,msg)
        send(uid,nickname,msg)
    else:
        send(uid,nickname,msg)