from selenium import *
from selenium import webdriver
from selenium.webdriver import Firefox
import threading
import time
import re
def get_praise():
    browser = Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')

    browser.get("https://www.google.com/search?q=Lenovo IdeaPad 330")#.format(object_p)

    results = browser.find_elements_by_css_selector('div.g')
    href = []
    for result in results:
        link = result.find_element_by_tag_name("a")
        href.append(link.get_attribute("href"))

    iterator =0
    print(len(href))
    list_price = []
    for link in href:
        try:
        #time.sleep(5)
            browser.execute_script("window.open('');")
            browser.switch_to.window(browser.window_handles[iterator])  # Switch to the new window
            print(link)
            browser.get(link)
            print(browser.find_elements_by_css_selector('div'))
            iterator+=1
        except:
            print("Error: unable to start thread")
#object_p = input()
    print(list_price)
get_praise()

