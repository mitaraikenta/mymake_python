from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.common.by import By
import keyboard
import sys

driver = webdriver.Chrome(executable_path="C:\chromedriver")

# キーボードsボタンを押すと抜けるサイトが見れるよ！
# 親が来たらキーボードeボタンを押すことでブラウザを閉じることができる
while True:
    if keyboard.is_pressed("e"):
        sys.exit()
        break
    if keyboard.is_pressed("s"):
        # 抜けるサイト
        driver.get('https://jp.pornhub.com/')