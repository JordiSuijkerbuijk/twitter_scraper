import time
import csv
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

users = ['scarra', 'scarra']
browser = webdriver.Chrome('H:\downloads\chromedriver_win32\chromedriver.exe')
userId = []
text = 'Hey, im working on an expirement to find out what the best way is to create a following for a twitch channel using both social media and bots. If u are interested in gaming or programming i would appreciate it if u would follow my channel: twitch.tv/zolderraam'

def login(bowser): 
    browser.get('https://twitter.com/login')
    time.sleep(1)
    username = browser.find_element_by_css_selector("input[name='session[username_or_email]']")
    password= browser.find_element_by_css_selector("input[name='session[password]']")
    username.send_keys("zolderraam1")
    password.send_keys("Flameislame123")

    submit = browser.find_element_by_xpath("//div[@data-testid='LoginForm_Login_Button']")
    submit.click()


def get_user_ids(browser):
    # print(browser.find_element_by_xpath("//div[@data-testid='392513215-unfollow']"))
    time.sleep(1)
    userId = browser.find_element_by_xpath("//div[contains(@data-testid, 'follow')]")
    splitString = userId.get_attribute("data-testid").split("-", 1)
    messages(splitString[0])

def get_users():
    with open("idiotScraper_users_csv", 'r', errors='ignore') as file:
        reader = csv.reader(file, delimiter=',', quotechar='|')
        next(reader)
        for user in reader:
            browser.get('https://twitter.com/' + user[0])
            time.sleep(1)
            userId = get_user_ids(browser)

def messages(userId):
    browser.get('https://twitter.com/messages/' + userId + '-1330631224826748932?text=' + text)
    time.sleep(1)
    try:
        sent = browser.find_element_by_xpath("//div[@data-testid='dmComposerSendButton']")
        browser.execute_script("arguments[0].click();", sent)
        return True
    except:
        return False

#Skip user if there is no message button on the profile so it becomes faster
#find an way that i can get more tweets since right now at some point it stops getting all the tweets
#Might be able to create an better getIdiots function were we search an tag get all the users and then search another tag and do the same.
        
time.sleep(1)
login(browser)
users = get_users()