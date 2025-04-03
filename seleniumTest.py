
from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.common.action_chains import ActionChains

import undetected_edgedriver as ue

import time

# 指定EdgeDriver的路径
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

edge = ue.Edge()
edgeDemo = edge.get('https://www.baidu.com')

edge_driver_path = 'E:\新建文件夹\edgedriver_win64.zip'  # 请替换为你的EdgeDriver实际路径

# 创建Edge浏览器实例
edge = driver = webdriver.Edge()

# driver.maximize_window()

driver.get('https://www.baidu.com')

# driver.execute_script("window.open('https://www.google.com')")
# time.sleep(5)

# driver.find_element(By.NAME, 'wd').send_keys('selenium自动化')

element = driver.find_element(By.ID, 'su')

# element.send_keys("aaaaaaaa")

# value = '111111'
# driver.execute_script("document.getElementById('su').value = arguments[0]", value)

driver.implicitly_wait(0.001)

print(driver.window_handles)

windowArray = driver.window_handles

driver.switch_to.window(windowArray[0])

# button = driver.switch_to.frame("su")
driver.switch_to.default_content()

driver.execute_script("alert(arguments[0])", "1")

alert = driver.switch_to.alert

alert.dismiss()

ActionChains(edge).move_to_element(element).send_keys("111").click(element).perform()

ActionChains(edge).context_click()

ActionChains(edge).click_and_hold()

ActionChains(edge).double_click()

button = driver.find_element(By.ID, 'su')

inp = driver.find_element(By.NAME, 'wd')

ActionChains(edge).drag_and_drop(button, inp)

# ActionChains(edge).drag_and_drop_by_offset()

ActionChains(edge).key_up(Keys.ENTER)

# ditu = driver.find_element(By.ID, 'mask')
# ActionChains.move_to_element(ditu).click_and_hold().move_by_offset(50,50).release().perform()

# driver.get_screenshot_as_file()
# driver.save_screenshot('F:\PycharmProjects\error\s.png')

s = driver.find_element(By.ID, 'ops')

ops = Select(s).options

Select(s).select_by_index(-1)
# element = WebDriverWait(driver, 1).until(
#     EC.element_to_be_clickable((By.ID, "su"))
# )
# element.click()

driver.close()

driver.quit()