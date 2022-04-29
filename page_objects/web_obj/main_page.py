from selenium.webdriver.common.by import By

interestinf = (By.ID, "ctl00_PlaceHolderMain_BoiInterestViewer_moreAboutInterest")
calculators = (By.ID, "ctl00_PlaceHolderMain_BoiHPQuickLinks_QuickLinksRepeater_ctl03_serviceDiv")
exchanges = (By.ID, "ctl00_PlaceHolderMain_BoiCurrencyExchangeViewer_ToAllRates")
dollar_rate = (By.XPATH, '//*[@id="ctl00_PlaceHolderMain_BoiCurrencyExchangeViewer_table"]/tbody/tr[1]/td[2]')
class MainPage():
    def __init__(self, driver):
        self.driver = driver

    def exchanges(self):
        return self.driver.find_element(exchanges[0], exchanges[1])

    def interest_info(self):
        return self.driver.find_element(interestinf[0], interestinf[1])

    def calculators(self):
        return self.driver.find_element(calculators[0], calculators[1])

    def dollar_rate(self):
            return self.driver.find_element(dollar_rate[0], dollar_rate[1])

    def graph (self):
        return self.driver.find_element(By.ID, 'ctl00_PlaceHolderMain_BoiHPInflationViewer_chartdiv')

    def markets(self):
        return self.driver.find_element(By.XPATH, '//*[@id="ctl00_BoiMainNavigation_navigation"]/li[5]/a')
