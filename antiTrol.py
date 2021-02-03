from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import threading
import sys
import os
import time

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def send(text):
    driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div["
                                 "2]/div[1]/div[2]").send_keys(text)
    driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[2]/div[1]/div[2]").send_keys(
        Keys.ENTER)


def kick():
    pos = getPos()
    action = webdriver.ActionChains(driver)
    action.move_to_element(to_element=driver.find_element_by_xpath(f"//body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/span[1]/div[1]/span[1]/div[1]/div[1]/div[1]/div[5]/div[4]/div[1]/div[{pos}]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]")).perform()
    time.sleep(0.1)
    driver.find_element_by_xpath(f"//body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/span[1]/div[1]/span[1]/div[1]/div[1]/div[1]/div[5]/div[4]/div[1]/div[{pos}]/div[1]/div[1]/div[2]/div[2]/div[2]/span[2]").click()
    time.sleep(0.1)
    driver.find_element_by_xpath("//body[1]/div[1]/div[1]/span[4]/div[1]/ul[1]/li[2]/div[1]").click()
    time.sleep(0.1)
    driver.find_element_by_xpath("//body[1]/div[1]/div[1]/span[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]").click()


def getPos():
    for i in range(20):
        try:
            name = driver.find_element_by_xpath(f"//body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/span[1]/div[1]/span[1]/div[1]/div[1]/div[1]/div[5]/div[4]/div[1]/div[{i}]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]").text
            if "להסיר" in name:
                return i
        except:
            pass
    return -1


def laughs():
    threading.Thread(target=kick).start()
    send("הבוט של ההנהלה לא רוצה אותך פה")
    send("האיום הוסר בהצלחה")

groupName = input("enter the group name: ")
chrome_options = Options()
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(resource_path("chromedriver.exe"),
                          options=chrome_options)

# enter whatsapp:
driver.get("https://web.whatsapp.com/")
time.sleep(15)
# search and enter the group:
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(groupName)
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(Keys.ENTER)
time.sleep(1)
# enter the settings:
driver.find_element_by_xpath("//div[4]//div[1]//header[1]").click()
time.sleep(0.6)
running = True
last="noder"

while last=="noder":
    try:
        elements = driver.find_elements_by_class_name("_1VzZY")
        elements = [message.text for message in elements]
        last=elements[-2]
        msg=last
    except:
        pass
# send("קבוצה זו מוגנת 24/7 על ידי הבוט של ההנהלה מפני טרולים")
counter=1
# main loop:
while running:
    try:
        elements = driver.find_elements_by_class_name("_1VzZY")
        elements = [message.text for message in elements]
        msg = elements[-2]
        if msg!=last:
            last=msg
            print(msg)
            if "להסיר" in msg and "הצטרף" in msg:
                threading.Thread(target=laughs).start()
                print(f"kicked {counter} trolls")
                counter+=1
    except:
        pass

driver.close()
