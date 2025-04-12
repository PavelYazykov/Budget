import allure

from common_methods.http_methods import HttpMethods
from common_methods.variables import CommonVariables


class TestPaymentInfoMethods:

    @staticmethod
    def create_payment_info(payment_info_id, wallet_id, access_token):
        with allure.step('XXXXXXXXXXXXXXXXX'):
            endpoint = f'/api/v1/payment_info/{payment_info_id}/'
            post_url = CommonVariables.base_url + endpoint
            body = {
                "wallet_id": wallet_id
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def get_payment_info_by_id(payment_info_id, access_token):
        with allure.step('XXXXXXXXXXXXXXXXX'):
            endpoint = f'/api/v1/payment_info/{payment_info_id}/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def delete_payment_info(access_token): # ВОЗМОЖНО КОСЯК ТАК КАК ДЕБТ ID НЕТ
        with allure.step('XXXXXXXXXXXXXXXXX'):
            endpoint = '/api/v1/payment_info/{debt_id}/'
            delete_url = CommonVariables.base_url + endpoint
            result = HttpMethods.delete(delete_url, access_token)
            return result

    @staticmethod
    def get_payment_info(access_token):
        endpoint = '/api/v1/payment_info/'
        get_url = CommonVariables.base_url + endpoint
        result = HttpMethods.get(get_url, access_token)
        return result
