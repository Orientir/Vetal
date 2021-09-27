from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.bing.com/translator")

select = Select(driver.find_element_by_id('tta_tgtsl'))
select.select_by_value('de')

print(select, 'select')

elem = driver.find_element_by_id("tta_input_ta")
print(elem, 'elem')
elem.clear()
elem.send_keys("hello world")
elem.send_keys(Keys.RETURN)
time.sleep(3)
elem_trans = driver.find_element_by_id("tta_output_ta")
print(elem_trans, 'trans')
text = elem_trans.get_attribute('value')
print(text)
driver.close()