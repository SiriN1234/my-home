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
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
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
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
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
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
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
            "blockId": "627b293404a7d7314aeb7b0d"
        }
        ]
        }
    }

    return responseBody