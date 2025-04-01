
from selenium import webdriver

import selenium

import time

# 指定EdgeDriver的路径
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_driver_path = 'E:\新建文件夹\edgedriver_win64.zip'  # 请替换为你的EdgeDriver实际路径

# 创建Edge浏览器实例
driver = webdriver.Edge()

driver.maximize_window()

driver.get('https://www.baidu.com')

# driver.find_element(By.NAME, 'wd').send_keys('selenium自动化')

# element = driver.find_element(By.ID, 'su')

# element.send_keys("aaaaaaaa")

# value = '111111'
# driver.execute_script("document.getElementById('su').value = arguments[0]", value)

print(driver.current_url)

# element = WebDriverWait(driver, 1).until(
#     EC.element_to_be_clickable((By.ID, "su"))
# )
# element.click()

driver.close()

driver.quit()