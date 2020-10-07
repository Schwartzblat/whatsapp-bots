from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as pag
import datetime


def getHour():
    return str(datetime.datetime.now()).split()[1].split(":")[0]


def getMinute():
    return str(datetime.datetime.now()).split()[1].split(":")[1]


def send(msg):
    driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div["
                                 "2]/div[1]/div[2]").send_keys(msg)
    driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[2]/div[1]/div[2]").send_keys(
        Keys.ENTER)


pag.FAILSAFE = False
chrome_options = Options()
chrome_options.add_argument("start-maximized")
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(r"C:\Users\alonp\PycharmProjects\whatsapp\drivers\chromedriver.exe",
                          options=chrome_options)

# enter whatsapp:
driver.set_page_load_timeout(10)
driver.get("https://web.whatsapp.com/")
time.sleep(15)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(
    "מסיבת טבע אצל יואל גבע")
time.sleep(5)
pag.click(1476, 433)
time.sleep(2)
running = True
last = "bla"
# main loop:
while running:

    if last != getHour()+":"+getMinute():
        last = getHour()+":"+getMinute()
        # option xx:xx:
        if getHour()[0] == getMinute()[0] == getHour()[1] == getMinute()[1]:
            send("סופר גיורא")
        # option xy:xy:
        elif getHour()[0] == getMinute()[0] and getHour()[1] == getMinute()[1]:
            send("גיורא")
        # option xy:yx:
        elif getHour()[0] == getMinute()[1] and getHour()[1] == getMinute()[0]:
            send("אריוג")

        # option 12:34 and like this:
        elif int(getHour()[0]) + 1 == int(getHour()[1]) and int(getHour()[0]) + 2 == int(getMinute()[0]) and int(
                getHour()[0]) + 3 == int(getMinute()[1]):
            send("אולטרה גיורא")
        # option xx:yy:
        elif getHour()[0] == getHour()[1] and getMinute()[0] == getMinute()[1]:
            send("אקסטרה גיורא")

    time.sleep(10)
driver.close()
