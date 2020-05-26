from selenium import webdriver
from time import sleep

from secrets import face_email, face_password


class Tinder:
    def __init__(self):
        self.web_driver = webdriver.Firefox()

    def go_to_login_page(self):
        self.web_driver.get("http://tinder.com")

        sleep(5)

        facebook_btn = self.web_driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div/div[3]/span/div[2]/button"
        )
        facebook_btn.click()

        # switch to facebook login popup
        self.web_driver.switch_to_window(self.web_driver.window_handles[1])

    def login(self):
        email = self.web_driver.find_element_by_xpath(
            "//*[@id='email']"
        )
        email.send_keys(face_email)

        password = self.web_driver.find_element_by_xpath(
            "//*[@id='pass']"
        )
        password.send_keys(face_password)

        login_btn = self.web_driver.find_element_by_xpath(
            "//*[@id='u_0_0']"
        )
        login_btn.click()

        self.web_driver.switch_to_window(self.web_driver.window_handles[0])


if __name__ == '__main__':
    bot = Tinder()
    bot.go_to_login_page()
    bot.login()
