from selenium import webdriver
from bs4 import BeautifulSoup as Soup
from selenium.webdriver.chrome.service import Service
import time
import os
import urllib
import random

#connect to the imgur to search meme
s=Service('/usr/local/bin/chromedriver')
browser = webdriver.Chrome(service=s)
url = 'https://imgur.com/search?q=meme'
browser.get(url)

#for those who has slow network to prevaent the website haven't loaded
time.sleep(3)

#to get the html
page = browser.page_source
browser.quit()
#let html be pretty
soup = Soup(page,"html.parser")

#check if you have this dir here
if not os.path.exists("pic"):
    os.mkdir("pic")
    
#random choose the pics in the website
x = random.sample(range(50),10)
pic_numbers = 1

#put the pics into the dir
for i in x:
    pic = soup.find_all(class_="image-list-link")[i].img.get('src')
    urllib.request.urlretrieve('https:'+pic,os.path.join('your_dir','meme'+str(pic_numbers)))
    pic_numbers +=1
