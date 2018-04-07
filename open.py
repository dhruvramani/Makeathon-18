import time
from nltkrun import classify
from html.parser import HTMLParser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MLStripper(HTMLParser):
    
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def send_message(target, string):
    x_arg = '//span[contains(@title,' + target.lower() + ')]'
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()
    message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    message.send_keys(string)
    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/button')[0]
    sendbutton.click()

def mainMessage(sleep=0):
    time.sleep(sleep)
    rightChatBoxes = driver.find_elements_by_css_selector(".CxUIE")

    i = 1
    for rightChatBox in rightChatBoxes:
        chatHead = driver.find_elements_by_css_selector("._3zmhL")[0]
        no_messages = int(chatHead.text)

        rightChatBox.click()

        if i == 1:
            time.sleep(sleep)
            i = i+1

        messages = driver.find_elements_by_css_selector(".ZhF0n")[-no_messages:]

        for message in messages:
            mess = strip_tags(message.text)
            group_name = "'" + classify(mess)[0] + "'"
            print(mess)

            send_message(group_name, mess)
            alert1 = driver.SwitchTo().Alert()
            alert1.Accept()


driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
time.sleep(2)

count = 10
while 1:
    mainMessage(count)
    time.sleep(1)
    count = 0

time.sleep(10)
driver.quit()
