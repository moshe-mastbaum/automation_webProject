import allure
from extentions.api_actions import ApiActions
from xml.etree import ElementTree
# from utilities.common_ops import get_data
from utilities.common_ops import get_data

url = get_data("ApiUrl")
id ='2'
firstname= 'Janet'


class ApiFlows:

    @staticmethod
    @allure.step('get dollar rate from boi api')
    def dollar_rate_boi(self):
        response = ApiActions.get_dollar_rate()
        tree= ElementTree.fromstring(response.content)
        return tree[1][4].text



    @staticmethod
    @allure.step('extract value from response')
    def get_username(id):
        response = ApiActions.get(url+'/'+id)
        return ApiActions.extract_value_from_response(response, ['data','first_name'])

    @staticmethod
    @allure.step('create user')
    def create_user(name, job ):
        payload = {'name':name, 'job':job}
        status_code = ApiActions.post(url, payload)
        return status_code

    @staticmethod
    @allure.step('update user')
    def update_user(name, job, id ):
        payload = {'name':name, 'job':job}
        status_code = ApiActions.put(url+'/'+id, payload)
        return status_code

    @staticmethod
    @allure.step('delete user')
    def delete_user(id):
        status_code = ApiActions.delete(url+'/'+id)
        return status_code

