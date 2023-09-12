from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

CHROME_DRIVER_PATH = "C:/development/chromedriver"



class BetBot:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get('https://www.betika.com/en-ke/login?next=%2F')
        time.sleep(5)

        input_field = self.driver.find_element(By.XPATH, '//input[@type="text" and @placeholder="e.g. 0712 234567"]')
        input_field.send_keys("0705360334")

        password = self.driver.find_element(By.XPATH, '//input[@type="password"]')
   
        password.send_keys("juventus")

        time.sleep(2)
        login_button = self.driver.find_element(By.CLASS_NAME, "login")
        
        login_button.send_keys(Keys.ENTER)
    def place_bet(self):
        time.sleep(5)
        button_xpath = '//button[contains(@class, "prebet-match__odd") and ./span[number(text()) < 2.4]]'
        buttons = self.driver.find_elements(By.XPATH, button_xpath)
        for button in buttons:
            self.driver.execute_script("arguments[0].scrollIntoView();", button)
            self.driver.execute_script("arguments[0].click();", button)
        time.sleep(5)
        amount = self.driver.find_element(By.XPATH, '//input[@type="number" and @placeholder="Enters stake"]')
        amount.click()
        amount.send_keys(Keys.CONTROL + 'a')
        amount.send_keys(Keys.BACKSPACE)
        amount.send_keys("5")
        place_Bet = self.driver.find_element(By.CLASS_NAME, "button__primary")
        actions = ActionChains(self.driver)
        actions.click(place_Bet).perform()
        time.sleep(5)




bot = BetBot(CHROME_DRIVER_PATH)
bot.login()
bot.place_bet()