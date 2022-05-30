from selenium import webdriver
import chromedriver_autoinstaller
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./chromedriver/{chrome_ver}/chromedriver.exe', options = options)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./chromedriver/{chrome_ver}/chromedriver.exe', options = options)

driver.implicitly_wait(300)


#경로
url = 'C:\\chatbot\\'
myURL = 'https://www.myhome.go.kr/hws/portal/mtx/selectFixesSportView.do?tySe=FIXES100'
driver.get(myURL)

driver.find_element_by_xpath('//*[@id="MENU000003"]/img').click()
driver.find_element_by_xpath('//*[@id="srchPrgrStts_1"]/span').click()
driver.find_element_by_xpath('//*[@id="schMapDiv"]/div[1]/div[1]/div[2]/span[16]/a/img').click()
driver.find_element_by_xpath('//*[@id="frm"]/div[3]/span[1]').click()
time.sleep(10)

myhome_titles = driver.find_elements_by_css_selector(".al > a")
a = []
b = 0

detail_url = 'https://m.myhome.go.kr/hws/mbl/sch/selectRsdtLttotListView.do#detailPage?pblancId='

for i in myhome_titles:
    href = i.get_attribute('href')
    num1 = href[27:32]
    num = str(detail_url) + str(num1) + chr(38) + 'searchSe=R'
    a.append(num)
    b += 1
    print(b, num1)


df = pd.DataFrame((a), columns = ['url'])
print(df)

df.to_csv('./Jeonnam_url.csv', index = False, encoding='utf-8')