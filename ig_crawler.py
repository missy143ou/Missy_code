from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from bs4 import BeautifulSoup as Soup
import pprint
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests
from selenium.webdriver import chrome
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
import json
import os


password = os.environ.get('MY_SECRET_PASSWORD', 'default_password')

# 建立driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 打開ig
driver.get("http://www.instagram.com")

# target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# enter username and password
username.clear()
username.send_keys("liamhsu0104")
password.clear()
password.send_keys(password)

# target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(3)

try:
    alert = driver.switch_to.alert
    alert.accept()  # 接受彈出視窗
    # 或者使用 alert.dismiss() 如果你想要拒絕彈出視窗
except NoAlertPresentException:
    pass  # 如果沒有彈出視窗就忽略

# # alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

# 前往目標網站
target=['https://www.instagram.com/iceskycoldly/']
filename=['摩愛']

for item_target, item_filename  in zip(target,filename):

    driver.get(item_target)
    last_height = driver.execute_script("return document.body.scrollHeight")
    img_links = []
    anchors=[]
    prev_anchors = None

    # 先滾動至最底
    while True:  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print("Reached the bottom of the page")
            break
        last_height=new_height

    # 回到原點
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)

    # 開始抓取(一小段一小段抓)
    while True: 
        # 滾動一小段距離
        driver.execute_script("window.scrollTo(0, window.scrollY + 500);")
        time.sleep(3)  
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'a')))  # 等待頁面元素加載
       
    #    抓取網址
        soup=BeautifulSoup(driver.page_source,"html.parser")
        find_path=soup.find_all('a', class_='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd')
        for item in find_path:
            href = item.get('href')
            if href and href.startswith('/p'):
                full_url = 'https://www.instagram.com' + href
                anchors.append(full_url)
        # 判斷是否到底部        
        if anchors == prev_anchors:
            print("No new links found. Exiting loop.")
            break
        else:
            img_links += anchors  # 如果不相同，則添加到 img_links
            prev_anchors = anchors  # 更新 prev_anchors 為當前迴圈的 anchors
            anchors=[]

    # 排除一樣的網址並依照順序排列
    unique_list = []
    for item in img_links:
        if item not in unique_list:
            unique_list.append(item)
    img_links=unique_list

    print('Found ' + str(len(img_links)) + ' links to images')
    print(img_links)
    text=[]

    # 開始抓取每個貼文的照片與內文
    for tag in img_links:
        driver.get(tag)
        time.sleep(5)
        tmp=[]
        tmp2=[]

        # 下載html下來
        soup=BeautifulSoup(driver.page_source,"html.parser")

        # 定位, 這個輸出會是list
        find_path=soup.find_all('span',class_='x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj')
        
        # 抓文章
        for h1 in find_path:
            tmp.append(h1.get_text())

        content=tmp
        print(content)

        # 抓貼文第一章照片
        soup=BeautifulSoup(driver.page_source,"html.parser")
        find_path2=soup.find_all('img',class_='x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3', alt=False)
        for img in find_path2:
            if img.get('src').startswith('https://scontent'):
                tmp2.append(img.get('src'))

        # 按按紐換照片直到沒得按為止, 過程中抓照片
        while True:
            try:
                button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='下一步']")))
                button.click()
                time.sleep(3)

                soup=BeautifulSoup(driver.page_source,"html.parser")
                find_path2=soup.find_all('img',class_='x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3', alt=False)
                for img in find_path2:
                    if img.get('src').startswith('https://scontent'):
                        tmp2.append(img.get('src'))

            except TimeoutException:
                break

        # 刪除重複的連結, 並依照順序排序
        unique_list2 = []
        for item in tmp2:
            if item not in unique_list2:
                unique_list2.append(item)
        picture=unique_list2

        # 設定字典
        dict_1={
            '照片':picture,
            '貼文內容':content
        }
        text.append(dict_1)
        print(dict_1)

    # 將所有貼文內容輸出出去
    with open(f"{item_filename}.json", 'w', encoding='utf-8') as f:
        for item in text:
            formatted_data = json.dumps(item, indent=4, ensure_ascii=False)
            f.write(formatted_data + "\n")

input("爬蟲結束, 按任意鍵結束")


