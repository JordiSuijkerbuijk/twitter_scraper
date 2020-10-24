import time
import csv
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

users = ['scarra', 'scarra']
browser = webdriver.Chrome('H:\downloads\chromedriver_win32\chromedriver.exe')
userId = []
text = 'I sent this using my bot..., its so fucking late... crack crack crack, i want to die'

def login(bowser): 
	browser.get('https://twitter.com/login')
	time.sleep(1)
	username = browser.find_element_by_css_selector("input[name='session[username_or_email]']")
	password= browser.find_element_by_css_selector("input[name='session[password]']")
	username.send_keys("input username")
	password.send_keys("input password")

	submit = browser.find_element_by_xpath("//div[@data-testid='LoginForm_Login_Button']")
	submit.click()


def get_user_ids(browser):
	# print(browser.find_element_by_xpath("//div[@data-testid='392513215-unfollow']"))
	time.sleep(1)
	userId = browser.find_element_by_xpath("//div[contains(@data-testid, 'follow')]")
	splitString = userId.get_attribute("data-testid").split("-", 1)
	messages(splitString[0])

def get_users():
	# with open("idiotScraper_users_csv", 'r', errors='ignore') as file:
	#     reader = csv.reader(file, delimiter=',', quotechar='|')
	#     for row in reader:
	#         print(row)
	for user in users:
		browser.get('https://twitter.com/' + user)
		time.sleep(1)
		userId = get_user_ids(browser)

def messages(userId):
	browser.get('https://twitter.com/messages/' + userId + '-1229336829465415680?text=' + text)
	time.sleep(1)
	sent = browser.find_element_by_xpath("//div[@data-testid='dmComposerSendButton']")
	browser.execute_script("arguments[0].click();", sent)

	#Check if i can open browser with cookies so my twitter stays logged in
	# if this is not possible make sure we log in using python



        
time.sleep(1)
login(browser)
users = get_users()