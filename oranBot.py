import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as pag
import random


def check(msg, giora):
    for i in range(len(giora)):
        if str(giora[i]) in msg:
            return True
    return False


def checkNumLoaded():
    for i in range(100):
        try:
            lastMsg = driver.find_element_by_xpath(
                f"//div[{i}]//div[1]//div[1]//div[1]//div[1]//div[1]//span[1]//span[1]")
        except:
            return i


pag.FAILSAFE = False
driver = webdriver.Chrome(r"C:\Users\alonp\PycharmProjects\whatsapp\drivers\chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.get("https://web.whatsapp.com/")
time.sleep(15)
print("done")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(
    "שביעיסטים חורבן")
print("done1")
time.sleep(5)
pag.click(1476, 433)
time.sleep(2)
running = True
last = "bla"
counter = 0
send = "ח"
while running:
    try:
        msg_got = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
        msg = [message.text for message in msg_got][-1]
        if msg != last:
            print(msg)
            last = msg
            counter += 1
        if counter % 6 == 0:

            driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div["
                                         "2]/div[1]/div[2]").send_keys(send)
            driver.find_element_by_xpath(
                "/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[2]/div[1]/div[2]").send_keys(
                Keys.ENTER)
            send = send + "ח"
    except:
        pass
driver.close()
