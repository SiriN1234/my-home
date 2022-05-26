from flask import Flask, request
import json
import pandas as pd
import csv
import random

from app import test_text as tt

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


###################################################################
# thumbnail 불러오기
thumbnail = pd.read_csv("./app/data/Thumbnail.csv")
thumbnail_arr = []
for i in range(10) :
    thumbnail_arr.append(thumbnail.iloc[i]['thumbnail'])
###################################################################


# 서울시 임대주택 목록
@app.route('/api/seoul', methods=['POST'])
def seoul():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    ###########################################################
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
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################
    
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
                            "imageUrl": rand_thumb[0]
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
                            "imageUrl": rand_thumb[1]
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
                            "imageUrl": rand_thumb[2]
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
                            "imageUrl": rand_thumb[3]
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
                            "imageUrl": rand_thumb[4]
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
                            "imageUrl": rand_thumb[5]
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
                            "imageUrl": rand_thumb[6]
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
                            "imageUrl": rand_thumb[7]
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
                            "imageUrl": rand_thumb[8]
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
                            "imageUrl": rand_thumb[9]
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

    ###########################################################
    # csv 파일 불러오기
    gyeonggi_notice = pd.read_csv("./app/data/Gyeonggi_notice.csv")
    gyeonggi_url = pd.read_csv("./app/data/Gyeonggi_url.csv")

    # 값을 넣을 배열 선언
    gyeonggi_notice_arr = [] # description에 들어갈 값
    gyeonggi_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        gyeonggi_url_arr.append(gyeonggi_url.iloc[i]['url'])
        gyeonggi_notice_arr.append(gyeonggi_notice.iloc[i]['name'] + "\n공급유형 : " + gyeonggi_notice.iloc[i]['title'] + "\n공고일자 : " + gyeonggi_notice.iloc[i]['re_date'])
    
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "description": gyeonggi_notice_arr[0],
                        "thumbnail": {
                            "imageUrl": rand_thumb[0]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeonggi_url_arr[0]
                            }
                        ]
                    },
                    {
                        "description": gyeonggi_notice_arr[1],
                        "thumbnail": {
                            "imageUrl": rand_thumb[1]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeonggi_url_arr[1]
                            }
                        ]
                    },
                    {
                        "description": gyeonggi_notice_arr[2],
                        "thumbnail": {
                            "imageUrl": rand_thumb[2]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeonggi_url_arr[2]
                            }
                        ]
                    },
                    {
                        "description": gyeonggi_notice_arr[3],
                        "thumbnail": {
                            "imageUrl": rand_thumb[3]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeonggi_url_arr[3]
                            }
                        ]
                    },
                    {
                        "description": gyeonggi_notice_arr[4],
                        "thumbnail": {
                            "imageUrl": rand_thumb[4]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeonggi_url_arr[4]
                            }
                        ]
                    },
                    {
                        "description": gyeonggi_notice_arr[5],
                        "thumbnail": {
                            "imageUrl": rand_thumb[5]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeonggi_url_arr[5]
                            }
                        ]
                    },
                    {
                        "description": gyeonggi_notice_arr[6],
                        "thumbnail": {
                            "imageUrl": rand_thumb[6]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeonggi_url_arr[6]
                            }
                        ]
                    },
                    {
                        "description": gyeonggi_notice_arr[7],
                        "thumbnail": {
                            "imageUrl": rand_thumb[7]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeonggi_url_arr[7]
                            }
                        ]
                    },
                    {
                        "description": gyeonggi_notice_arr[8],
                        "thumbnail": {
                            "imageUrl": rand_thumb[8]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeonggi_url_arr[8]
                            }
                        ]
                    },
                    {
                        "description": gyeonggi_notice_arr[9],
                        "thumbnail": {
                            "imageUrl": rand_thumb[9]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeonggi_url_arr[9]
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

    ###########################################################
    # csv 파일 불러오기
    incheon_notice = pd.read_csv("./app/data/Incheon_notice.csv")
    incheon_url = pd.read_csv("./app/data/Incheon_url.csv")

    # 값을 넣을 배열 선언
    incheon_notice_arr = [] # description에 들어갈 값
    incheon_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        incheon_url_arr.append(incheon_url.iloc[i]['url'])
        incheon_notice_arr.append(incheon_notice.iloc[i]['name'] + "\n공급유형 : " + incheon_notice.iloc[i]['title'] + "\n공고일자 : " + incheon_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "description": incheon_notice_arr[0],
                        "thumbnail": {
                            "imageUrl": rand_thumb[0]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": incheon_url_arr[0]
                            }
                        ]
                    },
                    {
                        "description": incheon_notice_arr[1],
                        "thumbnail": {
                            "imageUrl": rand_thumb[1]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": incheon_url_arr[1]
                            }
                        ]
                    },
                    {
                        "description": incheon_notice_arr[2],
                        "thumbnail": {
                            "imageUrl": rand_thumb[2]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": incheon_url_arr[2]
                            }
                        ]
                    },
                    {
                        "description": incheon_notice_arr[3],
                        "thumbnail": {
                            "imageUrl": rand_thumb[3]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": incheon_url_arr[3]
                            }
                        ]
                    },
                    {
                        "description": incheon_notice_arr[4],
                        "thumbnail": {
                            "imageUrl": rand_thumb[4]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": incheon_url_arr[4]
                            }
                        ]
                    },
                    {
                        "description": incheon_notice_arr[5],
                        "thumbnail": {
                            "imageUrl": rand_thumb[5]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": incheon_url_arr[5]
                            }
                        ]
                    },
                    {
                        "description": incheon_notice_arr[6],
                        "thumbnail": {
                            "imageUrl": rand_thumb[6]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": incheon_url_arr[6]
                            }
                        ]
                    },
                    {
                        "description": incheon_notice_arr[7],
                        "thumbnail": {
                            "imageUrl": rand_thumb[7]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": incheon_url_arr[7]
                            }
                        ]
                    },
                    {
                        "description": incheon_notice_arr[8],
                        "thumbnail": {
                            "imageUrl": rand_thumb[8]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": incheon_url_arr[8]
                            }
                        ]
                    },
                    {
                        "description": incheon_notice_arr[9],
                        "thumbnail": {
                            "imageUrl": rand_thumb[9]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": incheon_url_arr[9]
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

    ###########################################################
    # csv 파일 불러오기
    daejeon_notice = pd.read_csv("./app/data/Daejeon_notice.csv")
    daejeon_url = pd.read_csv("./app/data/Daejeon_url.csv")

    # 값을 넣을 배열 선언
    daejeon_notice_arr = [] # description에 들어갈 값
    daejeon_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        daejeon_url_arr.append(daejeon_url.iloc[i]['url'])
        daejeon_notice_arr.append(daejeon_notice.iloc[i]['name'] + "\n공급유형 : " + daejeon_notice.iloc[i]['title'] + "\n공고일자 : " + daejeon_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "description": daejeon_notice_arr[0],
                        "thumbnail": {
                            "imageUrl": rand_thumb[0]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daejeon_url_arr[0]
                            }
                        ]
                    },
                    {
                        "description": daejeon_notice_arr[1],
                        "thumbnail": {
                            "imageUrl": rand_thumb[1]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daejeon_url_arr[1]
                            }
                        ]
                    },
                    {
                        "description": daejeon_notice_arr[2],
                        "thumbnail": {
                            "imageUrl": rand_thumb[2]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daejeon_url_arr[2]
                            }
                        ]
                    },
                    {
                        "description": daejeon_notice_arr[3],
                        "thumbnail": {
                            "imageUrl": rand_thumb[3]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daejeon_url_arr[3]
                            }
                        ]
                    },
                    {
                        "description": daejeon_notice_arr[4],
                        "thumbnail": {
                            "imageUrl": rand_thumb[4]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daejeon_url_arr[4]
                            }
                        ]
                    },
                    {
                        "description": daejeon_notice_arr[5],
                        "thumbnail": {
                            "imageUrl": rand_thumb[5]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daejeon_url_arr[5]
                            }
                        ]
                    },
                    {
                        "description": daejeon_notice_arr[6],
                        "thumbnail": {
                            "imageUrl": rand_thumb[6]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daejeon_url_arr[6]
                            }
                        ]
                    },
                    {
                        "description": daejeon_notice_arr[7],
                        "thumbnail": {
                            "imageUrl": rand_thumb[7]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daejeon_url_arr[7]
                            }
                        ]
                    },
                    {
                        "description": daejeon_notice_arr[8],
                        "thumbnail": {
                            "imageUrl": rand_thumb[8]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daejeon_url_arr[8]
                            }
                        ]
                    },
                    {
                        "description": daejeon_notice_arr[9],
                        "thumbnail": {
                            "imageUrl": rand_thumb[9]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daejeon_url_arr[9]
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
@app.route('/api/sejong', methods=['POST'])
def sejong():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    ###########################################################
    # csv 파일 불러오기
    sejong_notice = pd.read_csv("./app/data/Sejong_notice.csv")
    sejong_url = pd.read_csv("./app/data/Sejong_url.csv")

    # 값을 넣을 배열 선언
    sejong_notice_arr = [] # description에 들어갈 값
    sejong_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        sejong_url_arr.append(sejong_url.iloc[i]['url'])
        sejong_notice_arr.append(sejong_notice.iloc[i]['name'] + "\n공급유형 : " + sejong_notice.iloc[i]['title'] + "\n공고일자 : " + sejong_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "description": sejong_notice_arr[0],
                        "thumbnail": {
                            "imageUrl": rand_thumb[0]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": sejong_url_arr[0]
                            }
                        ]
                    },
                    {
                        "description": sejong_notice_arr[1],
                        "thumbnail": {
                            "imageUrl": rand_thumb[1]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": sejong_url_arr[1]
                            }
                        ]
                    },
                    {
                        "description": sejong_notice_arr[2],
                        "thumbnail": {
                            "imageUrl": rand_thumb[2]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": sejong_url_arr[2]
                            }
                        ]
                    },
                    {
                        "description": sejong_notice_arr[3],
                        "thumbnail": {
                            "imageUrl": rand_thumb[3]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": sejong_url_arr[3]
                            }
                        ]
                    },
                    {
                        "description": sejong_notice_arr[4],
                        "thumbnail": {
                            "imageUrl": rand_thumb[4]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": sejong_url_arr[4]
                            }
                        ]
                    },
                    {
                        "description": sejong_notice_arr[5],
                        "thumbnail": {
                            "imageUrl": rand_thumb[5]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": sejong_url_arr[5]
                            }
                        ]
                    },
                    {
                        "description": sejong_notice_arr[6],
                        "thumbnail": {
                            "imageUrl": rand_thumb[6]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": sejong_url_arr[6]
                            }
                        ]
                    },
                    {
                        "description": sejong_notice_arr[7],
                        "thumbnail": {
                            "imageUrl": rand_thumb[7]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": sejong_url_arr[7]
                            }
                        ]
                    },
                    {
                        "description": sejong_notice_arr[8],
                        "thumbnail": {
                            "imageUrl": rand_thumb[8]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": sejong_url_arr[8]
                            }
                        ]
                    },
                    {
                        "description": sejong_notice_arr[9],
                        "thumbnail": {
                            "imageUrl": rand_thumb[9]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": sejong_url_arr[9]
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
    
    ###########################################################
    # csv 파일 불러오기
    busan_notice = pd.read_csv("./app/data/Busan_notice.csv")
    busan_url = pd.read_csv("./app/data/Busan_url.csv")

    # 값을 넣을 배열 선언
    busan_notice_arr = [] # description에 들어갈 값
    busan_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        busan_url_arr.append(busan_url.iloc[i]['url'])
        busan_notice_arr.append(busan_notice.iloc[i]['name'] + "\n공급유형 : " + busan_notice.iloc[i]['title'] + "\n공고일자 : " + busan_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################    

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "description": busan_notice_arr[0],
                        "thumbnail": {
                            "imageUrl": rand_thumb[0]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": busan_url_arr[0]
                            }
                        ]
                    },
                    {
                        "description": busan_notice_arr[1],
                        "thumbnail": {
                            "imageUrl": rand_thumb[1]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": busan_url_arr[1]
                            }
                        ]
                    },
                    {
                        "description": busan_notice_arr[2],
                        "thumbnail": {
                            "imageUrl": rand_thumb[2]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": busan_url_arr[2]
                            }
                        ]
                    },
                    {
                        "description": busan_notice_arr[3],
                        "thumbnail": {
                            "imageUrl": rand_thumb[3]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": busan_url_arr[3]
                            }
                        ]
                    },
                    {
                        "description": busan_notice_arr[4],
                        "thumbnail": {
                            "imageUrl": rand_thumb[4]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": busan_url_arr[4]
                            }
                        ]
                    },
                    {
                        "description": busan_notice_arr[5],
                        "thumbnail": {
                            "imageUrl": rand_thumb[5]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": busan_url_arr[5]
                            }
                        ]
                    },
                    {
                        "description": busan_notice_arr[6],
                        "thumbnail": {
                            "imageUrl": rand_thumb[6]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": busan_url_arr[6]
                            }
                        ]
                    },
                    {
                        "description": busan_notice_arr[7],
                        "thumbnail": {
                            "imageUrl": rand_thumb[7]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": busan_url_arr[7]
                            }
                        ]
                    },
                    {
                        "description": busan_notice_arr[8],
                        "thumbnail": {
                            "imageUrl": rand_thumb[8]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": busan_url_arr[8]
                            }
                        ]
                    },
                    {
                        "description": busan_notice_arr[9],
                        "thumbnail": {
                            "imageUrl": rand_thumb[9]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": busan_url_arr[9]
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

    ###########################################################
    # csv 파일 불러오기
    ulsan_notice = pd.read_csv("./app/data/Ulsan_notice.csv")
    ulsan_url = pd.read_csv("./app/data/Ulsan_url.csv")

    # 값을 넣을 배열 선언
    ulsan_notice_arr = [] # description에 들어갈 값
    ulsan_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        ulsan_url_arr.append(ulsan_url.iloc[i]['url'])
        ulsan_notice_arr.append(ulsan_notice.iloc[i]['name'] + "\n공급유형 : " + ulsan_notice.iloc[i]['title'] + "\n공고일자 : " + ulsan_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "description": ulsan_notice_arr[0],
                        "thumbnail": {
                            "imageUrl": rand_thumb[0]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": ulsan_url_arr[0]
                            }
                        ]
                    },
                    {
                        "description": ulsan_notice_arr[1],
                        "thumbnail": {
                            "imageUrl": rand_thumb[1]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": ulsan_url_arr[1]
                            }
                        ]
                    },
                    {
                        "description": ulsan_notice_arr[2],
                        "thumbnail": {
                            "imageUrl": rand_thumb[2]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": ulsan_url_arr[2]
                            }
                        ]
                    },
                    {
                        "description": ulsan_notice_arr[3],
                        "thumbnail": {
                            "imageUrl": rand_thumb[3]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": ulsan_url_arr[3]
                            }
                        ]
                    },
                    {
                        "description": ulsan_notice_arr[4],
                        "thumbnail": {
                            "imageUrl": rand_thumb[4]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": ulsan_url_arr[4]
                            }
                        ]
                    },
                    {
                        "description": ulsan_notice_arr[5],
                        "thumbnail": {
                            "imageUrl": rand_thumb[5]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": ulsan_url_arr[5]
                            }
                        ]
                    },
                    {
                        "description": ulsan_notice_arr[6],
                        "thumbnail": {
                            "imageUrl": rand_thumb[6]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": ulsan_url_arr[6]
                            }
                        ]
                    },
                    {
                        "description": ulsan_notice_arr[7],
                        "thumbnail": {
                            "imageUrl": rand_thumb[7]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": ulsan_url_arr[7]
                            }
                        ]
                    },
                    {
                        "description": ulsan_notice_arr[8],
                        "thumbnail": {
                            "imageUrl": rand_thumb[8]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": ulsan_url_arr[8]
                            }
                        ]
                    },
                    {
                        "description": ulsan_notice_arr[9],
                        "thumbnail": {
                            "imageUrl": rand_thumb[9]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": ulsan_url_arr[9]
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

    ###########################################################
    # csv 파일 불러오기
    daegu_notice = pd.read_csv("./app/data/Daegu_notice.csv")
    daegu_url = pd.read_csv("./app/data/Daegu_url.csv")

    # 값을 넣을 배열 선언
    daegu_notice_arr = [] # description에 들어갈 값
    daegu_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        daegu_url_arr.append(daegu_url.iloc[i]['url'])
        daegu_notice_arr.append(daegu_notice.iloc[i]['name'] + "\n공급유형 : " + daegu_notice.iloc[i]['title'] + "\n공고일자 : " + daegu_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "description": daegu_notice_arr[0],
                        "thumbnail": {
                            "imageUrl": rand_thumb[0]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daegu_url_arr[0]
                            }
                        ]
                    },
                    {
                        "description": daegu_notice_arr[1],
                        "thumbnail": {
                            "imageUrl": rand_thumb[1]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daegu_url_arr[1]
                            }
                        ]
                    },
                    {
                        "description": daegu_notice_arr[2],
                        "thumbnail": {
                            "imageUrl": rand_thumb[2]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daegu_url_arr[2]
                            }
                        ]
                    },
                    {
                        "description": daegu_notice_arr[3],
                        "thumbnail": {
                            "imageUrl": rand_thumb[3]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daegu_url_arr[3]
                            }
                        ]
                    },
                    {
                        "description": daegu_notice_arr[4],
                        "thumbnail": {
                            "imageUrl": rand_thumb[4]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daegu_url_arr[4]
                            }
                        ]
                    },
                    {
                        "description": daegu_notice_arr[5],
                        "thumbnail": {
                            "imageUrl": rand_thumb[5]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daegu_url_arr[5]
                            }
                        ]
                    },
                    {
                        "description": daegu_notice_arr[6],
                        "thumbnail": {
                            "imageUrl": rand_thumb[6]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daegu_url_arr[6]
                            }
                        ]
                    },
                    {
                        "description": daegu_notice_arr[7],
                        "thumbnail": {
                            "imageUrl": rand_thumb[7]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daegu_url_arr[7]
                            }
                        ]
                    },
                    {
                        "description": daegu_notice_arr[8],
                        "thumbnail": {
                            "imageUrl": rand_thumb[8]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daegu_url_arr[8]
                            }
                        ]
                    },
                    {
                        "description": daegu_notice_arr[9],
                        "thumbnail": {
                            "imageUrl": rand_thumb[9]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": daegu_url_arr[9]
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

    ###########################################################
    # csv 파일 불러오기
    gwangju_notice = pd.read_csv("./app/data/Gwangju_notice.csv")
    gwangju_url = pd.read_csv("./app/data/Gwangju_url.csv")

    # 값을 넣을 배열 선언
    gwangju_notice_arr = [] # description에 들어갈 값
    gwangju_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        gwangju_url_arr.append(gwangju_url.iloc[i]['url'])
        gwangju_notice_arr.append(gwangju_notice.iloc[i]['name'] + "\n공급유형 : " + gwangju_notice.iloc[i]['title'] + "\n공고일자 : " + gwangju_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "description": gwangju_notice_arr[0],
                        "thumbnail": {
                            "imageUrl": rand_thumb[0]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gwangju_url_arr[0]
                            }
                        ]
                    },
                    {
                        "description": gwangju_notice_arr[1],
                        "thumbnail": {
                            "imageUrl": rand_thumb[1]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gwangju_url_arr[1]
                            }
                        ]
                    },
                    {
                        "description": gwangju_notice_arr[2],
                        "thumbnail": {
                            "imageUrl": rand_thumb[2]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gwangju_url_arr[2]
                            }
                        ]
                    },
                    {
                        "description": gwangju_notice_arr[3],
                        "thumbnail": {
                            "imageUrl": rand_thumb[3]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gwangju_url_arr[3]
                            }
                        ]
                    },
                    {
                        "description": gwangju_notice_arr[4],
                        "thumbnail": {
                            "imageUrl": rand_thumb[4]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gwangju_url_arr[4]
                            }
                        ]
                    },
                    {
                        "description": gwangju_notice_arr[5],
                        "thumbnail": {
                            "imageUrl": rand_thumb[5]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gwangju_url_arr[5]
                            }
                        ]
                    },
                    {
                        "description": gwangju_notice_arr[6],
                        "thumbnail": {
                            "imageUrl": rand_thumb[6]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gwangju_url_arr[6]
                            }
                        ]
                    },
                    {
                        "description": gwangju_notice_arr[7],
                        "thumbnail": {
                            "imageUrl": rand_thumb[7]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gwangju_url_arr[7]
                            }
                        ]
                    },
                    {
                        "description": gwangju_notice_arr[8],
                        "thumbnail": {
                            "imageUrl": rand_thumb[8]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gwangju_url_arr[8]
                            }
                        ]
                    },
                    {
                        "description": gwangju_notice_arr[9],
                        "thumbnail": {
                            "imageUrl": rand_thumb[9]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gwangju_url_arr[9]
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

    ###########################################################
    # csv 파일 불러오기
    gangwon_notice = pd.read_csv("./app/data/Gangwon_notice.csv")
    gangwon_url = pd.read_csv("./app/data/Gangwon_url.csv")

    # 값을 넣을 배열 선언
    gangwon_notice_arr = [] # description에 들어갈 값
    gangwon_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        gangwon_url_arr.append(gangwon_url.iloc[i]['url'])
        gangwon_notice_arr.append(gangwon_notice.iloc[i]['name'] + "\n공급유형 : " + gangwon_notice.iloc[i]['title'] + "\n공고일자 : " + gangwon_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "description": gangwon_notice_arr[0],
                        "thumbnail": {
                            "imageUrl": rand_thumb[0]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gangwon_url_arr[0]
                            }
                        ]
                    },
                    {
                        "description": gangwon_notice_arr[1],
                        "thumbnail": {
                            "imageUrl": rand_thumb[1]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gangwon_url_arr[1]
                            }
                        ]
                    },
                    {
                        "description": gangwon_notice_arr[2],
                        "thumbnail": {
                            "imageUrl": rand_thumb[2]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gangwon_url_arr[2]
                            }
                        ]
                    },
                    {
                        "description": gangwon_notice_arr[3],
                        "thumbnail": {
                            "imageUrl": rand_thumb[3]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gangwon_url_arr[3]
                            }
                        ]
                    },
                    {
                        "description": gangwon_notice_arr[4],
                        "thumbnail": {
                            "imageUrl": rand_thumb[4]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gangwon_url_arr[4]
                            }
                        ]
                    },
                    {
                        "description": gangwon_notice_arr[5],
                        "thumbnail": {
                            "imageUrl": rand_thumb[5]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gangwon_url_arr[5]
                            }
                        ]
                    },
                    {
                        "description": gangwon_notice_arr[6],
                        "thumbnail": {
                            "imageUrl": rand_thumb[6]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gangwon_url_arr[6]
                            }
                        ]
                    },
                    {
                        "description": gangwon_notice_arr[7],
                        "thumbnail": {
                            "imageUrl": rand_thumb[7]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gangwon_url_arr[7]
                            }
                        ]
                    },
                    {
                        "description": gangwon_notice_arr[8],
                        "thumbnail": {
                            "imageUrl": rand_thumb[8]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gangwon_url_arr[8]
                            }
                        ]
                    },
                    {
                        "description": gangwon_notice_arr[9],
                        "thumbnail": {
                            "imageUrl": rand_thumb[9]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gangwon_url_arr[9]
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
    
    ###########################################################
    # csv 파일 불러오기
    chungnam_notice = pd.read_csv("./app/data/Chungnam_notice.csv")
    chungnam_url = pd.read_csv("./app/data/Chungnam_url.csv")

    # 값을 넣을 배열 선언
    chungnam_notice_arr = [] # description에 들어갈 값
    chungnam_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        chungnam_url_arr.append(chungnam_url.iloc[i]['url'])
        chungnam_notice_arr.append(chungnam_notice.iloc[i]['name'] + "\n공급유형 : " + chungnam_notice.iloc[i]['title'] + "\n공고일자 : " + chungnam_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "description": chungnam_notice_arr[0],
                        "thumbnail": {
                            "imageUrl": rand_thumb[0]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungnam_url_arr[0]
                            }
                        ]
                    },
                    {
                        "description": chungnam_notice_arr[1],
                        "thumbnail": {
                            "imageUrl": rand_thumb[1]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungnam_url_arr[1]
                            }
                        ]
                    },
                    {
                        "description": chungnam_notice_arr[2],
                        "thumbnail": {
                            "imageUrl": rand_thumb[2]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungnam_url_arr[2]
                            }
                        ]
                    },
                    {
                        "description": chungnam_notice_arr[3],
                        "thumbnail": {
                            "imageUrl": rand_thumb[3]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungnam_url_arr[3]
                            }
                        ]
                    },
                    {
                        "description": chungnam_notice_arr[4],
                        "thumbnail": {
                            "imageUrl": rand_thumb[4]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungnam_url_arr[4]
                            }
                        ]
                    },
                    {
                        "description": chungnam_notice_arr[5],
                        "thumbnail": {
                            "imageUrl": rand_thumb[5]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungnam_url_arr[5]
                            }
                        ]
                    },
                    {
                        "description": chungnam_notice_arr[6],
                        "thumbnail": {
                            "imageUrl": rand_thumb[6]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungnam_url_arr[6]
                            }
                        ]
                    },
                    {
                        "description": chungnam_notice_arr[7],
                        "thumbnail": {
                            "imageUrl": rand_thumb[7]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungnam_url_arr[7]
                            }
                        ]
                    },
                    {
                        "description": chungnam_notice_arr[8],
                        "thumbnail": {
                            "imageUrl": rand_thumb[8]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungnam_url_arr[8]
                            }
                        ]
                    },
                    {
                        "description": chungnam_notice_arr[9],
                        "thumbnail": {
                            "imageUrl": rand_thumb[9]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungnam_url_arr[9]
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

    ###########################################################
    # csv 파일 불러오기
    chungbuk_notice = pd.read_csv("./app/data/Chungbuk_notice.csv")
    chungbuk_url = pd.read_csv("./app/data/Chungbuk_url.csv")

    # 값을 넣을 배열 선언
    chungbuk_notice_arr = [] # description에 들어갈 값
    chungbuk_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        chungbuk_url_arr.append(chungbuk_url.iloc[i]['url'])
        chungbuk_notice_arr.append(chungbuk_notice.iloc[i]['name'] + "\n공급유형 : " + chungbuk_notice.iloc[i]['title'] + "\n공고일자 : " + chungbuk_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "description": chungbuk_notice_arr[0],
                        "thumbnail": {
                            "imageUrl": rand_thumb[0]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungbuk_url_arr[0]
                            }
                        ]
                    },
                    {
                        "description": chungbuk_notice_arr[1],
                        "thumbnail": {
                            "imageUrl": rand_thumb[1]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungbuk_url_arr[1]
                            }
                        ]
                    },
                    {
                        "description": chungbuk_notice_arr[2],
                        "thumbnail": {
                            "imageUrl": rand_thumb[2]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungbuk_url_arr[2]
                            }
                        ]
                    },
                    {
                        "description": chungbuk_notice_arr[3],
                        "thumbnail": {
                            "imageUrl": rand_thumb[3]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungbuk_url_arr[3]
                            }
                        ]
                    },
                    {
                        "description": chungbuk_notice_arr[4],
                        "thumbnail": {
                            "imageUrl": rand_thumb[4]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungbuk_url_arr[4]
                            }
                        ]
                    },
                    {
                        "description": chungbuk_notice_arr[5],
                        "thumbnail": {
                            "imageUrl": rand_thumb[5]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungbuk_url_arr[5]
                            }
                        ]
                    },
                    {
                        "description": chungbuk_notice_arr[6],
                        "thumbnail": {
                            "imageUrl": rand_thumb[6]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungbuk_url_arr[6]
                            }
                        ]
                    },
                    {
                        "description": chungbuk_notice_arr[7],
                        "thumbnail": {
                            "imageUrl": rand_thumb[7]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungbuk_url_arr[7]
                            }
                        ]
                    },
                    {
                        "description": chungbuk_notice_arr[8],
                        "thumbnail": {
                            "imageUrl": rand_thumb[8]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungbuk_url_arr[8]
                            }
                        ]
                    },
                    {
                        "description": chungbuk_notice_arr[9],
                        "thumbnail": {
                            "imageUrl": rand_thumb[9]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": chungbuk_url_arr[9]
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

    ###########################################################
    # csv 파일 불러오기
    gyeongnam_notice = pd.read_csv("./app/data/Gyeongnam_notice.csv")
    gyeongnam_url = pd.read_csv("./app/data/Gyeongnam_url.csv")

    # 값을 넣을 배열 선언
    gyeongnam_notice_arr = [] # description에 들어갈 값
    gyeongnam_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        gyeongnam_url_arr.append(gyeongnam_url.iloc[i]['url'])
        gyeongnam_notice_arr.append(gyeongnam_notice.iloc[i]['name'] + "\n공급유형 : " + gyeongnam_notice.iloc[i]['title'] + "\n공고일자 : " + gyeongnam_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "description": gyeongnam_notice_arr[0],
                        "thumbnail": {
                            "imageUrl": rand_thumb[0]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongnam_url_arr[0]
                            }
                        ]
                    },
                    {
                        "description": gyeongnam_notice_arr[1],
                        "thumbnail": {
                            "imageUrl": rand_thumb[1]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongnam_url_arr[1]
                            }
                        ]
                    },
                    {
                        "description": gyeongnam_notice_arr[2],
                        "thumbnail": {
                            "imageUrl": rand_thumb[2]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongnam_url_arr[2]
                            }
                        ]
                    },
                    {
                        "description": gyeongnam_notice_arr[3],
                        "thumbnail": {
                            "imageUrl": rand_thumb[3]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongnam_url_arr[3]
                            }
                        ]
                    },
                    {
                        "description": gyeongnam_notice_arr[4],
                        "thumbnail": {
                            "imageUrl": rand_thumb[4]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongnam_url_arr[4]
                            }
                        ]
                    },
                    {
                        "description": gyeongnam_notice_arr[5],
                        "thumbnail": {
                            "imageUrl": rand_thumb[5]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongnam_url_arr[5]
                            }
                        ]
                    },
                    {
                        "description": gyeongnam_notice_arr[6],
                        "thumbnail": {
                            "imageUrl": rand_thumb[6]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongnam_url_arr[6]
                            }
                        ]
                    },
                    {
                        "description": gyeongnam_notice_arr[7],
                        "thumbnail": {
                            "imageUrl": rand_thumb[7]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongnam_url_arr[7]
                            }
                        ]
                    },
                    {
                        "description": gyeongnam_notice_arr[8],
                        "thumbnail": {
                            "imageUrl": rand_thumb[8]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongnam_url_arr[8]
                            }
                        ]
                    },
                    {
                        "description": gyeongnam_notice_arr[9],
                        "thumbnail": {
                            "imageUrl": rand_thumb[9]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongnam_url_arr[9]
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

    ###########################################################
    # csv 파일 불러오기
    gyeongbuk_notice = pd.read_csv("./app/data/Gyeongbuk_notice.csv")
    gyeongbuk_url = pd.read_csv("./app/data/Gyeongbuk_url.csv")

    # 값을 넣을 배열 선언
    gyeongbuk_notice_arr = [] # description에 들어갈 값
    gyeongbuk_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        gyeongbuk_url_arr.append(gyeongbuk_url.iloc[i]['url'])
        gyeongbuk_notice_arr.append(gyeongbuk_notice.iloc[i]['name'] + "\n공급유형 : " + gyeongbuk_notice.iloc[i]['title'] + "\n공고일자 : " + gyeongbuk_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "description": gyeongbuk_notice_arr[0],
                        "thumbnail": {
                            "imageUrl": rand_thumb[0]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongbuk_url_arr[0]
                            }
                        ]
                    },
                    {
                        "description": gyeongbuk_notice_arr[1],
                        "thumbnail": {
                            "imageUrl": rand_thumb[1]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongbuk_url_arr[1]
                            }
                        ]
                    },
                    {
                        "description": gyeongbuk_notice_arr[2],
                        "thumbnail": {
                            "imageUrl": rand_thumb[2]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongbuk_url_arr[2]
                            }
                        ]
                    },
                    {
                        "description": gyeongbuk_notice_arr[3],
                        "thumbnail": {
                            "imageUrl": rand_thumb[3]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongbuk_url_arr[3]
                            }
                        ]
                    },
                    {
                        "description": gyeongbuk_notice_arr[4],
                        "thumbnail": {
                            "imageUrl": rand_thumb[4]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongbuk_url_arr[4]
                            }
                        ]
                    },
                    {
                        "description": gyeongbuk_notice_arr[5],
                        "thumbnail": {
                            "imageUrl": rand_thumb[5]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongbuk_url_arr[5]
                            }
                        ]
                    },
                    {
                        "description": gyeongbuk_notice_arr[6],
                        "thumbnail": {
                            "imageUrl": rand_thumb[6]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongbuk_url_arr[6]
                            }
                        ]
                    },
                    {
                        "description": gyeongbuk_notice_arr[7],
                        "thumbnail": {
                            "imageUrl": rand_thumb[7]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongbuk_url_arr[7]
                            }
                        ]
                    },
                    {
                        "description": gyeongbuk_notice_arr[8],
                        "thumbnail": {
                            "imageUrl": rand_thumb[8]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongbuk_url_arr[8]
                            }
                        ]
                    },
                    {
                        "description": gyeongbuk_notice_arr[9],
                        "thumbnail": {
                            "imageUrl": rand_thumb[9]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": gyeongbuk_url_arr[9]
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

    ###########################################################
    # csv 파일 불러오기
    jeonnam_notice = pd.read_csv("./app/data/Jeonnam_notice.csv")
    jeonnam_url = pd.read_csv("./app/data/Jeonnam_url.csv")

    # 값을 넣을 배열 선언
    jeonnam_notice_arr = [] # description에 들어갈 값
    jeonnam_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        jeonnam_url_arr.append(jeonnam_url.iloc[i]['url'])
        jeonnam_notice_arr.append(jeonnam_notice.iloc[i]['name'] + "\n공급유형 : " + jeonnam_notice.iloc[i]['title'] + "\n공고일자 : " + jeonnam_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "description": jeonnam_notice_arr[0],
                        "thumbnail": {
                            "imageUrl": rand_thumb[0]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonnam_url_arr[0]
                            }
                        ]
                    },
                    {
                        "description": jeonnam_notice_arr[1],
                        "thumbnail": {
                            "imageUrl": rand_thumb[1]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonnam_url_arr[1]
                            }
                        ]
                    },
                    {
                        "description": jeonnam_notice_arr[2],
                        "thumbnail": {
                            "imageUrl": rand_thumb[2]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonnam_url_arr[2]
                            }
                        ]
                    },
                    {
                        "description": jeonnam_notice_arr[3],
                        "thumbnail": {
                            "imageUrl": rand_thumb[3]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonnam_url_arr[3]
                            }
                        ]
                    },
                    {
                        "description": jeonnam_notice_arr[4],
                        "thumbnail": {
                            "imageUrl": rand_thumb[4]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonnam_url_arr[4]
                            }
                        ]
                    },
                    {
                        "description": jeonnam_notice_arr[5],
                        "thumbnail": {
                            "imageUrl": rand_thumb[5]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonnam_url_arr[5]
                            }
                        ]
                    },
                    {
                        "description": jeonnam_notice_arr[6],
                        "thumbnail": {
                            "imageUrl": rand_thumb[6]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonnam_url_arr[6]
                            }
                        ]
                    },
                    {
                        "description": jeonnam_notice_arr[7],
                        "thumbnail": {
                            "imageUrl": rand_thumb[7]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonnam_url_arr[7]
                            }
                        ]
                    },
                    {
                        "description": jeonnam_notice_arr[8],
                        "thumbnail": {
                            "imageUrl": rand_thumb[8]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonnam_url_arr[8]
                            }
                        ]
                    },
                    {
                        "description": jeonnam_notice_arr[9],
                        "thumbnail": {
                            "imageUrl": rand_thumb[9]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonnam_url_arr[9]
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

    ###########################################################
    # csv 파일 불러오기
    jeonbuk_notice = pd.read_csv("./app/data/Jeonbuk_notice.csv")
    jeonbuk_url = pd.read_csv("./app/data/Jeonbuk_url.csv")

    # 값을 넣을 배열 선언
    jeonbuk_notice_arr = [] # description에 들어갈 값
    jeonbuk_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        jeonbuk_url_arr.append(jeonbuk_url.iloc[i]['url'])
        jeonbuk_notice_arr.append(jeonbuk_notice.iloc[i]['name'] + "\n공급유형 : " + jeonbuk_notice.iloc[i]['title'] + "\n공고일자 : " + jeonbuk_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "description": jeonbuk_notice_arr[0],
                        "thumbnail": {
                            "imageUrl": rand_thumb[0]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonbuk_url_arr[0]
                            }
                        ]
                    },
                    {
                        "description": jeonbuk_notice_arr[1],
                        "thumbnail": {
                            "imageUrl": rand_thumb[1]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonbuk_url_arr[1]
                            }
                        ]
                    },
                    {
                        "description": jeonbuk_notice_arr[2],
                        "thumbnail": {
                            "imageUrl": rand_thumb[2]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonbuk_url_arr[2]
                            }
                        ]
                    },
                    {
                        "description": jeonbuk_notice_arr[3],
                        "thumbnail": {
                            "imageUrl": rand_thumb[3]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonbuk_url_arr[3]
                            }
                        ]
                    },
                    {
                        "description": jeonbuk_notice_arr[4],
                        "thumbnail": {
                            "imageUrl": rand_thumb[4]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonbuk_url_arr[4]
                            }
                        ]
                    },
                    {
                        "description": jeonbuk_notice_arr[5],
                        "thumbnail": {
                            "imageUrl": rand_thumb[5]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonbuk_url_arr[5]
                            }
                        ]
                    },
                    {
                        "description": jeonbuk_notice_arr[6],
                        "thumbnail": {
                            "imageUrl": rand_thumb[6]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonbuk_url_arr[6]
                            }
                        ]
                    },
                    {
                        "description": jeonbuk_notice_arr[7],
                        "thumbnail": {
                            "imageUrl": rand_thumb[7]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonbuk_url_arr[7]
                            }
                        ]
                    },
                    {
                        "description": jeonbuk_notice_arr[8],
                        "thumbnail": {
                            "imageUrl": rand_thumb[8]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonbuk_url_arr[8]
                            }
                        ]
                    },
                    {
                        "description": jeonbuk_notice_arr[9],
                        "thumbnail": {
                            "imageUrl": rand_thumb[9]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeonbuk_url_arr[9]
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

    ###########################################################
    # csv 파일 불러오기
    jeju_notice = pd.read_csv("./app/data/Jeju_notice.csv")
    jeju_url = pd.read_csv("./app/data/Jeju_url.csv")

    # 값을 넣을 배열 선언
    jeju_notice_arr = [] # description에 들어갈 값
    jeju_url_arr = [] # webLinkUrl에 들어갈 값

    # 반복문을 이용해 배열에 값 채워넣기
    for i in range(10) :
        jeju_url_arr.append(jeju_url.iloc[i]['url'])
        jeju_notice_arr.append(jeju_notice.iloc[i]['name'] + "\n공급유형 : " + jeju_notice.iloc[i]['title'] + "\n공고일자 : " + jeju_notice.iloc[i]['re_date'])
        
    # imageUrl에 들어갈 값 랜덤으로 섞기
    rand_thumb = random.sample(thumbnail_arr, 10)
    ###########################################################

    responseBody = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                        "description": jeju_notice_arr[0],
                        "thumbnail": {
                            "imageUrl": rand_thumb[0]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeju_url_arr[0]
                            }
                        ]
                    },
                    {
                        "description": jeju_notice_arr[1],
                        "thumbnail": {
                            "imageUrl": rand_thumb[1]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeju_url_arr[1]
                            }
                        ]
                    },
                    {
                        "description": jeju_notice_arr[2],
                        "thumbnail": {
                            "imageUrl": rand_thumb[2]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeju_url_arr[2]
                            }
                        ]
                    },
                    {
                        "description": jeju_notice_arr[3],
                        "thumbnail": {
                            "imageUrl": rand_thumb[3]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeju_url_arr[3]
                            }
                        ]
                    },
                    {
                        "description": jeju_notice_arr[4],
                        "thumbnail": {
                            "imageUrl": rand_thumb[4]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeju_url_arr[4]
                            }
                        ]
                    },
                    {
                        "description": jeju_notice_arr[5],
                        "thumbnail": {
                            "imageUrl": rand_thumb[5]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeju_url_arr[5]
                            }
                        ]
                    },
                    {
                        "description": jeju_notice_arr[6],
                        "thumbnail": {
                            "imageUrl": rand_thumb[6]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeju_url_arr[6]
                            }
                        ]
                    },
                    {
                        "description": jeju_notice_arr[7],
                        "thumbnail": {
                            "imageUrl": rand_thumb[7]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeju_url_arr[7]
                            }
                        ]
                    },
                    {
                        "description": jeju_notice_arr[8],
                        "thumbnail": {
                            "imageUrl": rand_thumb[8]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeju_url_arr[8]
                            }
                        ]
                    },
                    {
                        "description": jeju_notice_arr[9],
                        "thumbnail": {
                            "imageUrl": rand_thumb[9]
                        },
                        "buttons": [
                            {
                                "action":  "webLink",
                                "label": "자세히 보기",
                                "webLinkUrl": jeju_url_arr[9]
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