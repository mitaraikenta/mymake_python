from selenium import webdriver
from selenium.webdriver.common.by import By

# まずはpip installしてね↓
# pip install selenium chromedriver-binary-aut
import os
import signal

#変数USERに学籍番号を入れてね
USER = ''
#変数PASSにパスワードを入れてね
PASS = ''
driver = webdriver.Chrome(executable_path="C:\chromedriver")

# 学校のURLをセット
driver.get('https://portal.nkz.ac.jp/portal/top.do')
# ユーザー名自動入力
elem_username  = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[1]/div[2]/form/ul/li[2]/input')
elem_username.send_keys(USER)
# パスワード自動入力
elem_password = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[1]/div[2]/form/ul/li[4]/input')
elem_password.send_keys(PASS)
# ログインボタン自動入力
logbutton = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[1]/div[2]/form/div[2]/input")
logbutton.click()
# 成績照会自動入力
grades = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[2]/div[3]/ul[2]/li[3]/a")
grades.click()

os.kill(driver.service.process.pid, signal.SIGTERM)