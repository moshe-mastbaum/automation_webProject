from selenium.webdriver.common.by import By


datepicker = (By.ID, "txtRateDate")
year = (By.CLASS_NAME, "ui-datepicker-year")
month = (By.CLASS_NAME, "ui-datepicker-month")
search = (By.ID, "btnSearchRateDate")

class ExchangesPage():
    def __init__(self, driver):
        self.driver = driver

    def datepicker(self):
        return self.driver.find_element(datepicker[0], datepicker[1])

    def year(self):
        return self.driver.find_element(year[0], year[1])

    def month(self):
        return self.driver.find_element(month[0], month[1])

    def search(self):
        return self.driver.find_element(search[0], search[1])

    def day(self, day):
        return self.driver.find_element(By.LINK_TEXT, day)

    def exchange_rate(self, currency):
        xpath = "// table[1] / tbody / tr["+currency+"] / td[4] / div[2]"
        return self.driver.find_element(By.XPATH, xpath)