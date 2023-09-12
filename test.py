from selenium import webdriver
from selenium.webdriver.common.by import By
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    # Initialize a new browser instance using Chrome webdriver
    driver = webdriver.Chrome()

    # Navigate to Google's home page
    driver.get('https://www.betika.com/en-ke/login?next=%2F')
    driver.implicitly_wait(10)
    

    # Find the search box element and type "betika"
    #search_box = driver.find_element(By.NAME, 'q')
    #search_box.send_keys('betika')
    input_field = driver.find_element(By.XPATH, '//input[@type="text" and @placeholder="e.g. 0712 234567"]')
    input_field.send_keys("0705360334")
    
    password = driver.find_element(By.XPATH, '//input[@type="password"]')
   
    password.send_keys("juventus")

    login_button = driver.find_element(By.CLASS_NAME, "button")
    login_button.click()
    
    wait = WebDriverWait(driver, 10)
    new_page_element = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="text"]'))) 


except Exception as e:
    # Print the traceback information if an exception occurs
    traceback.print_exc()

finally:
    # Close the browser window
    wait = WebDriverWait(driver, 10)
    new_page_element = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="text"]'))) 
    driver.quit()
