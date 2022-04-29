import time
import allure
import pytest
import selenium
from applitools.selenium import Eyes
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.common_ops import get_data, get_timestamp
from utilities.manage_pages import ManagePages

driver = None
action = None
eyes = Eyes()
web_driver = get_data('Browser')

@pytest.fixture(scope='class')
def init_web_driver(request):
    edriver = get_webdriver()
    globals()['driver']= edriver
    driver=globals()['driver']
    globals()['action'] = ActionChains(driver)
    driver.maximize_window()
    driver.implicitly_wait(int(get_data('WaitTime')))
    driver.get(get_data('Url'))
    request.cls.driver = driver
    ManagePages.init_web_pages()
    eyes.api_key='LsCdrGdLqJnIx6AKPDs9rEW1QgFamvze2H0aK5aIx2E110'
    yield
    driver.quit()

def get_webdriver():
    if web_driver.lower() == 'chrome':
        return webdriver.Chrome(ChromeDriverManager().install())
    if web_driver.lower() == 'firefox':
        return webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    if web_driver.lower() == 'edge':
        return webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    else:
        raise Exception('unrecognized browser')


def pytest_exception_interact(node, call, report):
    image = get_data('ScreenshotPath')+'screen'+str(get_timestamp())+'.png'
    if globals()['driver']:
        globals()['driver'].get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)


