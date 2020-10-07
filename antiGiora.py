from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as pag
import datetime


def getHour():
    return str(datetime.datetime.now()).split()[1].split(":")[0]


def getMinute():
    if int(str(datetime.datetime.now()).split()[1].split(":")[1]) + 1 % 60 == 0:
        return str("00")
    elif int(str(datetime.datetime.now()).split()[1].split(":")[1]) + 1 < 10:
        return "0"+str(int(str(datetime.datetime.now()).split()[1].split(":")[1]) + 1)
    return str(int(str(datetime.datetime.now()).split()[1].split(":")[1]) + 1)


def disable():
    print(datetime.datetime.now())
    time.sleep(54)
    driver.find_element_by_xpath("//body/div/div/div/div/div/span/div/span/div/div/div/div[2]/div[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//li[2]//label[1]//input[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//body/div/div/span/div/div/div/div/div/div/div/div[2]").click()
    print(f"disabled at: {datetime.datetime.now()}")
    time.sleep(66)
    enable()


def enable():
    print(f"enabling at {datetime.datetime.now()}]")
    driver.find_element_by_xpath("//body/div/div/div/div/div/span/div/span/div/div/div/div[2]/div[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//li[1]//label[1]//input[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//body/div/div/span/div/div/div/div/div/div/div/div[2]").click()


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
    "check")
time.sleep(4)
driver.find_element_by_xpath("//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]").click()
time.sleep(2)
# enter the settings:
driver.find_element_by_xpath("//div[4]//div[1]//header[1]").click()
time.sleep(0.3)
driver.find_element_by_xpath("//body/div/div/div/div/div/span/div/span/div/div/div/div[4]/div[3]/div[1]").click()
running = True
last = "bla"
# main loop:

while running:

    if last != getHour() + ":" + getMinute():
        last = getHour() + ":" + getMinute()
        # option xx:xx:
        if getHour()[0] == getMinute()[0] == getHour()[1] == getMinute()[1]:
            disable()
        # option xy:xy:
        elif getHour()[0] == getMinute()[0] and getHour()[1] == getMinute()[1]:
            disable()
        # option xy:yx:
        elif getHour()[0] == getMinute()[1] and getHour()[1] == getMinute()[0]:
            disable()

        # option 12:34 and like this:
        elif int(getHour()[0]) + 1 == int(getHour()[1]) and int(getHour()[0]) + 2 == int(getMinute()[0]) and int(
                getHour()[0]) + 3 == int(getMinute()[1]) + 1:
            disable()
        # option xx:yy:
        elif getHour()[0] == getHour()[1] and getMinute()[0] == getMinute()[1]:
            disable()

    time.sleep(5)
driver.close()
