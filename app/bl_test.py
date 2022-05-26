from flask import Blueprint
from flask import Flask, request, jsonify
import pandas as pd


app = Blueprint("blue_test", __name__)


@app.route("/api/blue_test", methods=['POST'])
def blue_test():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "블루프린트 테스트"
                    }
                }
            ]
        }
    }

    return responseBody