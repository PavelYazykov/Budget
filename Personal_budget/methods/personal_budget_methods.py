import allure

from common_methods.http_methods import HttpMethods
from common_methods.variables import CommonVariables


class PersonalBudgetMethods:

    @staticmethod
    def create_personal_budget(
            transaction_type, category_id, subcategory_id, amount, month, year, date_reminder, title, have_to_remind,
            remind_in_days, access_token
    ):
        with allure.step('Создание единоразового объекта персонального бюджета'):
            endpoint = '/api/v1/personal_budget/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "year": year,
                "regular_outcome": {
                    "date_reminder": date_reminder,
                    "title": title,
                    "have_to_remind": have_to_remind,
                    "remind_in_days": remind_in_days
                }
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def get_personal_budget(access_token):
        with allure.step('Получение всех единоразовых объектов объектов бюджета'):
            endpoint = '/api/v1/personal_budget/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_personal_budget_by_id(personal_budget_id, access_token):
        with allure.step('Получение единоразового объекта бюджета по id'):
            endpoint = f'/api/v1/personal_budget/{personal_budget_id}/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def change_personal_budget(
            personal_budget_id, transaction_type, category_id, subcategory_id, amount, month, year, access_token
    ):
        with allure.step('Редактирование данных единоразового объекта персонального бюджета'):
            endpoint = f'/api/v1/personal_budget/{personal_budget_id}/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "year": year
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def delete_personal_budget(personal_budget_id, access_token):
        with allure.step('Удаление единоразового объекта персонального бюджета'):
            endpoint = f'/api/v1/personal_budget/{personal_budget_id}/'
            delete_url = CommonVariables.base_url + endpoint
            result = HttpMethods.delete(delete_url, access_token)
            return result

    @staticmethod
    def patch_personal_budget_auto_use(
            personal_budget_id, transaction_type, category_id, subcategory_id, amount, month, year, access_token
    ):
        with allure.step('Редактирование данных единоразового и регулярного объекта персонального бюджета'):
            endpoint = f'/api/v1/personal_budget/auto_use/{personal_budget_id}/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "year": year
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

