import json

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium import webdriver
import time

edge = webdriver.Edge()

edge.get('http://13.251.42.112:8800/admin/#/admin/xhs_app/crawlmedevice/')
# password  username el-button el-button--primary

edge.find_element(By.NAME, 'username').send_keys('ml_test')

edge.find_element(By.NAME, 'password').send_keys('jscDyKgpLe')

edge.find_element(By.CLASS_NAME, 'el-button').click()

edge.get('http://13.251.42.112:8800/admin/#/admin/xhs_app/crawlmedevice/')

handle = edge.window_handles

edge.switch_to.window(handle[-1])

infoButton = edge.find_element(By.XPATH, "//span[text()='200账号详情']")

# infoButton.click()
ActionChains(edge).move_to_element(infoButton).click(infoButton).perform()

edge.switch_to.default_content()

time.sleep(5)

table = edge.find_element(By.TAG_NAME, 'table')
# table = edge.find_element(By.ID, 'result_list')
tr = table.find_element(By.TAG_NAME, 'tr')

print(json.dumps(tr.text))

# with open("data.txt", 'w', encoding='utf-8') as f:
    # for i in tr:
    #     th = tr[i].find_element(By.TAG_NAME, 'th')
    #     f.write('th\n')