import time

from selenium.webdriver.common.by import By

credit_crad = (By.ID, "SelectNoCardClient")
Senior_citizen = (By.ID, "SelectSeniorCitizen")
disability_client = (By.ID, "SelectDisabilityClient")
actions_by_clerk = (By.ID, "txtActionsByclerk")
direct_channel_actions = (By.ID, "txtDirectChannelActions")
commission_btn = (By.XPATH, '//*[@id="BoiCommissionsCalculatorBody"]/div[6]/a')
result_bank = (By.XPATH, )




class CommissionCal():
    def __init__(self, driver):
        self.driver = driver

    def cerdit_crad(self):
        time.sleep(0.5)
        return self.driver.find_element(credit_crad[0], credit_crad[1])

    def Senior_citizen(self):
        time.sleep(0.3)
        return self.driver.find_element(Senior_citizen[0], Senior_citizen[1])

    def disability_client(self):
        time.sleep(0.3)
        return self.driver.find_element(disability_client[0], disability_client[1])

    def actions_by_clerk(self):
        time.sleep(0.3)
        return self.driver.find_element(actions_by_clerk[0], actions_by_clerk[1])

    def direct_channel_actions(self):
        time.sleep(0.3)
        return self.driver.find_element(direct_channel_actions[0], direct_channel_actions[1])

    def commission_btn(self):
        time.sleep(1)
        return self.driver.find_element(commission_btn[0], commission_btn[1])

    def result_bank(self, bank_num):
        p="// table[ @class ='BoiCommissionsResult'] / tbody /tr["+bank_num+']/td'
        return self.driver.find_elements(commission_btn[0], p)

