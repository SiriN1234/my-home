from flask import Flask, request
import json
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello, World!'


# 카카오톡 텍스트형 응답
@app.route('/api/test', methods=['POST'])
def test():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "안녕하세요? 테스트 메세지입니다."
                    }
                }
            ]
        }
    }

    return responseBody


# 카카오톡 카드 테스트
@app.route('/api/cardTest', methods=['POST'])
def cardTest():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "title": "보물상자",
                        "description": "보물상자 안에는 뭐가 있을까",
                        "thumbnail": {
                            "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                        },
                        "buttons": [
                            {
                                "action": "message",
                                "label": "열어보기",
                                "messageText": "짜잔! 우리가 찾던 보물입니다"
                            },
                            {
                                "action":  "webLink",
                                "label": "구경하기",
                                "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                            }
                        ]
                    },
                    {
                        "title": "보물상자2",
                        "description": "보물상자2 안에는 뭐가 있을까",
                        "thumbnail": {
                            "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                        },
                        "buttons": [
                            {
                                "action": "message",
                                "label": "열어보기",
                                "messageText": "짜잔! 우리가 찾던 보물입니다"
                            },
                            {
                                "action":  "webLink",
                                "label": "구경하기",
                                "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                            }
                        ]
                    },
                    {
                        "title": "보물상자3",
                        "description": "보물상자3 안에는 뭐가 있을까",
                        "thumbnail": {
                            "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                        },
                        "buttons": [
                            {
                                "action": "message",
                                "label": "열어보기",
                                "messageText": "짜잔! 우리가 찾던 보물입니다"
                            },
                            {
                                "action":  "webLink",
                                "label": "구경하기",
                                "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                            }
                        ]
                    }
                ]
            }
        }
        ]
        }
    }

    return responseBody