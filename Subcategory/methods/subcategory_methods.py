import json
import allure
from common_methods.http_methods import HttpMethods
from common_methods.variables import CommonVariables
base_url = CommonVariables.base_url


class SubcategoryMethods:

    @staticmethod
    def get_subcategory(access_token):
        with allure.step('Получение списка подкатегорий доходов и расходов'):
            endpoint = '/api/v1/subcategory/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_subcategory_with_category_id(category, access_token):
        with allure.step('Получение списка подкатегорий доходов и расходов по id категории'):
            endpoint = '/api/v1/subcategory/'
            category = f'?category={category}'
            get_url = CommonVariables.base_url + endpoint + category
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def create_subcategory(category_id, title, access_token):
        with allure.step('Создание подкатегории'):
            endpoint = '/api/v1/subcategory/'
            post_url = base_url + endpoint
            body = {
                "category_id": category_id,
                "title": title
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def get_subcategory_by_id(subcategory_id, access_token):
        with allure.step('Получение подкатегории по id'):
            endpoint = f'/api/v1/subcategory/{subcategory_id}/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url,  access_token)
            return result

    @staticmethod
    def change_subcategory(subcategory_id, title, is_archived, access_token):
        with allure.step('Изменение информации подкатегории'):
            endpoint = f'/api/v1/subcategory/{subcategory_id}/'
            body = {
                "title": title,
                "is_archived": is_archived
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def delete_subcategory(subcategory_id, access_token):
        endpoint = f'/api/v1/subcategory/{subcategory_id}/'
        delete_url = base_url + endpoint
        result = HttpMethods.delete(delete_url, access_token)
        return result

    @staticmethod
    def get_subcategory_id(result):
        with allure.step('Получение id подкатегории'):
            result_text = result.text
            data = json.loads(result_text)
            subcategory_id = data['data']['id']
            return subcategory_id


