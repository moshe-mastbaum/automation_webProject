# from page_objects.electron_obj.task_page import TaskPage
from page_objects.web_obj.calculators_page import CalculatorsPage
from page_objects.web_obj.commission_cal_p import CommissionCal
from page_objects.web_obj.commission_explantion_p import CommissionEx
from page_objects.web_obj.effetiv_nominal_cal import EffectivNomonalCal
from page_objects.web_obj.exchanges_page import ExchangesPage
from page_objects.web_obj.main_page import MainPage
from page_objects.web_obj.monetary_page import MonetaryPage
#from test_cases.conftest import driver
import test_cases.conftest as conf
from page_objects.web_obj.top_area import Top
from page_objects.web_obj.about_page import About
from page_objects.web_obj.supervision_page import Supervision


# web_objects


# web_main = None
web_monetary = None
web_efct_nomin_cal = None
web_calculators = None
web_commission_explane = None
web_commission_cal = None
# web_exchanges = None

# electron objects
electron_task = None

class ManagePages:
    @staticmethod
    def init_web_pages():
        # globals()['web_main'] = MainPage(conf.driver)
        globals()['web_monetary'] = MonetaryPage(conf.driver)
        globals()['web_efct_nomin_cal'] = EffectivNomonalCal(conf.driver)
        globals()['web_calculators'] = CalculatorsPage(conf.driver)
        globals()['web_commission_explane'] = CommissionEx(conf.driver)
        globals()['web_commission_cal'] = CommissionCal(conf.driver)
        # globals()['web_exchanges'] = ExchangesPage(conf.driver)

    @staticmethod
    def init_electron_pages():
        globals()['electron_task'] = TaskPage(conf.driver)