import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_tweets(browser): 
    body = browser.find_element_by_tag_name('body')
    tweets = []
    while len(tweets) < num_of_tweets:
        for _ in range(5):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
        # tweets = browser.find_elements_by_xpath("//div[@aria-label='Tijdlijn: Tijdlijn doorzoeken']")
        tweets = browser.find_elements_by_xpath("//div[@data-testid='tweet']")
    return tweets

def parse_and_save(tweets, num_of_tweets, query):
    counter = 0
    column_separator = ","

    with open("idiotScraper_users_csv", 'w', errors='ignore') as file:
        fieldnames = ['User:']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for tweet in tweets:
            if counter == num_of_tweets:
                break
            user = tweet.find_element_by_class_name('css-901oao').text

            writer.writerow({'User': user})
            counter += 1

browser = webdriver.Chrome('H:\downloads\chromedriver_win32\chromedriver.exe');
base_url = "https://twitter.com/search?q="
query = '%23twitch'
url = base_url + query
num_of_tweets = 5;

browser.get(url)
time.sleep(1)
tweets = get_tweets(browser)
parse_and_save(tweets, num_of_tweets, query)