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
import json



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
password.send_keys("Test123123")

# target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

time.sleep(3)
# # We are logged in!
# # alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

# 前進目標貼文網站

# target=['https://www.instagram.com/k.ht19/','https://www.instagram.com/houdong__/']
# filename=['椪柑','侯董']

target=['https://www.instagram.com/iceskycoldly/']
filename=['摩愛']

for item_target, item_filename  in zip(target,filename):

    driver.get(item_target)
    last_height = driver.execute_script("return document.body.scrollHeight")
    img_links = []
    anchors=[]
    prev_anchors = None


    while True:  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # 如果高度相同，那么已经到达底部
            print("Reached the bottom of the page")
            break
        last_height=new_height

    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)

    while True: 
        # 滾動一小段距離
        driver.execute_script("window.scrollTo(0, window.scrollY + 500);")
        time.sleep(3)  # 根據實際情況調整
        # 檢查新出現的鏈接
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'a')))  # 等待頁面元素加載
        # select all the anchor elements on the page

        soup=BeautifulSoup(driver.page_source,"html.parser")
        find_path=soup.find_all('a', class_='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd')
        for item in find_path:
            href = item.get('href')
            if href and href.startswith('/p'):
                full_url = 'https://www.instagram.com' + href
                anchors.append(full_url)
        
        # anchors = driver.find_elements(By.TAG_NAME, 'a')
        # # only keep their href attributes
        # anchors = [a.get_attribute('href') for a in anchors]
        # # filter links that do not start with instagram's prefix
        # anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]
        # # store outside the for loop

        if anchors == prev_anchors:
            print("No new links found. Exiting loop.")
            break
        else:
            img_links += anchors  # 如果不相同，則添加到 img_links
            prev_anchors = anchors  # 更新 prev_anchors 為當前迴圈的 anchors
            anchors=[]


    #     # 檢查是否到達頁面底部
    #     new_height = driver.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         scroll_attempt += 1
    #         # 如果多次滾動後高度未變，認為到達底部
    #         if scroll_attempt >= 3:  # 連續3次滾動高度未變化，認為到達底部
    #             break
    #     else:
    #         scroll_attempt = 0
    #         last_height = new_height

    unique_list = []
    for item in img_links:
        if item not in unique_list:
            unique_list.append(item)

    img_links=unique_list

    print('Found ' + str(len(img_links)) + ' links to images')
    print(img_links)
    text=[]

    for tag in img_links:
        driver.get(tag)
        time.sleep(5)

        # 下載html下來
        soup=BeautifulSoup(driver.page_source,"html.parser")

        # 定位, 這個輸出會是list
        find_path=soup.find_all('span',class_='x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj')
        tmp=[]
        tmp2=[]
        
    
        for h1 in find_path:
            # 获取每个 <h1> 标签的文本内容
            tmp.append(h1.get_text())


        content=tmp
        print(content)

        soup=BeautifulSoup(driver.page_source,"html.parser")
        find_path2=soup.find_all('img',class_='x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3', alt=False)
        for img in find_path2:
            if img.get('src').startswith('https://scontent'):
                tmp2.append(img.get('src'))

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


        unique_list2 = []
        for item in tmp2:
            if item not in unique_list2:
                unique_list2.append(item)

        picture=unique_list2

        dict_1={
            '照片':picture,
            '貼文內容':content
        }
        text.append(dict_1)
        print(dict_1)

    with open(f"{item_filename}.json", 'w', encoding='utf-8') as f:
        for item in text:
            formatted_data = json.dumps(item, indent=4, ensure_ascii=False)
            f.write(formatted_data + "\n")

input("ok")


