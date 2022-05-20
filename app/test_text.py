import pandas as pd
import csv

def pt() :
    a = "abcde"
    return a

seoul_notice = pd.read_csv("./data/Seoul_notice.csv")
seoul_url = pd.read_csv("./data/Seoul_url.csv")

print(seoul_notice.iloc[0]['name'] + "\n공급유형 : " + seoul_notice.iloc[0]['title'] + "\n공고일자 : " + seoul_notice.iloc[0]['re_date'])
print(seoul_url.iloc[0]['url'])