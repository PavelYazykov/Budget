import json

import allure

from common_methods.http_methods import HttpMethods
from common_methods.variables import CommonVariables


class CurrencyMethods:
    @staticmethod
    def get_currency(access_token):
        with allure.step('Получение списка валют'):
            endpoint = '/api/v1/currency/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_currency_without_auth():
        with allure.step('Получение списка валют'):
            endpoint = '/api/v1/currency/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get_without_auth(get_url)
            return result

    @staticmethod
    def create_currency(code, full_title, short_title, access_token):
        with allure.step('Создание валюты'):
            endpoint = '/api/v1/currency/'
            post_url = CommonVariables.base_url + endpoint
            body = {
                "code": code,
                "full_title": full_title,
                "short_title": short_title
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_currency_without_short_title(code, full_title, access_token):
        with allure.step('Создание валюты без поля short_title'):
            endpoint = '/api/v1/currency/'
            post_url = CommonVariables.base_url + endpoint
            body = {
                "code": code,
                "full_title": full_title
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_currency_without_full_title(code, short_title, access_token):
        with allure.step('Создание валюты  без поля full_title'):
            endpoint = '/api/v1/currency/'
            post_url = CommonVariables.base_url + endpoint
            body = {
                "code": code,
                "short_title": short_title
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_currency_without_code(full_title, short_title, access_token):
        with allure.step('Создание валюты без поля code'):
            endpoint = '/api/v1/currency/'
            post_url = CommonVariables.base_url + endpoint
            body = {
                "full_title": full_title,
                "short_title": short_title
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def get_currency_by_id(currency_id, access_token):
        with allure.step('Информация о валюте по id'):
            endpoint = f'/api/v1/currency/{currency_id}/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def change_currency(currency_id, code, full_title, short_title, access_token):
        with allure.step('Изменение информации о валюте'):
            endpoint = f'/api/v1/currency/{currency_id}/'
            patch_url = CommonVariables.base_url + endpoint
            body = {
                "code": code,
                "full_title": full_title,
                "short_title": short_title
            }
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_currency_wt_short_title(currency_id, code, full_title, access_token):
        with allure.step('Изменение информации о валюте без short_title'):
            endpoint = f'/api/v1/currency/{currency_id}/'
            patch_url = CommonVariables.base_url + endpoint
            body = {
                "code": code,
                "full_title": full_title,
            }
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_currency_wt_full_title(currency_id, code, short_title, access_token):
        with allure.step('Изменение информации о валюте'):
            endpoint = f'/api/v1/currency/{currency_id}/'
            patch_url = CommonVariables.base_url + endpoint
            body = {
                "code": code,
                "short_title": short_title
            }
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_currency_wt_code(currency_id, full_title, short_title, access_token):
        with allure.step('Изменение информации о валюте без поля код'):
            endpoint = f'/api/v1/currency/{currency_id}/'
            patch_url = CommonVariables.base_url + endpoint
            body = {
                "full_title": full_title,
                "short_title": short_title
            }
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def delete_currency(currency_id, access_token):
        with allure.step('Удаление валюты'):
            endpoint = f'/api/v1/currency/{currency_id}/'
            delete_url = CommonVariables.base_url + endpoint
            result = HttpMethods.delete(delete_url, access_token)
            return result

    @staticmethod
    def delete_currency_wt_currency_id(access_token):
        with allure.step('Удаление валюты без currency_id'):
            endpoint = f'/api/v1/currency/'
            delete_url = CommonVariables.base_url + endpoint
            result = HttpMethods.delete(delete_url, access_token)
            return result

    @staticmethod
    def delete_currency_if_bug(result, access_token):
        result_text = result.text
        data = json.loads(result_text)
        currency_id = data['data']['id']
        print(currency_id)
        result_delete = CurrencyMethods.delete_currency(currency_id, access_token)
        return result_delete


