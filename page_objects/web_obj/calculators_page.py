from selenium.webdriver.common.by import By

effetivnomianl = (By.XPATH,'//div[@class="WpBody"][1]//tr[2]//a' )
commission = (By.XPATH, '//*[@id="BoiWebPartZone4"]/div[2]/table/tbody/tr[1]/td[2]/p/strong/a' )


class CalculatorsPage():
    def __init__(self, driver):
        self.driver = driver

    def effetivnomianl(self):
        return self.driver.find_element(effetivnomianl[0], effetivnomianl[1])

    def commission(self):
        return self.driver.find_element(commission[0], commission[1])