from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from time import sleep

from secrets import face_email, face_password, cell_phone


class Tinder:
    def __init__(self):
        geo_allowed = webdriver.FirefoxOptions()
        geo_allowed.set_preference('geo.prompt.testing', True)
        geo_allowed.set_preference('geo.prompt.testing.allow', True)
        geo_allowed.set_preference('geo.provider.network.url',
                                   'data:application/json,{"location": {"lat": 51.47, "lng": 0.0}, "accuracy": 100.0}')
        self.web_driver = webdriver.Firefox(options=geo_allowed)

    def go_to_login_page(self):
        self.web_driver.get("http://tinder.com")

        sleep(5)

        if self.web_driver.find_element_by_xpath(
                "/html/body/div[2]/div/div/div/div/div[3]/span/div[2]/button/span[2]"
        ).text == "LOG IN WITH FACEBOOK":
            # case the second button is Facebook login
            self.click_face_login(facebook_xpath="/html/body/div[2]/div/div/div/div/div[3]/span/div[2]/button")
        else:
            # more options button case the second button is not Facebook login
            self.web_driver.find_element_by_xpath(
                "/html/body/div[2]/div/div/div/div/div[3]/span/button"
            ).click()
            self.click_face_login(facebook_xpath="/html/body/div[2]/div/div/div/div/div[3]/span/div[3]/button")

    def click_face_login(self, facebook_xpath):
        self.web_driver.find_element_by_xpath(
            facebook_xpath
        ).click()

        sleep(4)
        self.web_driver.switch_to_window(self.web_driver.window_handles[1])

    def check_element_exists(self, path):
        try:
            self.web_driver.find_element_by_xpath(path)
        except NoSuchElementException:
            return False
        return True

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

        if self.check_element_exists("/html/body/div[2]/div/div/div[1]/div[2]/div/input"):
            sleep(5)
            cell_phone_field = self.web_driver.find_element_by_xpath(
                "/html/body/div[2]/div/div/div[1]/div[2]/div/input"
            )

            cell_phone_field.send_keys(cell_phone)
            self.web_driver.find_element_by_xpath(
                "/html/body/div[2]/div/div/div[1]/button"
            ).click()
            self.web_driver.switch_to_window(self.web_driver.window_handles[0])
        self.tinder_home_page()

    def tinder_home_page(self):
        # allow use your geolocation
        sleep(4)
        self.web_driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div/div[3]/button[1]"
        ).click()

        # disable notification at web application
        self.web_driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div/div[3]/button[2]"
        ).click()
