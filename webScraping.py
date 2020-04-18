import urllib.request
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as ps
import numpy as np

# chrome_options = Options()
# chrome_options.add_argument("--headless")

url = 'http://www15.plala.or.jp/gcap/disney/?fbclid=IwAR3kRauo1da4_n3SGpzz8pQAkP46o2OUkp2x70aVRxCjMhR4fobT7uKnHZ0'
# html = urllib.request.urlopen(url)

driver = webdriver.Chrome('C:/Users/Asus/Desktop/chromedriver')
driver.get(url)
time.sleep(2)


data_all = []
data_time = []

def number(date):
    for j in range(5, date):
        for i in range(0, 7):
            soup = bs(driver.page_source, 'html.parser')
            date = driver.find_element_by_xpath(f"/html/body/div[1]/div[3]/div[1]/div[3]/div[2]/div/table/tbody/tr[{j}]/td[{i+1}]/div[1]/div[1]")
            num = driver.find_element_by_xpath(f"/html/body/div[1]/div[3]/div[1]/div[3]/div[2]/div/table/tbody/tr[{j}]/td[{i+1}]/div[1]/div[2]")
            data_all.append(date.text)
            data_time.append(num.text)


for x in range(100):
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[3]/div[2]/div/table/tbody/tr[2]/td[1]/input").click()
    time.sleep(2)

for z in range(84):
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[3]/div[2]/div/table/tbody/tr[2]/td[3]/input").click()
    time.sleep(2)
    if z == 2 or z == 5 or z == 8 or z == 11 or z == 14 or z == 17 or z == 19 or z == 22 or z == 26 or z == 28 or z == 31 or z == 34 or z == 36 or z == 40 or z == 43 or z == 45 or z == 48 or z == 51 or z == 54 or z == 57 or z == 59 or z == 63 or z == 66 or z == 68 or z == 71 or z == 74 or z == 77 or z == 80 or z == 83:
        number(10)
    else:
        number(9)

list = []
year = 2012
for year in range(2012, 2019):
    if year == 2012 or year == 2016:
        for mon in range(1, 13):
            if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
                for day in range(1, 32):
                    time = pd.date_range(f'{year}/{mon}/{day}/8:15', f'{year}/{mon}/{day}/21:45', freq="30min")
                    list.append(time)
                    # day += 1
            if mon == 2:
                for day in range(1, 30):
                    time = pd.date_range(f'{year}/{mon}/{day}/8:15', f'{year}/{mon}/{day}/21:45', freq="30min")
                    list.append(time)
            if mon == 4 or mon == 6 or mon == 9 or mon == 11:
                for day in range(1, 31):
                    time = pd.date_range(f'{year}/{mon}/{day}/8:15', f'{year}/{mon}/{day}/21:45', freq="30min")
                    list.append(time)
    elif year == 2018:
        for mon in range(1, 13):
            if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 :
                for day in range(1, 32):
                    time = pd.date_range(f'{year}/{mon}/{day}/8:15', f'{year}/{mon}/{day}/21:45', freq="30min")
                    list.append(time)
                    # day += 1
            if mon == 2:
                for day in range(1, 29):
                    time = pd.date_range(f'{year}/{mon}/{day}/8:15', f'{year}/{mon}/{day}/21:45', freq="30min")
                    list.append(time)
            if mon == 4 or mon == 6 or mon == 9 or mon == 11:
                for day in range(1, 31):
                    time = pd.date_range(f'{year}/{mon}/{day}/8:15', f'{year}/{mon}/{day}/21:45', freq="30min")
                    list.append(time)
            if mon == 12:
                for day in range(1,30):
                    time = pd.date_range(f'{year}/{mon}/{day}/8:15', f'{year}/{mon}/{day}/21:45', freq="30min")
                    list.append(time)

    else:
        for mon in range(1, 13):
            if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
                for day in range(1, 32):
                    time = pd.date_range(f'{year}/{mon}/{day}/8:15', f'{year}/{mon}/{day}/21:45', freq="30min")
                    list.append(time)
                    # day += 1
            if mon == 2:
                for day in range(1, 29):
                    time = pd.date_range(f'{year}/{mon}/{day}/8:15', f'{year}/{mon}/{day}/21:45', freq="30min")
                    list.append(time)
            if mon == 4 or mon == 6 or mon == 9 or mon == 11:
                for day in range(1, 31):
                    time = pd.date_range(f'{year}/{mon}/{day}/8:15', f'{year}/{mon}/{day}/21:45', freq="30min")
                    list.append(time)
# list = pd.DataFrame(list)
# list = list.values
# df_time = np.reshape(list, (-1, 1), order='C')
# df_time = pd.DataFrame(df_time)  # 時間

data_all = pd.DataFrame(data_all)
data_time = pd.DataFrame(data_time)
data_all['num'] = data_time
data_all.rename(columns={'0': 'date'})
data_all.to_csv('data.csv', index=False)



# print(data_all)

    # for j in data:
    #     data_all.append(j.text)
# print(data_all)
# for i in range(31, -31):
# sort = data_all[-31]
# a = sort
# print(a)
    # print(f'data_all[{-i}]')

# data_all = pd.DataFrame(data_all)
# data_all.to_csv('data_try.csv', encoding='utf-8')



# date = []
# for x in data:
#     date.append(x.text.strip())
# print(date)
#
# driver.find_element_by_class_name("BOX")
# for tag in soup.find_all("td", {'class': 'JAM'}):
#     tag.to_csv('D:/file' + str(tag) + '.csv', encoding='utf-8-sig', index=False)

# for j in range(3):
#     driver.find_element_by_xpath("/html/body/div/div[3]/div/div[3]/table/tbody/tr[2]/td[1]/input").click()
#     driver.find_element_by_class_name("JAM").click()
#     for i in title:
#         driver.find_element_by_css_selector("td[id*='" + i + "']").click()
#         soap = driver.page_source
#         data = pd.read_html(soap)
#         a = data[22]
#         #print(a)
#         a.to_csv('D:/files/專題' + str(i)+'-'+str(j) + '.csv', encoding='utf-8-sig', index=False)



