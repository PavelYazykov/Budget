import allure

from common_methods.http_methods import HttpMethods
from common_methods.variables import CommonVariables


class RegularOutcomeMethods:

    @staticmethod
    def create_regular_outcome(
            title, category_id, subcategory_id, period, amount, is_paid_off, date_of_next_pay, access_token
    ):
        with allure.step('Создание объекта регулярных списаний'):
            endpoint = '/api/v1/regular_outcome/'
            body = {
                "title": title,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "period": period,
                "amount": amount,
                "is_paid_off": is_paid_off,
                "date_of_next_pay": date_of_next_pay
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def get_regular_outcome(access_token):
        with allure.step('Получение списка всех регулярных списаний'):
            endpoint = 'access_token'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_regular_outcome_by_id(regular_outcome_id, access_token):
        with allure.step('Получение регулярных списаний по id'):
            endpoint = f'/api/v1/regular_outcome/{regular_outcome_id}/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def change_regular_outcome(
            regular_outcome_id, title, category_id, subcategory_id, period, amount, is_paid_off, access_token
    ):
        with allure.step('Измение регулярного списания по id'):
            endpoint = f'/api/v1/regular_outcome/{regular_outcome_id}/'
            body = {
                "title": title,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "period": period,
                "amount": amount,
                "is_paid_off": is_paid_off
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def delete_regular_outcome(regular_outcome_id, access_token):
        with allure.step('Удаление регулярного списания'):
            endpoint = f'/api/v1/regular_outcome/{regular_outcome_id}/'
            delete_url = CommonVariables.base_url + endpoint
            result = HttpMethods.delete(delete_url, access_token)
            return result

    @staticmethod
    def pay_regular_outcome(regular_outcome_id, wallet_id, access_token):
        with allure.step('Совершение оплаты по регулярному списанию'):
            endpoint = f'/api/v1/regular_outcome/pay_regular_outcome/{regular_outcome_id}/'
            body = {
                "wallet_id": wallet_id
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

