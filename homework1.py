from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from gtts import gTTS
import time
import os


service_obj = Service('./chromedriver')
driver = webdriver.Chrome(service=service_obj)
url = "https://www.hko.gov.hk/tc/wxinfo/currwx/fnd.htm"
driver.get(url)
search = driver.find_element(By.CSS_SELECTOR, "#general_sit").text
search1 = driver.find_element(By.CLASS_NAME, 'contentArea').text
para = driver.find_element(By.XPATH, "//div[@class='border_blank']").text                          
'''print(search, search1)'''


print(search)
print("===============================================================")

text = search
# Cantonese Speech
tts = gTTS(text=text, lang='yue')
tts.save("text1.mp3")


# Mandarin Speech
tts = gTTS(text=text, lang='zh')

tts.save("text2.mp3")

print("---------------- Search 1-----------------------")
print(search1)
print("===============================================================")
print("----------------- Para -------------------------")
print(para)
os.system("mpg321 readme.mp3")
time.sleep(4)
os.system("mpg321 text1.mp3")
time.sleep(2)
os.system("mpg321 text2.mp3")
driver.close()
