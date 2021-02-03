from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

groupName1 = input("enter the first group name: ")
groupName2 = input("enter the second group name: ")

chrome_options = Options()
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(resource_path("chromedriver.exe"),
                          options=chrome_options)

# enter whatsapp:
driver.get("https://web.whatsapp.com/")
time.sleep(20)
# search and enter the group:
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(groupName1)
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(Keys.ENTER)
time.sleep(3)
first = ""
while "את/ה" not in first:
    first = str(
        driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[2]/span[1]").text)

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(groupName2)
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(Keys.ENTER)
time.sleep(3)
second=""
while "את/ה" not in second:
    second = str(
        driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[2]/span[1]").text)

driver.close()

for name1 in first.split(", "):
    for name2 in second.split(", "):
        if name1 == name2 and name1 != "את/ה":
            print(name1)
print("alon the king")
