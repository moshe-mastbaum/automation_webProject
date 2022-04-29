from selenium.webdriver.common.by import By


# branches = (By.CSS_SELECTOR, "li>a[href='/he/BankingSupervision/BanksAndBranchLocations/Pages/Default.aspx']")
branches = (By.XPATH, '//*[@id="BoiSideNav"]/li[10]/a')
find_branche = (By.XPATH, '//*[@id="BoiMultiLayerLatestUpdatesTab1"]/div/div/div/div[2]/div/div[1]/a')
selectcity = (By.ID, 'BoiBankCityName')
banks = (By.CLASS_NAME, 'BankBrachItem')
class Supervision():
    def __init__(self, driver):
        self.driver = driver

    def branches(self):
        return self.driver.find_element(branches[0], branches[1])

    def find_branche(self):
        return self.driver.find_element(find_branche[0], find_branche[1])

    def selectcity(self):
        return self.driver.find_element(selectcity[0], selectcity[1])

    def banks(self):
        return self.driver.find_elements(banks[0], banks[1])