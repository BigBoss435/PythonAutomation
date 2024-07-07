#Import selenium libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

url = "http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get(url)

source = driver.find_element(By.XPATH, "//*[@id='box3']")

destination = driver.find_element(By.XPATH, "//*[@id='box103']")

actions = ActionChains(driver)

actions.drag_and_drop(source, destination).perform()

sleep(5)

driver.quit()