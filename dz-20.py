from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.bing.com/translator")

select = Select(driver.find_element_by_id('tta_tgtsl'))
select.select_by_value('de')

elem = driver.find_element_by_id("tta_input_ta")
elem.clear()
elem.send_keys("hello world")
elem.send_keys(Keys.RETURN)
time.sleep(3)
elem_trans = driver.find_element_by_id("tta_output_ta")
text = elem_trans.get_attribute('value')

with open('translate.txt', 'a', encoding='utf-8') as f:
    f.write(text+'\n')
driver.close()