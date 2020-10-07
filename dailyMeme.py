from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def sendImg(filepath):
    try:
        driver.find_element_by_xpath('//div[@title = "הוספת קובץ"]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath(
            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]').send_keys(filepath)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body/div/div/div/div/div/span/div/span/div/div/div/span/div/div[1]').click()
    except:
        pass


def send(msg):
    driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div["
                                 "2]/div[1]/div[2]").send_keys(msg)
    driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[2]/div[1]/div[2]").send_keys(
        Keys.ENTER)


def getMeme():
    global src
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    driver1 = webdriver.Chrome(r"C:\Users\alonp\PycharmProjects\whatsapp\drivers\chromedriver.exe",
                               options=chrome_options)
    driver1.get("https://www.instagram.com/i.have.no.memes.96.v4/")
    time.sleep(1)
    driver1.find_element_by_xpath("//body//div//div//div//div//div//div[1]//div[1]//a[1]//div[1]//div[2]").click()
    time.sleep(1)
    driver1.find_element_by_name("username").send_keys("0507336650")
    driver1.find_element_by_name("password").send_keys("tkui2004")
    driver1.find_element_by_xpath("//body/div/div/div/div/div/div/div/div/form/div/div[3]").click()
    time.sleep(10)
    try:
        driver1.find_element_by_xpath("//body/div/section/main/div/div/div/div/button[1]").click()
    except:
        pass
    time.sleep(3)
    find_src = driver1.find_elements_by_xpath('//your_xpath')
    for my_src in find_src:
        src = my_src.get_attribute("src")
    driver1.find_element_by_xpath("//body//div//div//div//div//div//div[1]//div[1]//a[1]//div[1]//div[2]").click()
    imgLink = driver1.current_url

    time.sleep(3)
    # download the image:
    driver1.get("https://www.howtotechies.com/private-video-downloader")
    time.sleep(2)
    driver1.find_element_by_id("video-url").send_keys(imgLink)
    driver1.find_element_by_xpath("//body/div/div/article/form/div[1]/input[1]").click()
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--headless")
    driver2 = webdriver.Chrome(r"C:\Users\alonp\PycharmProjects\whatsapp\drivers\chromedriver.exe",
                               options=chrome_options)
    driver2.get(imgLink + "?__a=1")
    time.sleep(1)
    text = driver2.find_element_by_xpath("//html//body//pre").text
    time.sleep(1)
    driver2.close()

    driver1.find_element_by_xpath("//html//body//div//div//article//form//div//p//textarea").send_keys(text)
    driver1.find_element_by_xpath("//div[2]//input[1]").click()
    time.sleep(5)
    driver1.find_element_by_xpath("//html//body//div//div//article//button")
    time.sleep(1)
    driver2.close()
    return src.split("/")[7].split(".jpg")[0]


src = "hello"
chrome_options = Options()
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(r"C:\Users\alonp\PycharmProjects\whatsapp\drivers\chromedriver.exe",
                          options=chrome_options)
driver.get('https://web.whatsapp.com/')
time.sleep(10)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(
    "ניסיון")
time.sleep(4)
driver.find_element_by_xpath("//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]").click()
time.sleep(2)
path = getMeme()
time.sleep(1)
sendImg(rf"C:\Users\alonp\Downloads\{path}")
time.sleep(300)
driver.quit()
