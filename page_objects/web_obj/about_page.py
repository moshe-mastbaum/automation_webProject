from selenium.webdriver.common.by import By


structure =(By.XPATH,'//form/div[4]/div/div/div/div[1]/div[1]/div/div[1]/div/ul/li[5]/a' )
# /he/AboutTheBank/OrganizationalStructure/Pages/Default.aspx

class About():
    def __init__(self, driver):
        self.driver = driver

    def structure(self):
        return self.driver.find_element(structure[0], structure[1])