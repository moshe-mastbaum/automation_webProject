from selenium.webdriver.common.by import By

intinf = (By.XPATH,'//*[@class="BoiInterestInflationTabs noindex"]/a[2]' )


class MonetaryPage():
    def __init__(self, driver):
        self.driver = driver

    def inflation(self):
        return self.driver.find_element(intinf[0], intinf[1])