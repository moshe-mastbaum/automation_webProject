from selenium.webdriver.common.by import By

commission_cal = (By.CSS_SELECTOR, '#BoiWebPartZone2 > div > p > a > img')

class CommissionEx():
    def __init__(self, driver):
        self.driver = driver

    def commission_cal(self):
        return self.driver.find_element(commission_cal[0], commission_cal[1])
