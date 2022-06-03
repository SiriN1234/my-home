from flask import Blueprint
from flask import Flask, request, jsonify

blue_main_menu = Blueprint("main_menu", __name__, url_prefix="/main_menu")

@blue_main_menu.route("/")
def main_menu_check():
    return "main_menu"

@blue_main_menu.route("/main", methods=['POST'])
def main_menu_1():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])
    
    res = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "basicCard": {
          "title": "메인메뉴",
          "description": "원하는 메뉴를 선택해주세요.",
          "thumbnail": {
            "imageUrl": ""
          },
          "profile": {
            "imageUrl": "",
            "nickname": "메인메뉴"
          },
          "buttons": [
            {
              "label": "주택복지 목록 보기",
              "action": "block",
              "blockId": "62946175fab76c716dbf502e?scenarioId=629460c7890e4a16d6ad4591"
            },
            {
              "label": "공공주택 공고 보기",
              "action": "block",
              "blockId": "6299b98eab89e678ee86d591?scenarioId=6299b966ab89e678ee86d58a"
            }
            
          ]
        }
      }
    ]
  }
}
    return jsonify(res)