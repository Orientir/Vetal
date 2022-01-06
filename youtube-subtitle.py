from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

button_points = ("(//yt-icon-button[@class='dropdown-trigger style-scope ytd-menu-renderer']/button[@class='style-scope yt-icon-button'])", 'button.yt-icon-button')

def get_elements_by_css_selector(browser, css_selector):
    elements = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
    )
    return elements

def get_element_by_css_selector(browser, css_selector):
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
    )
    return element

def get_element_by_xpath_selector(browser, xpath_selector):
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_selector))
    )
    return element

youtube_link = input('Input youtube link: ')

browser = webdriver.Chrome()
browser.get(youtube_link)

#yt_icon_button = get_elements_by_css_selector(browser, "ytd-menu-renderer.style-scope ytd-video-primary-info-renderer>yt-icon-button.dropdown-trigger style-scope ytd-menu-renderer>button.style-scope yt-icon-button")[0]
try:
    # yt_icon_button = browser.find_element_by_css_selector('button.yt-icon-button')
    try:
        yt_icon_button = get_element_by_css_selector(browser, button_points[1])
    except:
        yt_icon_button = get_element_by_xpath_selector(browser, button_points[0])
    time.sleep(3)
    browser.execute_script("arguments[0].click();", yt_icon_button)
    time.sleep(5)

    # ytd-menu-service-item-renderer class="style-scope ytd-menu-popup-renderer"
    # ytd_menu_service = browser.find_element_by_css_selector('ytd-menu-service-item-renderer.ytd-menu-popup-renderer')
    # ytd_menu_service = browser.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-menu-popup-renderer/tp-yt-paper-listbox/ytd-menu-service-item-renderer")
    ytd_menu_service = get_element_by_css_selector(browser, 'ytd-menu-service-item-renderer.ytd-menu-popup-renderer')
    browser.execute_script("arguments[0].click();", ytd_menu_service)
    print('CLICK')
    time.sleep(5)
    # panels = get_elements_by_css_selector(browser, 'ytd-transcript-body-renderer.ytd-transcript-renderer>div.ytd-transcript-body-renderer')
    # cue style-scope ytd-transcript-body-renderer active
    panels = browser.find_elements_by_css_selector(
                                          'ytd-transcript-body-renderer.ytd-transcript-renderer>div>div.cues>div.cue')
    for text in panels:
        print(text.text)
except Exception as e:
    print('EXCEPTION ', e)
browser.close()
# style-scope yt-icon-button
# subtitle = resp.html.xpath('//div[@class="style-scope ytd-engagement-panel-section-list-renderer"]/div[@class="cue-group"]')
# print(len(subtitle))
# pp(subtitle)
