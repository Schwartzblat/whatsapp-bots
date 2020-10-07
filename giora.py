from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as pag
import random
import pickle


def check(input, array):
    for i in range(len(array)):
        if str(array[i]) in input:
            return True
    return False


def howMuchIn(str, char):
    times = 0
    for x in range(len(str)):
        if char == str[x]:
            times += 1
    return times


def doubleCheck(string):
    if len(string) > 40:
        return False
    count = 0
    arr = ["ג", "י", "ו", "ר"]
    for i in range(4):
        if howMuchIn(string, arr[i]) > 0:
            count += 1

    if count == 4:
        return True


def send(text):
    driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div["
                                 "2]/div[1]/div[2]").send_keys(text)
    driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[2]/div[1]/div[2]").send_keys(
        Keys.ENTER)


pag.FAILSAFE = False
driver = webdriver.Chrome(r"C:\Users\alonp\PycharmProjects\whatsapp\drivers\chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.get("https://web.whatsapp.com/")
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(15)
print("done")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(
    "מסיבת טבע אצל יואל גבע")
print("done1")
time.sleep(5)
pag.click(1476, 433)
time.sleep(2)
running = True
last = "bla"
counter = 0

messages = ["סתום תפה יבן שרמוטה", "כוסשלהאמא שלך זונה", "לך תדחוף גיורא לתחת", "יא בזבוז זרע", "מושפל מסכן",
            "לך תחפש תחברים שלך", "גיורא תקע את אמא שלך", "תמות מאיידס בביצים יא אפס", "סתום כבר ילד זין"]
giora = ["גיורא", "אריוג", "הריוג", "הריוג", "ארויג", "אריוג", "אוריג", "אורג", "ארגיו", "רויגה", "רויגא"]
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
while running:
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    try:
        msg_got = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
        msg = [message.text for message in msg_got][-1]
        if msg != last:
            print(msg)
            last = msg
            if check(str(msg), giora) or doubleCheck(msg):
                print("found")
                message = messages[random.randrange(0, len(messages))]
                print(f"the message is: {message}")
                send(message)
    except:
        pass
driver.close()
