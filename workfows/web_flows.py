import time

import allure

import utilities.manage_pages as page
from extentions.ui_actions import UiAction
from extentions.verifications import Verifications
from page_objects.web_obj import top_area
from utilities.common_ops import wait, For, change_window, scrollto, sett, clickjs
from workfows.api_flows import ApiFlows


class WebFlows:

    @staticmethod
    # @allure.step('show organizational Structure')
    def organizational_Structure(self):
        UiAction.click(page.Top.about(self))
        UiAction.click(page.About.structure(self))

    @staticmethod
    @allure.step('verify dollar rate - api')
    def dollar_rate_site_api(self):
        site_res= page.MainPage.dollar_rate(self).text[:4]
        api_res= ApiFlows.dollar_rate_boi(self)[:4]
        print(site_res,api_res)
        Verifications.verify_equals(site_res, api_res)

    @staticmethod
    @allure.step('get exchange rets of date')
    def exchange_rate(self, date):
        UiAction.click(page.MainPage.exchanges(self))
        UiAction.click(page.ExchangesPage.datepicker(self))
        UiAction.select1(page.ExchangesPage.year(self), int(date[0]))
        UiAction.select1(page.ExchangesPage.month(self), int(date[1]))
        UiAction.click(page.ExchangesPage.day(self, date[2]))
        UiAction.click(page.ExchangesPage.search(self))
        time.sleep(2)

    @allure.step('verify currncy rate')
    def verify_exchange_rate(self, currncy , expected):
        res = page.ExchangesPage.exchange_rate(self, currncy).text
        Verifications.verify_equals(res, expected)
        UiAction.click(page.Top.logo(self))

    @allure.step('find banks in city')
    def find_bank(self, city_num):
        UiAction.click(page.Top.supervision(self))
        clickjs(self, page.Supervision.branches(self))
        UiAction.click(page.Supervision.find_branche(self))
        UiAction.select1(page.Supervision.selectcity(self), city_num)
        time.sleep(1)

    @allure.step('verify num of banks in city')
    def verify_num_of_banks (self, expected):
        res =  str(len(page.Supervision.banks(self)))
        Verifications.verify_equals(res, expected)
        UiAction.click(page.Top.logo(self))

    @staticmethod
    @allure.step('convert effctiv interest to nominal')
    def efct_to_nomin(self, num):
        UiAction.click(page.MainPage.calculators(self))
        UiAction.click(page.CalculatorsPage.effetivnomianl(self))
        change_window(self, 1)
        UiAction.text_in(page.EffectivNomonalCal.effectivin(self), num)
        UiAction.click(page.EffectivNomonalCal.btnefctin(self))

    @staticmethod
    @allure.step('verify nominal output')
    def verify_nominal(self, expected):
        actual = page.EffectivNomonalCal.nominalout(self).get_attribute("value")
        print("expected is:",expected,"actual is:", actual)
        Verifications.verify_equals(actual, expected)
        self.driver.close()
        change_window(self, 0)
        UiAction.click(page.Top.logo(self))

    @staticmethod
    @allure.step('get commission of client')
    def commission_p(self, detials):
        UiAction.click(page.MainPage.calculators(self))
        UiAction.click(page.CalculatorsPage.commission(self))
        UiAction.click(page.CommissionEx.commission_cal(self))
        change_window(self, 1)
        UiAction.select1(page.CommissionCal.cerdit_crad(self), detials[0])
        UiAction.select1(page.CommissionCal.Senior_citizen(self), detials[1])
        UiAction.select1(page.CommissionCal.disability_client(self), detials[2])
        UiAction.text_in(page.CommissionCal.actions_by_clerk(self), detials[3])
        UiAction.text_in(page.CommissionCal.direct_channel_actions(self), detials[4])
        UiAction.click(page.CommissionCal.commission_btn(self))

    @staticmethod
    @allure.step('verify commission')
    def verify_commissions(self, bank_num, expected):
        res =  page.CommissionCal.result_bank(self, str(bank_num))
        actual_commissions = [res[1].text, res[2].text, res[3].text]
        print("expected is:", expected, "actual is:", actual_commissions)
        Verifications.verify_equals(actual_commissions, expected)
        self.driver.close()
        change_window(self, 0)
        UiAction.click(page.Top.logo(self))

