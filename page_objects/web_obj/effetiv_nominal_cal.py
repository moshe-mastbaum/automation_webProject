from selenium.webdriver.common.by import By

# effectiveInput =(By.ID,'EffectiveInput' )
effectiveInput =(By.XPATH,'//*[@id="EffectiveInput"]' )
NominalOutput =(By.ID,'NominalOutput' )

btn_efctin = (By.CSS_SELECTOR, 'a[rel="Effective"]')
NominalInput =(By.ID,'NominalInput' )
EffectiveOutput =(By.ID,'EffectiveOutput' )
btn_nominin = (By.CSS_SELECTOR, 'a[rel="Nominal"]')


class EffectivNomonalCal():
    def __init__(self, driver):
        self.driver = driver

    def effectivin(self):
        return self.driver.find_element(effectiveInput[0], effectiveInput[1])

    def nominalout(self):
        return self.driver.find_element(NominalOutput[0], NominalOutput[1])

    def btnefctin(self):
        return self.driver.find_element(btn_efctin[0], btn_efctin[1])

    def nominalin(self):
        return self.driver.find_element(NominalInput[0], NominalInput[1])

    def effectivout(self):
        return self.driver.find_element(EffectiveOutput[0], EffectiveOutput[1])

    def btnnominin(self):
        return self.driver.find_element(btn_nominin[0], btn_nominin[1])