from selenium.webdriver.common.by import By

logo = (By.XPATH, '//img[@alt="Bank Of Israel"]')
supervision = (By.CSS_SELECTOR, "a[href='/he/BankingSupervision/Pages/Default.aspx']")
about = (By.CSS_SELECTOR, "a[href='/he/AboutTheBank/Pages/Default.aspx']")

class Top():
    def __init__(self, driver):
        self.driver = driver

    def logo(self):
        return self.driver.find_element(logo[0], logo[1])

    def supervision(self):
        return self.driver.find_element(supervision[0], supervision[1])

    def about(self):
        return self.driver.find_element(about[0], about[1])


