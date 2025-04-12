import allure

from common_methods.http_methods import HttpMethods
from common_methods.checking import Checking
from common_methods.variables import CommonVariables


class PersonalBudgetAutoUseMethods:

    @staticmethod
    def get_personal_budget_auto_use(access_token):
        with allure.step('Запрос информации об объектах регулярного бюджета'):
            endpoint = '/api/v1/personal_budget_auto_use/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_personal_budget_auto_use_without_auth():
        with allure.step('Запрос информации об объектах регулярного бюджета без авторизации'):
            endpoint = '/api/v1/personal_budget_auto_use/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get_without_auth(get_url)
            return result

    @staticmethod
    def create_personal_budget_auto_use(transaction_type, category_id, subcategory_id, amount, date_reminder, access_token):
        with allure.step('Создание объекта регулярного бюджета'):
            endpoint = '/api/v1/personal_budget_auto_use/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "date_reminder": date_reminder
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_auto_use_without_date_reminder(transaction_type, category_id, subcategory_id, amount,
                                                              access_token):
        with allure.step('Создание объекта регулярного бюджета без поля date_reminder'):
            endpoint = '/api/v1/personal_budget_auto_use/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_auto_use_without_amount(transaction_type, category_id, subcategory_id, date_reminder,
                                                       access_token):
        with allure.step('Создание объекта регулярного бюджета без поля amount'):
            endpoint = '/api/v1/personal_budget_auto_use/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "date_reminder": date_reminder
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_auto_use_without_subcategory_id(transaction_type, category_id, amount, date_reminder,
                                                               access_token):
        with allure.step('Создание объекта регулярного бюджета без поля subcategory_id'):
            endpoint = '/api/v1/personal_budget_auto_use/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "amount": amount,
                "date_reminder": date_reminder
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_auto_use_without_category_id(transaction_type, subcategory_id, amount, date_reminder,
                                                            access_token):
        with allure.step('Создание объекта регулярного бюджета без поля category_id'):
            endpoint = '/api/v1/personal_budget_auto_use/'
            body = {
                "transaction_type": transaction_type,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "date_reminder": date_reminder
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_auto_use_without_transaction_type(
            category_id, subcategory_id, amount, date_reminder, access_token):
        with allure.step('Создание объекта регулярного бюджета без поля transaction_type'):
            endpoint = '/api/v1/personal_budget_auto_use/'
            body = {
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "date_reminder": date_reminder
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_auto_use_without_body(access_token):
        with allure.step('Создание объекта регулярного бюджета без body'):
            endpoint = '/api/v1/personal_budget_auto_use/'
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post_without_body(post_url, access_token)
            return result

    @staticmethod
    def get_personal_budget_auto_use_by_id(personal_budget_auto_use_id,  access_token):
        with allure.step('Запрос информации об объектах регулярного бюджета по id'):
            endpoint = f'/api/v1/personal_budget_auto_use/{personal_budget_auto_use_id}/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def delete_personal_budget_auto_use(personal_budget_auto_use_id, access_token):
        with allure.step('Удаление объекта регулярного бюджета'):
            endpoint = f'/api/v1/personal_budget_auto_use/{personal_budget_auto_use_id}/'
            delete_url = CommonVariables.base_url + endpoint
            result = HttpMethods.delete(delete_url, access_token)
            return result

    @staticmethod
    def delete_personal_budget_auto_use_without_id(access_token):
        with allure.step('Удаление объекта регулярного бюджета без поля personal_budget_auto_use_id'):
            endpoint = f'/api/v1/personal_budget_auto_use/'
            delete_url = CommonVariables.base_url + endpoint
            result = HttpMethods.delete(delete_url, access_token)
            return result

    @staticmethod
    def change_personal_budget_auto_use(
            personal_budget_id, transaction_type, category_id, subcategory_id, amount, access_token
    ):
        with allure.step('Изменение регулярного персонального бюджета'):
            endpoint = f'/api/v1/personal_budget/auto_use/{personal_budget_id}/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def delete_auto_use_if_bug(result, access_token):
        if result.status_code == 201:
            data = Checking.get_data(result)
            auto_use_id = data['data']['id']
            delete_result = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(auto_use_id, access_token)
            Checking.check_statuscode(delete_result, 204)

