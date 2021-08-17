from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
#
# driver = webdriver.Chrome()
# #driver.set_page_load_timeout(50)
# #driver.set_script_timeout(9) #Both settings are effective
# driver.get("https://www.python.org")
# sleep(3)
# print(driver.title)
# search_bar = driver.find_element_by_name("q")
# sleep(3)
# search_bar.clear()
# sleep(3)
# search_bar.send_keys("getting started with python")
# sleep(3)
# # finding the button using ID
# button = driver.find_element_by_id('submit')
# sleep(3)
#
# # clicking on the button
# button.click()
# sleep(3)
# #search_bar.send_keys(Keys.RETURN)
# print(driver.current_url)
# driver.close()


fp = webdriver.Chrome()
fp.set_preference("http.response.timeout", 5)
fp.set_preference("dom.max_script_run_time", 5)
driver = webdriver.Chrome(profile=fp)

driver.get("https://www.python.org")
sleep(3)
print(driver.title)
search_bar = driver.find_element_by_name("q")
sleep(3)
search_bar.clear()
sleep(3)
search_bar.send_keys("getting started with python")
sleep(3)
# finding the button using ID
button = driver.find_element_by_id('submit')
sleep(3)

# clicking on the button
button.click()
sleep(3)
#search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()