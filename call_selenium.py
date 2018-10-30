from selenium import webdriver
import time
import sys
args=sys.argv

with open(str(args[2])+"\\footer_origin.html", "r",encoding="utf-8_sig") as f:
    lines=f.read().replace("----***----***----", str(args[1]))

with open(str(args[2])+"\\footer.html", "w",encoding="utf-8_sig") as f:
    f.write(lines)

driver = webdriver.Chrome("c:/driver/chromedriver.exe")
time.sleep(2)
driver.get("http://127.0.0.1:8080/app/index")
