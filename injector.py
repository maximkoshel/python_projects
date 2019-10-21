"""
Inject the word to translate into Google's translate website
if the user want more options for translation .

"""
import getpass
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def hebrew_to_english(word):
    driver = webdriver.Chrome(driverservice)
    driver.maximize_window()
    driver.get("https://translate.google.com/#view=home&op=translate&sl=iw&tl=en")
    search_input_box = driver.find_element_by_tag_name("textarea")
    search_input_box.send_keys(word)

def hebrew_to_russian(word):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://translate.google.com/#view=home&op=translate&sl=iw&tl=ru")
    search_input_box = driver.find_element_by_tag_name("textarea")
    search_input_box.send_keys(word)

def russian_to_hebrew(word):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://translate.google.com/#view=home&op=translate&sl=ru&tl=iw")
    search_input_box = driver.find_element_by_tag_name("textarea")
    search_input_box.send_keys(word)

def russian_to_english(word):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://translate.google.com/#view=home&op=translate&sl=ru&tl=en")
    search_input_box = driver.find_element_by_tag_name("textarea")
    search_input_box.send_keys(word)

def english_to_russian(word):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=ru")
    search_input_box = driver.find_element_by_tag_name("textarea")
    search_input_box.send_keys(word)

def english_to_hebrew(word):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=iw")
    search_input_box = driver.find_element_by_tag_name("textarea")
    search_input_box.send_keys(word)

def chrome_check_spelling(word):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://google.com")
    search_input_box = driver.find_element_by_name('q')
    search_input_box.send_keys(word)
    search_input_box.send_keys(Keys.ENTER)
