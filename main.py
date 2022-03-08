from encodings import utf_8
from time import time
from tkinter import Button
from selenium import webdriver
import time
import json
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
import selenium.webdriver.common.devtools.v98 as devtools
import re
# test = driver.execute_script("var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")

options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')
capabilities = DesiredCapabilities.CHROME
capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

driver = webdriver.Chrome("chromedriver.exe", desired_capabilities=capabilities, options=options)

driver.get("https://nadlan.taxes.gov.il/svinfonadlan2010/")
time.sleep(3)

driver.find_element(by='id' ,value='txtYeshuv').send_keys('חיפה')
time.sleep(0.5)
driver.find_element(by='id',value='txtRechov').send_keys('דרך הים')
time.sleep(0.5)
driver.find_element(by='id',value='Bayt').send_keys('209')
time.sleep(1)

select = Select(driver.find_element_by_id("ContentUsersPage_DDLTypeNehes"))
select.select_by_visible_text("דירת מגורים")
time.sleep(1)
select = Select(driver.find_element_by_id("ContentUsersPage_DDLMahutIska"))
select.select_by_visible_text("הכל")
time.sleep(1)


submit = driver.find_element(by="id",value="ContentUsersPage_btnHipus")
submit.click()
time.sleep(2)

logs = driver.get_log("performance")

data = json.load(logs, indent=4)

# for i in logs:
#     with open('data.txt', 'a', utf_8) as file:
#         file.writelines(i['message'])

# print(type(logs))
