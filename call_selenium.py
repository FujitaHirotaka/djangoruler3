from selenium import webdriver
import time


driver = webdriver.Chrome("c:/driver/chromedriver.exe")
time.sleep(5)
driver.get("http://127.0.0.1:8080/app/index")