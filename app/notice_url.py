import pandas as pd
import csv

seoul_url = pd.read_csv("./data/Seoul_url.csv")
seoul_notice = pd.read_csv("./data/Seoul_notice.csv")

seoul_url_arr = []
seoul_notice_arr = []

for i in range(10) :
    seoul_url_arr.append(seoul_url.iloc[i]['url'])
    seoul_notice_arr.append(seoul_notice.iloc[i]['name'] + "\n공급유형 : " + seoul_notice.iloc[i]['title'] + "\n공고일자 : " + seoul_notice.iloc[i]['re_date'])


def seoul_notice_return(n) :
    return seoul_notice_arr[n]

def seoul_url_return(n) :
    return seoul_url_arr[n]