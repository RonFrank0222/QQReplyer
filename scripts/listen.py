from flask import Flask,request
from os import system
import api

app=Flask(__name__)

@app.route("/",methods=["POST"])#监听端口
def listen():
    uid="2978643621"
    nickname="ron"
    if request.get_json().get("message_type")=="private":
        msg=request.get_json().get("raw_message")#原始信息
        uid=request.get_json().get("sender").get("user_id")#QQ号
        nickname=request.get_json().get("sender").get("nickname")#昵称
        api.atri(uid,msg)
    if request.get_json().get("message_type")=="group":
        api.deal(uid,nickname,"group",0)
    
    return "Done"

if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1",port=8000)