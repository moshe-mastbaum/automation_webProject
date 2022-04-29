import time
import allure
import pytest
from utilities.common_ops import get_data
from workfows.web_flows import WebFlows
import test_cases.conftest as conf


@pytest.mark.usefixtures('init_web_driver')
class Test_web:
    @allure.title('exchange rate')
    @allure.description('currncy in rate out')
    def test_exchange_rates(self):
        date = get_data('Date').split(",")
        WebFlows.exchange_rate(self, date)
        WebFlows.verify_exchange_rate(self, get_data('Currncy'), get_data('Expected_rate'))

    @allure.title('dollar rate')
    @allure.description('compere rate in web to rate in api')
    def test_dolar_rate(self):
        WebFlows.dollar_rate_site_api(self)

    @allure.title('find bank')
    @allure.description('city in number of banks in this city out')
    def test_find_bank(self):
        WebFlows.find_bank(self, int(get_data('City_num')))
        WebFlows.verify_num_of_banks(self, get_data('Expected_num_of_banks'))

    @allure.title('effctiv nomial cal')
    @allure.description('effctiv in nomial out')
    def test_effective_nominal_cal(self):
        WebFlows.efct_to_nomin(self, get_data('Efct_in'))
        WebFlows.verify_nominal(self, get_data('Expected_nom'))

    @allure.title('commission cal')
    @allure.description('client details in commissons out')
    def test_commission_cal(self):
        details = get_data('Details_commisson').split(",")
        WebFlows.commission_p(self, details)
        WebFlows.verify_commissions(self, int(get_data('Bank_num')), get_data('Expected_commissions'))

    @allure.title('visual testing')
    @allure.description('visual testing')
    def test_verify_visual(self):
        conf.eyes.open(self.driver, "visual12", "visual13")
        WebFlows.organizational_Structure(self)
        conf.eyes.check_window('main page')
