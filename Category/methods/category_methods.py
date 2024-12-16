import allure
from common_methods.http_methods import HttpMethods
from common_methods.variables import CommonVariables


class CategoryMethods:

    @staticmethod
    def get_category(access_token):
        with allure.step('Получение списка категорий'):
            endpoint = '/api/v1/category/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_category_without_access_token():
        with allure.step('Получение списка категорий'):
            endpoint = '/api/v1/category/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get_without_auth(get_url)
            return result

    @staticmethod
    def get_category_with_excluded(excluded, access_token):
        with allure.step('Получение списка категорий с параметром excluded'):
            endpoint = '/api/v1/category/'
            excluded = f'?excluded={excluded}'
            get_url = CommonVariables.base_url + endpoint + excluded
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_category_with_transaction_type(transaction_type, access_token):
        with allure.step('Получение списка категорий с параметром transaction_type'):
            endpoint = '/api/v1/category/'
            transaction_type = f'?transaction_type={transaction_type}'
            get_url = CommonVariables.base_url + endpoint + transaction_type
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_category_with_all_params(excluded, transaction_type, access_token):
        with allure.step('Получение списка категорий со всеми параметрами'):
            endpoint = '/api/v1/category/'
            excluded = f'?excluded={excluded}'
            transaction_type = f'&transaction_type={transaction_type}'
            get_url = CommonVariables.base_url + endpoint + excluded + transaction_type
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_category_by_id(category_id, access_token):
        with allure.step('Получение списка категорий'):
            endpoint = f'/api/v1/category/{category_id}/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_category_by_id_without_id(access_token):
        with allure.step('Получение списка категорий'):
            endpoint = f'/api/v1/category/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result
