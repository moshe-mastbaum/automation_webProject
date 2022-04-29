import mysql.connector
import allure
import requests

mydb = mysql.connector.connect(
    host="remotemysql.com",
    database='v8d1uEhQPT',
    user="v8d1uEhQPT",
    password="COcVfGEIux"
)

class DbActions:
    @staticmethod
    @allure.step('get raquest')
    def query_db(columns,key):
        cols = ','.join(columns)
        query = 'SELECT '+ cols +' FROM '+'db_for_api_test'+' WHERE '+'testkey'+'='+"'"+key+"'"
        my_cursor = mydb.cursor()
        my_cursor.execute(query)
        my_result = my_cursor.fetchall()
        return my_result
