from instapy import InstaPy
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import schedule

IG_URL = 'http://instagram.com/'
TAG_URL = 'http://www.instagram.com/explore/tags/'


class Bot:
    def __init__(self):
        # options = webdriver.ChromeOptions()
        # options.add_argument("headless")
        # self.driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=options)
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')

    def login(self):
        self.driver.get(IG_URL)
        sleep(1)

    def enterUsernamePassword(self, username_input, password_input):
        username = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, "div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)")))
        username.click()
        username.send_keys(username_input)
        password = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, "div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)")))
        password.click()
        password.send_keys(password_input)
        btn_login = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
        btn_login.click()
        sleep(10)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        sleep(15)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()

    def getFollowersNumber(self, page_id):
        page_url = IG_URL + page_id
        self.driver.get(page_url)
        page_content = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#react-root > section > main")))
        slfw = BeautifulSoup(page_content.get_attribute('innerHTML'), 'html.parser')
        num_flw = slfw.findAll('span', {'class': 'g47SY'})
        num = num_flw[1].getText().replace(',', '')
        if 'k' in num:
            num = float(num[:-1]) * 1000
            return num
        elif 'm' in num:
            num = float(num[:-1]) * 1000000
            return num
        else:
            return float(num)


if __name__ == '__main__':
    bot = Bot()
    bot.login()
    bot.enterUsernamePassword(username_input='radiomusighi', password_input='Hosein_77')
    print(bot.getFollowersNumber("radiomusighi"))
