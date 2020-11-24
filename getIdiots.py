import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#get the @'s instead of

def get_tweets(browser): 
    body = browser.find_element_by_tag_name('body')
    userList = []
    while len(userList) < num_of_tweets:
        for _ in range(1):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
        # tweets += browser.find_elements_by_xpath("//div[@data-testid='tweet']")

        user = browser.find_element_by_class_name('css-1dbjc4n.r-18u37iz.r-1wbh5a2.r-1f6r7vd').text
        
        if user not in userList:
            userList.append(user)

        print(userList)

    return userList

def parse_and_save(userList, num_of_tweets, query):
    counter = 0
    column_separator = ","

    with open("idiotScraper_users_csv", 'w', newline='', errors='ignore') as file:
        fieldnames = ['User:']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for user in userList:
            writer.writerow({'User:': user})
            counter += 1

browser = webdriver.Chrome('H:\downloads\chromedriver_win32\chromedriver.exe');
base_url = "https://twitter.com/search?q="
query = '%23tft'
url = base_url + query
num_of_tweets = 25;

browser.get(url)
time.sleep(1)
tweets = get_tweets(browser)
parse_and_save(tweets, num_of_tweets, query)