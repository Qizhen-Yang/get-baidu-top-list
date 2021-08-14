# import libs
import requests
import csv
import time
from bs4 import BeautifulSoup

# getting content
# header settings
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36", 
         "Cookie": "your cookie"}
# original html code
baidu = requests.get("https://www.baidu.com", headers=header)
# get title and links
baidu_bs = BeautifulSoup(baidu.text, "html.parser")
baidu_top = baidu_bs.find_all("span", attrs = {'class': 'title-content-title'})

# time
date_and_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# writing into csv file
# open file
file = open("baidu_top.csv","a", encoding = 'utf-8', newline = "")
# csv writer
csv = csv.writer(file)
# content [date and time, string1, link1, string2, link2, ...]
csv_content = [date_and_time,
           baidu_top[0].string,
           baidu_top[1].string,
           baidu_top[2].string,
           baidu_top[3].string,
           baidu_top[4].string,
           baidu_top[5].string]
# write into file
csv.writerow(csv_content)
# print content
print("Added row:", csv_content)
# close file
file.close()