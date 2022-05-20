from flask import Flask, request
import json

from app import test_text as tt


import pandas as pd
import csv




app = Flask(__name__)



# 헬로우 월드 
@app.route('/')
def hello_world():
    return 'Hello, World!'





# 연습/테스트

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
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody







###################################################################
# description : 카드에 들어갈 텍스트
# thumbnail(필수) : 카드에 들어갈 이미지
# buttons : 카드 밑에 들어가는 버튼
## action : message 또는 webLink
## label : 버튼에 들어가는 텍스트
## webLinkUrl : 버튼 누르면 연결되는 웹페이지 주소

# quickReplies : 바로 연결 버튼
## action : message 또는 block
## blockId : action이 block일 때 넣는 값

# 블록ID 보는 방법
# 오픈빌더에서 해당 블록에 들어간 후 주소를 보면 중간에 /intent/가 있음
# 그 뒤의 값이 블록ID
###################################################################




# 임대주택 목록 출력하는 카드
# 1p 서울, 경기, 인천, 대전, 세종, 부산, 울산, 대구, 광주
# 2p 강원도, 충청남도, 충청북도, 경상남도, 경상북도, 전라남도, 전라북도, 제주특별자치도

# 서울시 임대주택 목록
@app.route('/api/seoul', methods=['POST'])
def seoul():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    # csv 파일 불러오기
    seoul_notice = pd.read_csv("./app/data/Seoul_notice.csv")
    seoul_url = pd.read_csv("./app/data/Seoul_url.csv")

    # 값을 넣을 배열 선언
    seoul_notice_arr = [] # description에 들어갈 값
    seoul_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        seoul_url_arr.append(seoul_url.iloc[i]['url'])
        seoul_notice_arr.append(seoul_notice.iloc[i]['name'] + "\n공급유형 : " + seoul_notice.iloc[i]['title'] + "\n공고일자 : " + seoul_notice.iloc[i]['re_date'])

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "description": seoul_notice_arr[0],
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": seoul_url_arr[0]
                            }
                        ]
                    },
                    {
                        "description": seoul_notice_arr[1],
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": seoul_url_arr[1]
                            }
                        ]
                    },
                    {
                        "description": seoul_notice_arr[2],
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": seoul_url_arr[2]
                            }
                        ]
                    },
                    {
                        "description": seoul_notice_arr[3],
                        "thumbnail": {
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": seoul_url_arr[3]
                            }
                        ]
                    },
                    {
                        "description": seoul_notice_arr[4],
                        "thumbnail": {
                            "imageUrl": "https://cdn.eroun.net/news/photo/201811/3955_16392_146.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": seoul_url_arr[4]
                            }
                        ]
                    },
                    {
                        "description": seoul_notice_arr[5],
                        "thumbnail": {
                            "imageUrl": "http://newsroom.etomato.com/userfiles/suwon%20kwonsun.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": seoul_url_arr[5]
                            }
                        ]
                    },
                    {
                        "description": seoul_notice_arr[6],
                        "thumbnail": {
                            "imageUrl": "https://post-phinf.pstatic.net/MjAyMTA2MDRfMTY2/MDAxNjIyNzkxODYwMzI4.I0nOP1lyXNA2J-so9L1dmQ4W0L8L3j4n3IHI35--6RMg.S1vc0fkJloQLMbD9FQHIrn2vHgJgiy0CsoC6Stth7Vcg.JPEG/1.JPG?type=w1200"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": seoul_url_arr[6]
                            }
                        ]
                    },
                    {
                        "description": seoul_notice_arr[7],
                        "thumbnail": {
                            "imageUrl": "https://img.sbs.co.kr/newimg/news/20220316/201647138_1280.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": seoul_url_arr[7]
                            }
                        ]
                    },
                    {
                        "description": seoul_notice_arr[8],
                        "thumbnail": {
                            "imageUrl": "https://www.shinailbo.co.kr/news/photo/202104/1398185_608466_5339.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": seoul_url_arr[8]
                            }
                        ]
                    },
                    {
                        "description": seoul_notice_arr[9],
                        "thumbnail": {
                            "imageUrl": "https://mediahub.seoul.go.kr/uploads/mediahub/2022/04/xsGpaZKCJGgdCtbWtiUMtHADDDbAlizt.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": seoul_url_arr[9]
                            }
                        ]
                    }
                ]
            }
        }
        ],
        "quickReplies": [
        {
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        },
        {
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody



# 경기도 임대주택 목록
@app.route('/api/gyeonggiDo', methods=['POST'])
def gyeonggiDo():
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
                        "description": "[정정공고]화성시 지역 행복주택 입주자격완화 예비입주자 모집\n공급유형 : 행복주택\n공고일자 : 2022-05-13",
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11426"
                            }
                        ]
                    },
                    {
                        "description": "화성시 지역 행복주택 입주자격완화 예비입주자 모집\n공급유형 : 행복주택\n공고일자 : 2022-05-13",
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11351"
                            }
                        ]
                    },
                    {
                        "description": "파주운정3 A34블록 영구임대주택 추가 및 예비입주자모집공고(22.05.13)\n공급유형 : 영구임대\n공고일자 : 2022-05-13",
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11349"
                            }
                        ]
                    },
                    {
                        "description": "화성봉담2 A-2블록 신혼희망타운 행복주택 입주자격완화 추가모집\n공급유형 : 행복주택\n공고일자 : 2022-05-12",
                        "thumbnail": {
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11346"
                            }
                        ]
                    },
                    {
                        "description": "2022년 경기도 시흥시 매입임대주택 입주자 선착순 수시모집\n공급유형 : 매입임대\n공고일자 : 2022-05-10",
                        "thumbnail": {
                            "imageUrl": "https://cdn.eroun.net/news/photo/201811/3955_16392_146.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11342"
                            }
                        ]
                    },
                    {
                        "description": "[오산시] 다가구 등 매입임대주택 예비입주자 모집 공고\n공급유형 : 매입임대\n공고일자 : 2022-05-10",
                        "thumbnail": {
                            "imageUrl": "http://newsroom.etomato.com/userfiles/suwon%20kwonsun.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11333"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고]평택시,안성시 국민임대 예비입주자 모집공고(22.05.06)\n공급유형 : 국민임대\n공고일자 : 2022-05-06",
                        "thumbnail": {
                            "imageUrl": "https://post-phinf.pstatic.net/MjAyMTA2MDRfMTY2/MDAxNjIyNzkxODYwMzI4.I0nOP1lyXNA2J-so9L1dmQ4W0L8L3j4n3IHI35--6RMg.S1vc0fkJloQLMbD9FQHIrn2vHgJgiy0CsoC6Stth7Vcg.JPEG/1.JPG?type=w1200"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11343"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고]2022년 5월 고양시 지역 행복주택 예비입주자 모집 공고\n공급유형 : 행복주택\n공고일자 : 2022-05-06",
                        "thumbnail": {
                            "imageUrl": "https://img.sbs.co.kr/newimg/news/20220316/201647138_1280.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11343"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고]파주시 행복주택 입주자격완화 예비자 모집공고(22.5.6)\n공급유형 : 행복주택\n공고일자 : 2022-05-06",
                        "thumbnail": {
                            "imageUrl": "https://www.shinailbo.co.kr/news/photo/202104/1398185_608466_5339.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11326"
                            }
                        ]
                    },
                    {
                        "description": "남양주시 지역 국민임대주택 예비입주자 모집\n공급유형 : 국민임대\n공급일자 : 2022-05-06",
                        "thumbnail": {
                            "imageUrl": "https://mediahub.seoul.go.kr/uploads/mediahub/2022/04/xsGpaZKCJGgdCtbWtiUMtHADDDbAlizt.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11320"
                            }
                        ]
                    }
                ]
            }
        }
        ],
        "quickReplies": [
        {
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        },
        {
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody



# 인천 임대주택 목록
@app.route('/api/incheon', methods=['POST'])
def incheon():
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
                        "description": "동인천역 파크푸르지오 공공임대주택(10년) 지구주민 우선공급 입주자모집 공고\n공급유형 : 10년임대\n공고일자 : 2022-05-13",
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11355"
                            }
                        ]
                    },
                    {
                        "description": "동인천역 파크푸르지오 영구 임대주택 지구주민 우선공급 입주자모집 공고\n공급유형 : 영구임대\n공고일자 : 2022-05-13",
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11354"
                            }
                        ]
                    },
                    {
                        "description": "행복주택(부평우민늘푸른) 예비입주자 모집공고(22.05.09공고)\n공급유형 : 행복주택\n공고일자 : 2022-05-09",
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11327"
                            }
                        ]
                    },
                    {
                        "description": "인천시[북서권] 국민임대주택 예비입주자 모집 공고(2022.05.06)\n공급유형 : 국민임대\n공고일자 : 2022-05-06",
                        "thumbnail": {
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11304"
                            }
                        ]
                    },
                    {
                        "description": "22년 5월 인천지역(남동구, 중구) 국민임대주택 예비입주자 모집\n공급유형 : 국민임대\n공고일자 : 2022-05-06",
                        "thumbnail": {
                            "imageUrl": "https://cdn.eroun.net/news/photo/201811/3955_16392_146.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11303"
                            }
                        ]
                    },
                    {
                        "description": "인천논현2단지 국민임대주택 예비입주자 모집 공고\n공급유형 : 국민임대\n공고일자 : 2022-05-06",
                        "thumbnail": {
                            "imageUrl": "http://newsroom.etomato.com/userfiles/suwon%20kwonsun.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11292"
                            }
                        ]
                    },
                    {
                        "description": "인천삼산4단지 국민임대주택 예비입주자 모집\n공급유형 : 국민임대\n공고일자 : 2022-05-06",
                        "thumbnail": {
                            "imageUrl": "https://post-phinf.pstatic.net/MjAyMTA2MDRfMTY2/MDAxNjIyNzkxODYwMzI4.I0nOP1lyXNA2J-so9L1dmQ4W0L8L3j4n3IHI35--6RMg.S1vc0fkJloQLMbD9FQHIrn2vHgJgiy0CsoC6Stth7Vcg.JPEG/1.JPG?type=w1200"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11292"
                            }
                        ]
                    },
                    {
                        "description": "2022 다자녀 전세임대 1순위 입주자 모집 공고\n공급유형 : 전세임대\n공고일자 : 2022-05-02",
                        "thumbnail": {
                            "imageUrl": "https://img.sbs.co.kr/newimg/news/20220316/201647138_1280.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11272"
                            }
                        ]
                    },
                    {
                        "description": "2022년 신혼부부 전세임대Ⅱ 입주자 수시모집(자격완화) 공고\n공급유형 : 전세임대\n공고일자 : 2022-04-25",
                        "thumbnail": {
                            "imageUrl": "https://www.shinailbo.co.kr/news/photo/202104/1398185_608466_5339.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11207"
                            }
                        ]
                    },
                    {
                        "description": "2022년 신혼부부 전세임대Ⅰ입주자 수시모집(자격완화) 공고\n공급유형 : 전세임대\n공고일자 : 2022-04-25",
                        "thumbnail": {
                            "imageUrl": "https://mediahub.seoul.go.kr/uploads/mediahub/2022/04/xsGpaZKCJGgdCtbWtiUMtHADDDbAlizt.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11206"
                            }
                        ]
                    }
                ]
            }
        }
        ],
        "quickReplies": [
        {
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        },
        {
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody



# 대전 임대주택 목록
@app.route('/api/daejeon', methods=['POST'])
def daejeon():
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
                        "description": "대전광역시 국민임대주택 예비입주자 모집공고(공고일:2022.05.16)\n공급유형 : 국민임대\n공고일자 : 2022-05-16",
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11413"
                            }
                        ]
                    },
                    {
                        "description": "대전천동3 5블록 10년 분양전환공공임대주택 지구주민(2,3순위) 우선공급 입주자모집공고\n공급유형 : 10년임대\n공고일자 : 2022-05-06",
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11298"
                            }
                        ]
                    },
                    {
                        "description": "2022 다자녀 전세임대 1순위 입주자 모집 공고\n공급유형 : 전세임대\n공고일자 : 2022-05-02",
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11272"
                            }
                        ]
                    },
                    {
                        "description": "2022년 신혼부부 전세임대Ⅱ 입주자 수시모집(자격완화) 공고\n공급유형 : 전세임대\n공고일자 : 2022-04-25",
                        "thumbnail": {
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11207"
                            }
                        ]
                    },
                    {
                        "description": "2022년 신혼부부 전세임대Ⅰ입주자 수시모집(자격완화) 공고\n공급유형 : 전세임대\n\공고일자 : 2022-04-25",
                        "thumbnail": {
                            "imageUrl": "https://cdn.eroun.net/news/photo/201811/3955_16392_146.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11206"
                            }
                        ]
                    },
                    {
                        "description": "대전도시공사 매입임대주택 상시모집 공고\n공급유형 : 매입임대\n공고일자 : 2022-04-25",
                        "thumbnail": {
                            "imageUrl": "http://newsroom.etomato.com/userfiles/suwon%20kwonsun.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11219"
                            }
                        ]
                    },
                    {
                        "description": "2022년 청년 매입임대주택 선착순 입주자 모집 공고\n공급유형 : 매입임대\n공고일자 : 2022-04-18",
                        "thumbnail": {
                            "imageUrl": "https://post-phinf.pstatic.net/MjAyMTA2MDRfMTY2/MDAxNjIyNzkxODYwMzI4.I0nOP1lyXNA2J-so9L1dmQ4W0L8L3j4n3IHI35--6RMg.S1vc0fkJloQLMbD9FQHIrn2vHgJgiy0CsoC6Stth7Vcg.JPEG/1.JPG?type=w1200"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11107"
                            }
                        ]
                    },
                    {
                        "description": "2022년 청년 매입임대주택 예비입주자 모집공고\n공급유형 : 매입임대\n공고일자 : 2022-04-04",
                        "thumbnail": {
                            "imageUrl": "https://img.sbs.co.kr/newimg/news/20220316/201647138_1280.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11057"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고]2022년 청년 전세임대 1순위 입주자 수시모집\n공급유형 : 전세임대\n공고일자 : 2022-01-14",
                        "thumbnail": {
                            "imageUrl": "https://www.shinailbo.co.kr/news/photo/202104/1398185_608466_5339.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11205"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고][정정공고][전국] 자립준비청년(보호종료아동) 매입임대 입주자 수시모집 공고	\n공급유형 : 매입임대\n공고일자 : 2022-01-14",
                        "thumbnail": {
                            "imageUrl": "https://mediahub.seoul.go.kr/uploads/mediahub/2022/04/xsGpaZKCJGgdCtbWtiUMtHADDDbAlizt.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=10955"
                            }
                        ]
                    }
                ]
            }
        }
        ],
        "quickReplies": [
        {
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        },
        {
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody




# 세종특별자치시 임대주택 목록
@app.route('/api/saejong', methods=['POST'])
def saejong():
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
                        "description": "2022 다자녀 전세임대 1순위 입주자 모집 공고\n공급유형 : 전세임대\n공고일자 : 2022-05-02",
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11272"
                            }
                        ]
                    },
                    {
                        "description": "전의면 사랑의 집(영구임대주택) 예비입주자 모집 공고\n공급유형 : 영구임대\n공고일자 :2022-03-08",
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=10807"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고]2022년 청년 전세임대 1순위 입주자 수시모집\n공급유형 : 전세임대\n공고일자 :2022-01-14",
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11205"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고][정정공고][전국] 자립준비청년(보호종료아동) 매입임대 입주자 수시모집 공고\n공급유형 : 매입임대\n공고일자 :2022-01-14",
                        "thumbnail": {
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=10955"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고]2022년 청년 전세임대 1순위 입주자 수시모집\n공급유형 : 전세임대\n공고일자 : 2022-01-14",
                        "thumbnail": {
                            "imageUrl": "https://cdn.eroun.net/news/photo/201811/3955_16392_146.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=10768"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고]2022년 신혼부부 전세임대Ⅱ 입주자 수시모집 공고\n공급유형 : 전세임대\n공고일자 : 2022-01-14",
                        "thumbnail": {
                            "imageUrl": "http://newsroom.etomato.com/userfiles/suwon%20kwonsun.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=10767"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고]2022년 신혼부부 전세임대Ⅰ 입주자 수시모집 공고\n공급유형 : 전세임대\n공고일자 : 2022-01-14",
                        "thumbnail": {
                            "imageUrl": "https://post-phinf.pstatic.net/MjAyMTA2MDRfMTY2/MDAxNjIyNzkxODYwMzI4.I0nOP1lyXNA2J-so9L1dmQ4W0L8L3j4n3IHI35--6RMg.S1vc0fkJloQLMbD9FQHIrn2vHgJgiy0CsoC6Stth7Vcg.JPEG/1.JPG?type=w1200"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=10766"
                            }
                        ]
                    },
                    {
                        "description": "22022년 신혼부부 전세임대Ⅰ 입주자 수시모집 공고\n공급유형 : 전세임대\n공고일자 : 2022-01-14",
                        "thumbnail": {
                            "imageUrl": "https://img.sbs.co.kr/newimg/news/20220316/201647138_1280.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=10644"
                            }
                        ]
                    },
                    {
                        "description": "2022년 청년 전세임대 1순위 입주자 수시모집\n공급유형 : 전세임대\n공고일자 : 2022-01-14",
                        "thumbnail": {
                            "imageUrl": "https://www.shinailbo.co.kr/news/photo/202104/1398185_608466_5339.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=10643"
                            }
                        ]
                    },
                    {
                        "description": "2022년 신혼부부 전세임대Ⅱ 입주자 수시모집 공고\n공급유형 : 전세임대\n공고일자 : 2022-01-14",
                        "thumbnail": {
                            "imageUrl": "https://mediahub.seoul.go.kr/uploads/mediahub/2022/04/xsGpaZKCJGgdCtbWtiUMtHADDDbAlizt.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=10642"
                            }
                        ]
                    }
                ]
            }
        }
        ],
        "quickReplies": [
        {
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        },
        {
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody



# 부산 임대주택 목록
@app.route('/api/busan', methods=['POST'])
def busan():
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
                        "description": "부산광역시 지역 국민임대주택 예비입주자 모집 공고(2022.05.16)\n공급유형 : 국민임대\n공고일자 : 2022-05-16",
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11385"
                            }
                        ]
                    },
                    {
                        "description": "부산연산2 행복주택 입주자 추가모집\n공급유형 : 행복주택\n공고일자 : 2022-05-10",
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11338"
                            }
                        ]
                    },
                    {
                        "description": "집주인 임대주택 입주자 수시모집 공고(부산 금정구 삼한골든뷰)\n공급유형 : 매입임대\n공고일자 : 2022-05-10",
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11334"
                            }
                        ]
                    },
                    {
                        "description": "부산동부권 해운대구 매입임대주택 예비입주자 모집\n공급유형 : 매입임대\n공고일자 : 2022-05-06",
                        "thumbnail": {
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11297"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고][부산울산] 2022년 기존주택 등 매입임대주택 예비입주자 모집\m공급유형 : 매입임대\m공고일자 : 2022-05-04",
                        "thumbnail": {
                            "imageUrl": "https://cdn.eroun.net/news/photo/201811/3955_16392_146.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11345"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고][부산울산] 2022년 기존주택 등 매입임대주택 예비입주자 모집\n공급유형 : 매입임대\n공고일자 : 2022-05-04",
                        "thumbnail": {
                            "imageUrl": "http://newsroom.etomato.com/userfiles/suwon%20kwonsun.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11332"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고][부산울산] 2022년 기존주택 등 매입임대주택 예비입주자 모집\n공급유형 : 매입임대\n공고일자 : 2022-05-04",
                        "thumbnail": {
                            "imageUrl": "https://post-phinf.pstatic.net/MjAyMTA2MDRfMTY2/MDAxNjIyNzkxODYwMzI4.I0nOP1lyXNA2J-so9L1dmQ4W0L8L3j4n3IHI35--6RMg.S1vc0fkJloQLMbD9FQHIrn2vHgJgiy0CsoC6Stth7Vcg.JPEG/1.JPG?type=w1200"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11325"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고][부산울산] 2022년 기존주택 등 매입임대주택 예비입주자 모집\n공급유형 : 매입임대\n공고일자 : 2022-05-04",
                        "thumbnail": {
                            "imageUrl": "https://img.sbs.co.kr/newimg/news/20220316/201647138_1280.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11321"
                            }
                        ]
                    },
                    {
                        "description": "[부산울산] 2022년 기존주택 등 매입임대주택 예비입주자 모집\n공급유형 : 매입임대\n공고일자 : 2022-05-04",
                        "thumbnail": {
                            "imageUrl": "https://www.shinailbo.co.kr/news/photo/202104/1398185_608466_5339.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11289"
                            }
                        ]
                    },
                    {
                        "description": "2022 다자녀 전세임대 1순위 입주자 모집 공고\n공급유형 : 전세임대\n공고일자 : 2022-05-02",
                        "thumbnail": {
                            "imageUrl": "https://mediahub.seoul.go.kr/uploads/mediahub/2022/04/xsGpaZKCJGgdCtbWtiUMtHADDDbAlizt.png"
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
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        },
        {
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody



# 울산 임대주택 목록
@app.route('/api/ulsan', methods=['POST'])
def ulsan():
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
                        "description": "울산광역시 지역 국민임대주택 예비입주자 모집공고(2022.05.16)\n공급유형 : 국민임대\n공고일자 : 2022-05-16",
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11383"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고][부산울산] 2022년 기존주택 등 매입임대주택 예비입주자 모집\n공급유형 : 매입임대\n공고일자 : 2022-05-04",
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11345"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고][부산울산] 2022년 기존주택 등 매입임대주택 예비입주자 모집\n공급유형 : 매입임대\n공고일자 : 2022-05-04",
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11332"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고][부산울산] 2022년 기존주택 등 매입임대주택 예비입주자 모집\n공급유형 : 매입임대\n공고일자 : 2022-05-04",
                        "thumbnail": {
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11325"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고][부산울산] 2022년 기존주택 등 매입임대주택 예비입주자 모집\n공급유형 : 매입임대\n공고일자 : 2022-05-04",
                        "thumbnail": {
                            "imageUrl": "https://cdn.eroun.net/news/photo/201811/3955_16392_146.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11321"
                            }
                        ]
                    },
                    {
                        "description": "[부산울산] 2022년 기존주택 등 매입임대주택 예비입주자 모집\n공급유형 : 매입임대\n공고일자 : 2022-05-04",
                        "thumbnail": {
                            "imageUrl": "http://newsroom.etomato.com/userfiles/suwon%20kwonsun.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11289"
                            }
                        ]
                    },
                    {
                        "description": "2022 다자녀 전세임대 1순위 입주자 모집 공고\n공급유형 : 전세임대\n공고일자 : 2022-05-02",
                        "thumbnail": {
                            "imageUrl": "https://post-phinf.pstatic.net/MjAyMTA2MDRfMTY2/MDAxNjIyNzkxODYwMzI4.I0nOP1lyXNA2J-so9L1dmQ4W0L8L3j4n3IHI35--6RMg.S1vc0fkJloQLMbD9FQHIrn2vHgJgiy0CsoC6Stth7Vcg.JPEG/1.JPG?type=w1200"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11272"
                            }
                        ]
                    },
                    {
                        "description": "문수데시앙2단지 10년공공임대주택(59A) 예비입주자 모집 공고\n공급유형 : 10년임대\n공고일자 : 2022-04-29",
                        "thumbnail": {
                            "imageUrl": "https://img.sbs.co.kr/newimg/news/20220316/201647138_1280.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11243"
                            }
                        ]
                    },
                    {
                        "description": "2022년 신혼부부 전세임대Ⅱ 입주자 수시모집(자격완화) 공고\n공급유형 : 전세임대\n공고일자 : 2022-04-25",
                        "thumbnail": {
                            "imageUrl": "https://www.shinailbo.co.kr/news/photo/202104/1398185_608466_5339.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11207"
                            }
                        ]
                    },
                    {
                        "description": "2022년 신혼부부 전세임대Ⅰ입주자 수시모집(자격완화) 공고\n공급유형 : 전세임대\n공고일자 : 2022-04-25",
                        "thumbnail": {
                            "imageUrl": "https://mediahub.seoul.go.kr/uploads/mediahub/2022/04/xsGpaZKCJGgdCtbWtiUMtHADDDbAlizt.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11206"
                            }
                        ]
                    }
                ]
            }
        }
        ],
        "quickReplies": [
        {
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        },
        {
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody




# 대구 임대주택 목록
@app.route('/api/daegu', methods=['POST'])
def daegu():
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
                        "description": "대구금호(1,5,8단지) 및 대구남산 국민임대주택 예비입주자 모집공고\n공급유형 : 국민임대\n공고일자 : 2022-05-16",
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11384"
                            }
                        ]
                    },
                    {
                        "description": "대구도시공사 수성알파시티 행복주택 예비입주자 모집\n공급유형 : 행복주택\n공고일자 : 2022-05-16",
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11353"
                            }
                        ]
                    },
                    {
                        "description": "대구북부권주거복지지사 기존주택 등 매입임대주택 입주자 모집\n공급유형 : 매입임대\n공고일자 : 2022-05-13",
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11350"
                            }
                        ]
                    },
                    {
                        "description": "대구대곡 천년나무 행복주택 입주자 모집공고\n공급유형 : 행복주택\n공고일자 : 2022-05-11",
                        "thumbnail": {
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11344"
                            }
                        ]
                    },
                    {
                        "description": "[경북 경산, 대구 동구_수성구] 신혼(혼인)부부매입임대주택II(전세형) 입주자격완화 추가 모집공고\n공급유형 : 매입임대\n공고일자 : 2022-05-06",
                        "thumbnail": {
                            "imageUrl": "https://cdn.eroun.net/news/photo/201811/3955_16392_146.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11295"
                            }
                        ]
                    },
                    {
                        "description": "2022 다자녀 전세임대 1순위 입주자 모집 공고\n공급유형 : 전세임대\n공고일자 : 2022-05-02",
                        "thumbnail": {
                            "imageUrl": "http://newsroom.etomato.com/userfiles/suwon%20kwonsun.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11272"
                            }
                        ]
                    },
                    {
                        "description": "2022년 신혼부부 전세임대Ⅱ 입주자 수시모집(자격완화) 공고\n공급유형 : 전세임대\n공고일자 : 2022-04-25",
                        "thumbnail": {
                            "imageUrl": "https://post-phinf.pstatic.net/MjAyMTA2MDRfMTY2/MDAxNjIyNzkxODYwMzI4.I0nOP1lyXNA2J-so9L1dmQ4W0L8L3j4n3IHI35--6RMg.S1vc0fkJloQLMbD9FQHIrn2vHgJgiy0CsoC6Stth7Vcg.JPEG/1.JPG?type=w1200"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11207"
                            }
                        ]
                    },
                    {
                        "description": "2022년 신혼부부 전세임대Ⅰ입주자 수시모집(자격완화) 공고\n공급유형 : 전세임대\n공고일자 : 2022-04-25",
                        "thumbnail": {
                            "imageUrl": "https://img.sbs.co.kr/newimg/news/20220316/201647138_1280.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11206"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고]2022년 청년 전세임대 1순위 입주자 수시모집\n공급유형 : 전세임대\n공고일자 : 2022-01-14",
                        "thumbnail": {
                            "imageUrl": "https://www.shinailbo.co.kr/news/photo/202104/1398185_608466_5339.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11205"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고][정정공고][전국] 자립준비청년(보호종료아동) 매입임대 입주자 수시모집 공고\n공급유형 : 매입임대\n공고일자 : 2022-01-14",
                        "thumbnail": {
                            "imageUrl": "https://mediahub.seoul.go.kr/uploads/mediahub/2022/04/xsGpaZKCJGgdCtbWtiUMtHADDDbAlizt.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=10955"
                            }
                        ]
                    }
                ]
            }
        }
        ],
        "quickReplies": [
        {
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        },
        {
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody




# 광주 임대주택 목록
@app.route('/api/gwangju', methods=['POST'])
def gwangju():
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
                        "description": "광주송화3 국민임대주택 입주자격완화 예비입주자 모집(2022.05.17)\n공급유형 : 국민임대\n공고일자 : 2022-05-17",
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11432"
                            }
                        ]
                    },
                    {
                        "description": "광주광역시 국민임대주택 예비입주자 모집(2022.05.16)\n공급유형 : 국민임대\n공고일자 : 2022-05-16",
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11376"
                            }
                        ]
                    },
                    {
                        "description": "광주도산 행복주택 추가 입주자 모집(2022.05.09)\n공급유형 : 행복주택\n공고일자 : 2022-05-09",
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11328"
                            }
                        ]
                    },
                    {
                        "description": "광주광역시 광산구 신축다세대 임대주택 입주자 모집[자격완화 , 전세형]\n공급유형 : 10년임대\n공고일자 : 2022-05-04",
                        "thumbnail": {
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11286"
                            }
                        ]
                    },
                    {
                        "description": "2022 다자녀 전세임대 1순위 입주자 모집 공고\n공급유형 : 전세임대\n공고일자 : 2022-05-02",
                        "thumbnail": {
                            "imageUrl": "https://cdn.eroun.net/news/photo/201811/3955_16392_146.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11272"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고][광주전남지역본부] 공공전세 1차 입주자 모집공고\n공급유형 : 매입임대\n공고일자 : 2022-04-28",
                        "thumbnail": {
                            "imageUrl": "http://newsroom.etomato.com/userfiles/suwon%20kwonsun.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11242"
                            }
                        ]
                    },
                    {
                        "description": "[광주전남지역본부] 공공전세 1차 입주자 모집공고\n공급유형 : 매입임대\n공고일자 : 2022-04-28",
                        "thumbnail": {
                            "imageUrl": "https://post-phinf.pstatic.net/MjAyMTA2MDRfMTY2/MDAxNjIyNzkxODYwMzI4.I0nOP1lyXNA2J-so9L1dmQ4W0L8L3j4n3IHI35--6RMg.S1vc0fkJloQLMbD9FQHIrn2vHgJgiy0CsoC6Stth7Vcg.JPEG/1.JPG?type=w1200"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11229"
                            }
                        ]
                    },
                    {
                        "description": "[정정공고][광주광역시 광산구] 기존주택 등 매입임대주택 입주자 모집 공고\n공급유형 : 매입임대\n공고일자 : 2022-04-26",
                        "thumbnail": {
                            "imageUrl": "https://img.sbs.co.kr/newimg/news/20220316/201647138_1280.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11285"
                            }
                        ]
                    },
                    {
                        "description": "[광주광역시 광산구] 기존주택 등 매입임대주택 입주자 모집 공고\n공급유형 : 매입임대\n공고일자 : 2022-04-26",
                        "thumbnail": {
                            "imageUrl": "https://www.shinailbo.co.kr/news/photo/202104/1398185_608466_5339.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11217"
                            }
                        ]
                    },
                    {
                        "description": "2022년 신혼부부 전세임대Ⅱ 입주자 수시모집(자격완화) 공고\n공급유형 : 전세임대\n공고일자 : 2022-04-25",
                        "thumbnail": {
                            "imageUrl": "https://mediahub.seoul.go.kr/uploads/mediahub/2022/04/xsGpaZKCJGgdCtbWtiUMtHADDDbAlizt.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11207"
                            }
                        ]
                    }
                ]
            }
        }
        ],
        "quickReplies": [
        {
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c35604a7d7314aebddd4?scenarioId=6281c2009ac8ed784416bc1a"
        },
        {
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody



# 강원도 임대주택 목록
@app.route('/api/gangwonDo', methods=['POST'])
def gangwonDo():
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
                        "description": "강원도 내용",
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11432"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11376"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11328"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11286"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://cdn.eroun.net/news/photo/201811/3955_16392_146.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11272"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "http://newsroom.etomato.com/userfiles/suwon%20kwonsun.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11242"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://post-phinf.pstatic.net/MjAyMTA2MDRfMTY2/MDAxNjIyNzkxODYwMzI4.I0nOP1lyXNA2J-so9L1dmQ4W0L8L3j4n3IHI35--6RMg.S1vc0fkJloQLMbD9FQHIrn2vHgJgiy0CsoC6Stth7Vcg.JPEG/1.JPG?type=w1200"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11229"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.sbs.co.kr/newimg/news/20220316/201647138_1280.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11285"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://www.shinailbo.co.kr/news/photo/202104/1398185_608466_5339.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11217"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://mediahub.seoul.go.kr/uploads/mediahub/2022/04/xsGpaZKCJGgdCtbWtiUMtHADDDbAlizt.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11207"
                            }
                        ]
                    }
                ]
            }
        }
        ],
        "quickReplies": [
        {
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c37d45b5fc3106460080?scenarioId=6281c2009ac8ed784416bc1a"
        },
        {
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody



# 충청남도 임대주택 목록
@app.route('/api/chungcheongNamdo', methods=['POST'])
def chungcheongNamdo():
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
                        "description": "충청남도 내용",
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11432"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11376"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11328"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11286"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://cdn.eroun.net/news/photo/201811/3955_16392_146.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11272"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "http://newsroom.etomato.com/userfiles/suwon%20kwonsun.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11242"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://post-phinf.pstatic.net/MjAyMTA2MDRfMTY2/MDAxNjIyNzkxODYwMzI4.I0nOP1lyXNA2J-so9L1dmQ4W0L8L3j4n3IHI35--6RMg.S1vc0fkJloQLMbD9FQHIrn2vHgJgiy0CsoC6Stth7Vcg.JPEG/1.JPG?type=w1200"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11229"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.sbs.co.kr/newimg/news/20220316/201647138_1280.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11285"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://www.shinailbo.co.kr/news/photo/202104/1398185_608466_5339.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11217"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://mediahub.seoul.go.kr/uploads/mediahub/2022/04/xsGpaZKCJGgdCtbWtiUMtHADDDbAlizt.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11207"
                            }
                        ]
                    }
                ]
            }
        }
        ],
        "quickReplies": [
        {
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c37d45b5fc3106460080?scenarioId=6281c2009ac8ed784416bc1a"
        },
        {
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody



# 충청북도 임대주택 목록
@app.route('/api/chungcheongBukdo', methods=['POST'])
def chungcheongBukdo():
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
                        "description": "충청북도 내용",
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11432"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11376"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11328"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11286"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://cdn.eroun.net/news/photo/201811/3955_16392_146.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11272"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "http://newsroom.etomato.com/userfiles/suwon%20kwonsun.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11242"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://post-phinf.pstatic.net/MjAyMTA2MDRfMTY2/MDAxNjIyNzkxODYwMzI4.I0nOP1lyXNA2J-so9L1dmQ4W0L8L3j4n3IHI35--6RMg.S1vc0fkJloQLMbD9FQHIrn2vHgJgiy0CsoC6Stth7Vcg.JPEG/1.JPG?type=w1200"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11229"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.sbs.co.kr/newimg/news/20220316/201647138_1280.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11285"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://www.shinailbo.co.kr/news/photo/202104/1398185_608466_5339.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11217"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://mediahub.seoul.go.kr/uploads/mediahub/2022/04/xsGpaZKCJGgdCtbWtiUMtHADDDbAlizt.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11207"
                            }
                        ]
                    }
                ]
            }
        }
        ],
        "quickReplies": [
        {
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c37d45b5fc3106460080?scenarioId=6281c2009ac8ed784416bc1a"
        },
        {
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody




# 경상남도 임대주택 목록
@app.route('/api/gyeongsangNamdo', methods=['POST'])
def gyeongsangNamdo():
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
                        "description": "경상남도 내용",
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11432"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11376"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11328"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11286"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://cdn.eroun.net/news/photo/201811/3955_16392_146.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11272"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "http://newsroom.etomato.com/userfiles/suwon%20kwonsun.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11242"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://post-phinf.pstatic.net/MjAyMTA2MDRfMTY2/MDAxNjIyNzkxODYwMzI4.I0nOP1lyXNA2J-so9L1dmQ4W0L8L3j4n3IHI35--6RMg.S1vc0fkJloQLMbD9FQHIrn2vHgJgiy0CsoC6Stth7Vcg.JPEG/1.JPG?type=w1200"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11229"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.sbs.co.kr/newimg/news/20220316/201647138_1280.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11285"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://www.shinailbo.co.kr/news/photo/202104/1398185_608466_5339.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11217"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://mediahub.seoul.go.kr/uploads/mediahub/2022/04/xsGpaZKCJGgdCtbWtiUMtHADDDbAlizt.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11207"
                            }
                        ]
                    }
                ]
            }
        }
        ],
        "quickReplies": [
        {
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c37d45b5fc3106460080?scenarioId=6281c2009ac8ed784416bc1a"
        },
        {
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody





# 경상북도 임대주택 목록
@app.route('/api/gyeongsangBukdo', methods=['POST'])
def gyeongsangBukdo():
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
                        "description": "경상북도 내용",
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11432"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11376"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11328"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11286"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://cdn.eroun.net/news/photo/201811/3955_16392_146.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11272"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "http://newsroom.etomato.com/userfiles/suwon%20kwonsun.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11242"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://post-phinf.pstatic.net/MjAyMTA2MDRfMTY2/MDAxNjIyNzkxODYwMzI4.I0nOP1lyXNA2J-so9L1dmQ4W0L8L3j4n3IHI35--6RMg.S1vc0fkJloQLMbD9FQHIrn2vHgJgiy0CsoC6Stth7Vcg.JPEG/1.JPG?type=w1200"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11229"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.sbs.co.kr/newimg/news/20220316/201647138_1280.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11285"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://www.shinailbo.co.kr/news/photo/202104/1398185_608466_5339.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11217"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://mediahub.seoul.go.kr/uploads/mediahub/2022/04/xsGpaZKCJGgdCtbWtiUMtHADDDbAlizt.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11207"
                            }
                        ]
                    }
                ]
            }
        }
        ],
        "quickReplies": [
        {
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c37d45b5fc3106460080?scenarioId=6281c2009ac8ed784416bc1a"
        },
        {
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody



# 전라남도 임대주택 목록
@app.route('/api/jeollaNamdo', methods=['POST'])
def jeollaNamdo():
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
                        "description": "전라남도 내용",
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11432"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11376"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11328"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11286"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://cdn.eroun.net/news/photo/201811/3955_16392_146.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11272"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "http://newsroom.etomato.com/userfiles/suwon%20kwonsun.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11242"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://post-phinf.pstatic.net/MjAyMTA2MDRfMTY2/MDAxNjIyNzkxODYwMzI4.I0nOP1lyXNA2J-so9L1dmQ4W0L8L3j4n3IHI35--6RMg.S1vc0fkJloQLMbD9FQHIrn2vHgJgiy0CsoC6Stth7Vcg.JPEG/1.JPG?type=w1200"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11229"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.sbs.co.kr/newimg/news/20220316/201647138_1280.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11285"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://www.shinailbo.co.kr/news/photo/202104/1398185_608466_5339.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11217"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://mediahub.seoul.go.kr/uploads/mediahub/2022/04/xsGpaZKCJGgdCtbWtiUMtHADDDbAlizt.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11207"
                            }
                        ]
                    }
                ]
            }
        }
        ],
        "quickReplies": [
        {
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c37d45b5fc3106460080?scenarioId=6281c2009ac8ed784416bc1a"
        },
        {
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody





# 전라북도 임대주택 목록
@app.route('/api/jeollaBukdo', methods=['POST'])
def jeollaBukdo():
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
                        "description": "전라북도 내용",
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11432"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11376"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11328"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11286"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://cdn.eroun.net/news/photo/201811/3955_16392_146.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11272"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "http://newsroom.etomato.com/userfiles/suwon%20kwonsun.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11242"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://post-phinf.pstatic.net/MjAyMTA2MDRfMTY2/MDAxNjIyNzkxODYwMzI4.I0nOP1lyXNA2J-so9L1dmQ4W0L8L3j4n3IHI35--6RMg.S1vc0fkJloQLMbD9FQHIrn2vHgJgiy0CsoC6Stth7Vcg.JPEG/1.JPG?type=w1200"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11229"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.sbs.co.kr/newimg/news/20220316/201647138_1280.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11285"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://www.shinailbo.co.kr/news/photo/202104/1398185_608466_5339.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11217"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://mediahub.seoul.go.kr/uploads/mediahub/2022/04/xsGpaZKCJGgdCtbWtiUMtHADDDbAlizt.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11207"
                            }
                        ]
                    }
                ]
            }
        }
        ],
        "quickReplies": [
        {
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c37d45b5fc3106460080?scenarioId=6281c2009ac8ed784416bc1a"
        },
        {
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody




# 제주특별자치도 임대주택 목록
@app.route('/api/jeju', methods=['POST'])
def jeju():
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
                        "description": "제주특별자치도 내용",
                        "thumbnail": {
                            "imageUrl": "https://www.korea.kr/newsWeb/resources/attaches/2017.08/09/2322222_cp.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11432"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://news.imaeil.com/photos/2020/05/06/2020050612251729107_l.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11376"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.hani.co.kr/imgdb/resize/2018/1126/00502924_20181126.JPG"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11328"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.hankyung.com/photo/202202/01.29018214.1.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11286"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://cdn.eroun.net/news/photo/201811/3955_16392_146.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11272"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "http://newsroom.etomato.com/userfiles/suwon%20kwonsun.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11242"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://post-phinf.pstatic.net/MjAyMTA2MDRfMTY2/MDAxNjIyNzkxODYwMzI4.I0nOP1lyXNA2J-so9L1dmQ4W0L8L3j4n3IHI35--6RMg.S1vc0fkJloQLMbD9FQHIrn2vHgJgiy0CsoC6Stth7Vcg.JPEG/1.JPG?type=w1200"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11229"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://img.sbs.co.kr/newimg/news/20220316/201647138_1280.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11285"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://www.shinailbo.co.kr/news/photo/202104/1398185_608466_5339.jpg"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11217"
                            }
                        ]
                    },
                    {
                        "description": "내용",
                        "thumbnail": {
                            "imageUrl": "https://mediahub.seoul.go.kr/uploads/mediahub/2022/04/xsGpaZKCJGgdCtbWtiUMtHADDDbAlizt.png"
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": "https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcDetailView.do?pblancId=11207"
                            }
                        ]
                    }
                ]
            }
        }
        ],
        "quickReplies": [
        {
            "label": "지역 목록으로 돌아가기",
            "action": "block",
            "blockId": "6281c37d45b5fc3106460080?scenarioId=6281c2009ac8ed784416bc1a"
        },
        {
            "label": "처음으로 돌아가기",
            "action": "block",
            "blockId": "627b293404a7d7314aeb7b0d?scenarioId=627b131e9ac8ed7844165d72"
        }
        ]
        }
    }

    return responseBody