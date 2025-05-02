import allure
import psycopg2

from common_methods.http_methods import HttpMethods
from common_methods.variables import CommonVariables, DataBase


class PaymentInfoMethods:

    @staticmethod
    def post_pay_payment_info(payment_info_id, wallet_id, access_token):
        with allure.step('Оплата просроченного платежа'):
            endpoint = f'/api/v1/payment_info/{payment_info_id}/'
            post_url = CommonVariables.base_url + endpoint
            body = {
                "wallet_id": wallet_id
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def post_pay_payment_info_without_payment_info_id(wallet_id, access_token):
        with allure.step('Оплата просроченного платежа без поля payment_info_id'):
            endpoint = f'/api/v1/payment_info/'
            post_url = CommonVariables.base_url + endpoint
            body = {
                "wallet_id": wallet_id
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def post_pay_payment_info_without_body(payment_info_id, access_token):
        with allure.step('Оплата просроченного платежа без body'):
            endpoint = f'/api/v1/payment_info/{payment_info_id}/'
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post_without_body(post_url, access_token)
            return result

    @staticmethod
    def post_pay_payment_info_without_auth(payment_info_id, wallet_id):
        with allure.step('Оплата просроченного платежа без авторизации'):
            endpoint = f'/api/v1/payment_info/{payment_info_id}/'
            post_url = CommonVariables.base_url + endpoint
            body = {
                "wallet_id": wallet_id
            }
            result = HttpMethods.post_without_auth(post_url, body)
            return result

    @staticmethod
    def get_payment_info_by_id(payment_info_id, access_token):
        with allure.step('Запрос информации о платеже payment_info по id'):
            endpoint = f'/api/v1/payment_info/{payment_info_id}/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_payment_info_by_id_without_payment_info_id(access_token):
        with allure.step('Запрос информации о платеже payment_info по id без поля payment_info_id'):
            endpoint = f'/api/v1/payment_info/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def delete_payment_info(payment_info_id, access_token):
        with allure.step('Удаление просроченного платежа'):
            endpoint = f'/api/v1/payment_info/{payment_info_id}/'
            delete_url = CommonVariables.base_url + endpoint
            result = HttpMethods.delete(delete_url, access_token)
            return result

    @staticmethod
    def get_payment_info(access_token):
        with allure.step('Запрос информации о платежах payment_info'):
            endpoint = '/api/v1/payment_info/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_payment_info_with_params(payloads, access_token):
        with allure.step('Запрос информации о платежах payment_info с параметрами'):
            endpoint = '/api/v1/payment_info/'
            payloads = payloads
            get_url = CommonVariables.base_url + endpoint + payloads
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def create_payment_info_in_bd(regular_outcome_id, amount, debt_date, paid_off_date, is_paid_on_time, payment_info_id):
        with psycopg2.connect(
                host=DataBase.host,
                user=DataBase.user,
                password=DataBase.password,
                dbname=DataBase.dbname,
                port=DataBase.port
        ) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""INSERT INTO payment_info(
            regular_outcome_id, amount, debt_date, paid_off_date, is_paid_on_time, id)
            VALUES(%s, %s, %s, %s, %s, %s);""", (regular_outcome_id, amount, debt_date, paid_off_date, is_paid_on_time,
                                                 payment_info_id))
            connection.commit()

    @staticmethod
    def create_regular_outcome(date_of_next_pay, regular_outcome_id):
        with psycopg2.connect(
                host=DataBase.host,
                user=DataBase.user,
                password=DataBase.password,
                dbname=DataBase.dbname,
                port=DataBase.port
        ) as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""UPDATE regular_outcomes SET date_of_next_pay='{date_of_next_pay}' WHERE id='{regular_outcome_id}'"""
            )
            connection.commit()
