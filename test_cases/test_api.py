
import allure
from extentions.db_actions import DbActions
from extentions.verifications import Verifications
from workfows.api_flows import ApiFlows



class Test_Api:

    @allure.title('create_and_verify_user')
    @allure.description('create_and_verify_user')
    def test_create_and_verify_user(self):
        data_test=DbActions.query_db(['name','job'],'create user')
        actual = ApiFlows.create_user(data_test[0][0], data_test[0][1])
        Verifications.verify_equals(actual, '201')


    @allure.title('test_verify_username')
    @allure.description('test_verify_username')
    def test_verify_username(self):
        data_test = DbActions.query_db(['id'], 'verify user name')
        actual = ApiFlows.get_username(data_test[0][0])
        Verifications.verify_equals(actual, 'Janet')

    @allure.title('test_update_user')
    @allure.description('test_update_user')
    def test_update_user(self):
        data_test = DbActions.query_db(['name','job','id'], 'update user')
        actual = ApiFlows.update_user(data_test[0][0],data_test[0][1],data_test[0][2])
        Verifications.verify_equals(actual, '200')

    @allure.title('test_delete_user')
    @allure.description('test_delete_user')
    def test_delete_user(self):
        data_test = DbActions.query_db(['id'], 'delete user')
        actual = ApiFlows.delete_user(data_test[0][0])
        Verifications.verify_equals(actual, '204')





