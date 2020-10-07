import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
group = input("enter a group name: ")
number = int(input("hoe much people in the group? "))
driver = webdriver.Chrome(r"C:\Users\alonp\PycharmProjects\whatsapp\drivers\chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.get("https://web.whatsapp.com/")
time.sleep(15)
print("done")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(group)
print("done1")
time.sleep(5)
time.sleep(3)
for i in range(number):
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys("@")
    if(i!=0):
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_DOWN*i)
        actions.send_keys(Keys.ENTER)
        actions.perform()
    else:
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(Keys.ENTER)
time.sleep(300)
driver.close()
