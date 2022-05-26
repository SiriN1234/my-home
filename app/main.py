from flask import Flask, request, Blueprint
import json
import pandas as pd
import csv
import random

from app import test_text as tt

from . import bl_test
from . import region_list

app = Flask(__name__)

# 지역별 임대주택 목록 출력
app.register_blueprint(region_list.app)





# 헬로우 월드
@app.route('/')
def hello_world():
    return 'Hello, World!'




# 연습/테스트

# 블루프린트 테스트
app.register_blueprint(bl_test.app)

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




# test1
def test_text() :
    a = "test1"
    return a

@app.route('/api/test1', methods=['POST'])
def test1():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": test_text()
                    }
                }
            ]
        }
    }

    return responseBody




# 다른 파이썬 파일에서 함수 호출 연습
@app.route('/api/test2', methods=['POST'])
def test2():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": tt.pt()
                    }
                }
            ]
        }
    }

    return responseBody




# 카드, 블록 연결 연습
@app.route('/api/test3', methods=['POST'])
def test3():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
        {
            "basicCard": {
            "title": "타이틀",
            "description": "왼쪽을 누르면 텍스트를 반환, 오른쪽을 누르면 링크 연결",
            "thumbnail": {
                "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
            },
            "buttons": [
            {
                "action": "block",
                "label": "텍스트",
                "blockId": "6285ee1475eca02fba63ce07?scenarioId=627b131e9ac8ed7844165d72"
            },
            {
                "action":  "webLink",
                "label": "링크",
                "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
            }
          ]
        }
      }
    ]
  }
}

    return responseBody





# 카카오톡 케로셀 카드 테스트
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
                        "description": "2022년 특화형 전세임대 청년 기숙사형(경희대) 입주자 정기모집 공고\n공급유형 : 전세임대\n공고일자 : 2022-05-10",
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11335"
                            }
                        ]
                    },
                    {
                        "description": "『도봉구 신혼부부 맞춤형 공공임대주택 (공동체주택)』입주자 추가모집 공고\n공급유형 : 매입임대\n공고일자 : 2022-05-06",
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11291"
                            }
                        ]
                    },
                    {
                        "description": "은평구 청년 창업인의 집 1호점 및 2호점 (수요자맞춤형 주택) 입주자 모집 공고\n공급유형 : 매입임대\n공고일자 : 2022-05-04",
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11290"
                            }
                        ]
                    },
                    {
                        "description": "2022 다자녀 전세임대 1순위 입주자 모집 공고\n공급유형 : 전세임대\n공고일자 : 2022-05-02",
                        "thumbnail": {
                            "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrLYeHWqhyQqNbQQCwa93FAFp7NgR-zLXwug&usqp=CAU"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11272"
                            }
                        ]
                    }
                ]
            }
        }
        ],
        "quickReplies": [
        {
            "label": "메인으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody



