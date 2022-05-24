import random
import pandas as pd
import csv

def pt() :
    a = "abcde"
    return a

thumbnail = pd.read_csv("./data/Thumbnail.csv")
thumbnail_arr = []
for i in range(10) :
    thumbnail_arr.append(thumbnail.iloc[i]['thumbnail'])
    
rand_thumb = random.sample(thumbnail_arr, 10)

print(rand_thumb[0])

rand_thumb = random.sample(thumbnail_arr, 10)

print(rand_thumb[0])