from flask import Flask
from flask import request
from flask import render_template
from flask import make_response, redirect, url_for
from flask import jsonify
from werkzeug.utils import secure_filename
from os import path
import json
import datetime

import shisanshui

app = Flask(__name__)

wsgi_app = app.wsgi_app

def stringtoimage(card_string):
    card_list = card_string.split(" ")
    card_name_list =[]
    for item in card_list:
        cardname = ""
        if(item[0] == '#'):
            cardname = "c_fangkuai"
        elif(item[0] == '*'):
            cardname = "c_meihua"
        elif(item[0] == '$'):
            cardname = "c_heitao"
        else:
            cardname = "c_hongxin"
        cardname = cardname + item[1:] + ".png"
        card_name_list.append(cardname)
    return card_name_list

@app.route('/')
@app.route('/index')
def home():
    message = {"flag":"hello world!"}
    return json.dumps(message,ensure_ascii=False)


 #图片上传函数
@app.route("/card_division",methods=['GET','POST'])
def card_division():     
    message = {
        "card":[
            "123",
            "456",
            "789"
        ],
        "card_image":[
            [],
            [],
            []
        ]
    }
    card_string = []
    json_data = request.get_json()
    print(json_data)
    print(json_data["cardstring"])
    card_string = json_data["cardstring"]
    message["card"] = shisanshui.main_function(card_string)
    message["card_image"][0] = stringtoimage(message["card"][0]) 
    message["card_image"][1] = stringtoimage(message["card"][1]) 
    message["card_image"][2] = stringtoimage(message["card"][2]) 
    return json.dumps(message,ensure_ascii=False) 


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=8080)    #外网访问，端口号为8080
