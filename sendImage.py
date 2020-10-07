from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("start-maximized")
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(r"C:\Users\alonp\PycharmProjects\whatsapp\drivers\chromedriver.exe",
                          options=chrome_options)
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
filepath = input('Enter your filepath (images/video): ')

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
sleep(5)
attachment_box = driver.find_element_by_xpath('//div[@title = "הוספת קובץ"]')
attachment_box.click()
sleep(5)
image_box = driver.find_element_by_xpath(
    '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(filepath)

sleep(3)

send_button = driver.find_element_by_xpath('//body/div/div/div/div/div/span/div/span/div/div/div/span/div/div[1]')
send_button.click()