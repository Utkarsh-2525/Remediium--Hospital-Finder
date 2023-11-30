from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

x = input()




options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)

# import requests
# #specify the url we want to scrape from
# Link = "https://www.google.com/maps/search/itching+hospitals/@26.5121452,80.1879258,13z/data=!3m1!4b1"
# #convert the web page to text
# Link_text = requests.get(Link)
# soup = BeautifulSoup(Link_text.text, "html.parser")
# our_table = soup.find_all('div')
# print(our_table)
st = "https://www.google.com/maps/search/"
st+=x
st+="+hospitals"
driver.get(st)

ls=driver.find_elements(By.CLASS_NAME,'hfpxzc')
for i in ls:
    print(i.get_attribute('aria-label'))
    print("\n")


print(review_titles.text)