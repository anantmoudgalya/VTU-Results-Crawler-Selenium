from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://www.expedia.com/")

driver.find_element(By.ID, "tab-flight-tab-hp").click()

driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")

time.sleep(2)

driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")

driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("03/19/2019")

driver.find_element(By.ID, "flight-returning-hp-flight")
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("03/21/2019")

driver.find_element(By.XPATH, "/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/div[7]/label/button").click()

wait = WebDriverWait(driver,10)

element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))

element.click()

time.sleep(3)

driver.quit()
#driver.find_element(By.XPATH, "//*[@id='stopFilter_stops-0']")