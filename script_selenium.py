from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.select import Select

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)


driver.get("http://127.0.0.1:8080/add")




input = driver.find_element(By.NAME, "title")
input.send_keys("Rambo III")
input = driver.find_element(By.NAME, "year")
input.send_keys("1988")
input = driver.find_element(By.NAME, "director")
input.send_keys("Peter MacDonald")
input = driver.find_element(By.NAME, "rating")
input.send_keys("4.70/10")
input = driver.find_element(By.NAME, "review")
input.send_keys("Sylvester Stallone later said his original premise of the film was more in keeping with the theme of Tears of the Sun, but set in Afghanistan.")

btm_enviar = driver.find_element(By.VALUE, "Grabar")
btm_enviar.click()
