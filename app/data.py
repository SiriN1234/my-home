import pandas as pd
import csv

seoul_url = pd.read_csv("./data/Seoul_url.csv")
seoul_notice = pd.read_csv("./data/Seoul_notice.csv")

seoul_url_arr = []
seoul_notice_arr = []

for i in range(9) :
    seoul_url_arr.append(seoul_url.iloc[i]['url'])
    seoul_notice_arr.append(seoul_notice.iloc[0]['name'] + "\n공급유형 : " + seoul_notice.iloc[0]['title'] + "\n공고일자 : " + seoul_notice.iloc[0]['re_date'])