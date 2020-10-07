import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# msg = input("enter a message: ")
# msg = "הודעה מספר "
contact = input("enter a contact name: ")
number = int(input("hoe much times do you want send the message? "))
message = input("enter the message: ")
driver = webdriver.Chrome(r"C:\Users\alonp\PycharmProjects\whatsapp\drivers\chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.get("https://web.whatsapp.com/")
time.sleep(20)
print("done")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(contact)
print("done1")
time.sleep(6)
# driver.find_element_by_class_name("_2kHpK").click()
print("done2")
for i in range(number):
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(message)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(Keys.ENTER)
    print(i)
    


time.sleep(300)
driver.close()

