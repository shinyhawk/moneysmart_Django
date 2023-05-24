# PROJECT: MoneySmart
# AUTHOR: @superbaby81230
# CREATED: 14/5/2023
# MODIFIED: 21/5/2023

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
# from bs4 import BeautifulSoup


def get_cards(url):
    cardUriList = ['credit-cards', 'cash-back', 'air-miles', 'travel-overseas-spending', 'welcome-offer', 'online-shopping',
                   'annual-fee-waiver', 'unionpay', 'student', 'digital-wallets', 'business-card', 'octopus-card-aavs']

    # initialize the webdriver
    driver = webdriver.Chrome()
    # navigate to the webpage
    driver.get(url)
    i = 0
    # click "Load more" button amap
    moreButton = driver.find_elements("xpath", '//div[@class="pagination-button"]/button')
    
    while moreButton:
        driver.execute_script('arguments[0].click();', moreButton[0])
        # Delay 3s
        time.sleep(3)
        moreButton = driver.find_elements("xpath", '//div[@class="pagination-button"]/button')

    # find anchor with "More detail" text-it's class name ="link-toggle"
    details = driver.find_elements("xpath", '//a[@class="link-toggle"]')
     # print the contents of each element
    i = 0
    for element in details:
        i = i + 1
        print(i)
        #click buttons
        driver.execute_script('arguments[0].click();', element)
        # time.sleep(1)

    # Get card Data
    cards = driver.find_elements(By.CLASS_NAME, 'listing-card')

    data = []
    for i, card in enumerate(cards):
        try:
            img_src = card.find_element(
                'xpath', './/div[@class="listing-card__image"]//img').get_attribute("src")
        except NoSuchElementException:
            img_src = None
        try:
            disclosure = card.find_element(
                By.CLASS_NAME, 'listing-card__disclosure').text
        except NoSuchElementException:
            disclosure = None
        try:
            title = card.find_element(
                'xpath', './/h2[@class="listing-card__title"]').text
        except NoSuchElementException:
            title = None
        try:
            badge_execlusive = card.find_element(
                'xpath', './/div[@class="badge badge--exclusive"]//div[@class="badge__label"]').text
        except NoSuchElementException:
            badge_execlusive = None
        try:
            badge_label = card.find_element(
                'xpath', './/div[@class="badge"]//div[@class="badge__label"]').text
        except NoSuchElementException:
            badge_label = None
        try:
            badge_primary = card.find_element(
                'xpath', './/div[@class="badge badge--primary"]//div[@class="badge__label"]').text
        except NoSuchElementException:
            badge_primary = None
        try:
            snippet = card.find_element(
                'xpath', './/div[@class="promotion-snippet__content"]').get_attribute('innerHTML')
        except NoSuchElementException:
            snippet = None
        try:
            snippet_img = card.find_element(
                'xpath', './/div[@class="promotion-snippet__image"]//img').get_attribute("src")
        except NoSuchElementException:
            snippet_img = None

        card_usp = card.find_elements(By.CLASS_NAME, 'listing-card__usp-group')
        card_usp_data = []
        for i, element in enumerate(card_usp):
            card_usp_data.append({'ratio':  element.find_element('xpath', './/dd').text, 'text': element.find_element('xpath', './/dt').text})

        data.append({
            "img_src": img_src,
            "disclosure": disclosure,
            "title": title,
            "badge_execlusive": badge_execlusive,
            "badge_label": badge_label,
            "badge_primary": badge_primary,
            "snippet": snippet,
            "snippet_img": snippet_img,
            'usp': card_usp_data
        })

    driver.quit()
    return data

# def get_cash_back():
# for i, card in enumerate(cards):
#     card_image_src = card.find_element('xpath', '//div[@class="listing-card__image"]//img').get_attribute("src")
#     # card_state = card.find_element(By.CLASS_NAME, 'listing-card__disclosure').text
#     card_bonus1 = card.find_element('xpath', '//div[@class="badge badge--exclusive"]//div[@class="badge__label"]').text
#     card_bonus2 = card.find_element('xpath', '//div[@class="badge badge--primary"]//div[@class="badge__label"]').text
#     card_title = card.find_element('xpath', '//h2[@class="listing-card__title"]').text
#     card_promotion_snippet_content = card.find_element(By.CLASS_NAME, 'promotion-snippet__content').text
#     card_snipp_image = card.find_element('xpath', '//div[@class="promotion-snippet__image"]//img').get_attribute("src")
# card_usp = card.find_elements(By.CLASS_NAME, 'listing-card__usp-group')
# card_usp_data = []
# for i, element in enumerate(card_usp):
#     card_usp_data.append({'ratio':  element.find_element('xpath', '//dd').text, 'text': element.find_element('xpath', '//dt').text})
# card_promotion = card.find_element(By.XPATH, '//h2[@class="listing-card__title"]')
# print(card_promotion.text)




#     print(element.text)
#  # close the webdriver
