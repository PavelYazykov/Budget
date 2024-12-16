import json

import allure
from common_methods.variables import CommonVariables
from common_methods.http_methods import HttpMethods
from common_methods.auth import Auth
base_url = CommonVariables.base_url


class PersonalTransactionMethods:

    @staticmethod
    def create_personal_transaction(
            amount, description, transaction_type, transaction_date, id_wallet_for_transfer, wallet_id, category_id,
            subcategory_id, access_token
    ):
        with allure.step('Создание персональной транзакции'):
            endpoint = '/api/v1/personal_transaction/'
            post_url = base_url + endpoint
            body = {
                "amount": amount,
                "description": description,
                "transaction_type": transaction_type,
                "transaction_date": transaction_date,
                "id_wallet_for_transfer": id_wallet_for_transfer,
                "wallet_id": wallet_id,
                "category_id": category_id,
                "subcategory_id": subcategory_id
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_transaction_without_amount(
            description, transaction_type, transaction_date, id_wallet_for_transfer, wallet_id, category_id,
            subcategory_id, access_token
    ):
        with allure.step('Создание персональной транзакции без поля amount'):
            endpoint = '/api/v1/personal_transaction/'
            post_url = base_url + endpoint
            body = {
                "description": description,
                "transaction_type": transaction_type,
                "transaction_date": transaction_date,
                "id_wallet_for_transfer": id_wallet_for_transfer,
                "wallet_id": wallet_id,
                "category_id": category_id,
                "subcategory_id": subcategory_id
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_transaction_without_description(
            amount, transaction_type, transaction_date, id_wallet_for_transfer, wallet_id, category_id,
            subcategory_id, access_token
    ):
        with allure.step('Создание персональной транзакции без поля description'):
            endpoint = '/api/v1/personal_transaction/'
            post_url = base_url + endpoint
            body = {
                "amount": amount,
                "transaction_type": transaction_type,
                "transaction_date": transaction_date,
                "id_wallet_for_transfer": id_wallet_for_transfer,
                "wallet_id": wallet_id,
                "category_id": category_id,
                "subcategory_id": subcategory_id
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_transaction_without_transaction_type(
            amount, description, transaction_date, id_wallet_for_transfer, wallet_id, category_id,
            subcategory_id, access_token
    ):
        with allure.step('Создание персональной транзакции без поля transaction type'):
            endpoint = '/api/v1/personal_transaction/'
            post_url = base_url + endpoint
            body = {
                "amount": amount,
                "description": description,
                "transaction_date": transaction_date,
                "id_wallet_for_transfer": id_wallet_for_transfer,
                "wallet_id": wallet_id,
                "category_id": category_id,
                "subcategory_id": subcategory_id
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_transaction_without_transaction_date(
            amount, description, transaction_type, id_wallet_for_transfer, wallet_id, category_id,
            subcategory_id, access_token
    ):
        with allure.step('Создание персональной транзакции без поля transaction date'):
            endpoint = '/api/v1/personal_transaction/'
            post_url = base_url + endpoint
            body = {
                "amount": amount,
                "description": description,
                "transaction_type": transaction_type,
                "id_wallet_for_transfer": id_wallet_for_transfer,
                "wallet_id": wallet_id,
                "category_id": category_id,
                "subcategory_id": subcategory_id
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_transaction_without_id_wallet_for_transfer(
            amount, description, transaction_type, transaction_date, wallet_id, category_id,
            subcategory_id, access_token
    ):
        with allure.step('Создание персональной транзакции без поля d_wallet_for_transfer'):
            endpoint = '/api/v1/personal_transaction/'
            post_url = base_url + endpoint
            body = {
                "amount": amount,
                "description": description,
                "transaction_type": transaction_type,
                "transaction_date": transaction_date,
                "wallet_id": wallet_id,
                "category_id": category_id,
                "subcategory_id": subcategory_id
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_transaction_without_id_wallet_for_transfer_trans_type(
            amount, description, transaction_date, wallet_id, category_id,
            subcategory_id, access_token
    ):
        with allure.step('Создание персональной транзакции без поля id_wallet_for_transfer и transaction_type'):
            endpoint = '/api/v1/personal_transaction/'
            post_url = base_url + endpoint
            body = {
                "amount": amount,
                "description": description,
                "transaction_date": transaction_date,
                "wallet_id": wallet_id,
                "category_id": category_id,
                "subcategory_id": subcategory_id
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_transaction_without_wallet_id(
            amount, description, transaction_type, transaction_date, id_wallet_for_transfer, category_id,
            subcategory_id, access_token
    ):
        with allure.step('Создание персональной транзакции без поля wallet id'):
            endpoint = '/api/v1/personal_transaction/'
            post_url = base_url + endpoint
            body = {
                "amount": amount,
                "description": description,
                "transaction_type": transaction_type,
                "transaction_date": transaction_date,
                "id_wallet_for_transfer": id_wallet_for_transfer,
                "category_id": category_id,
                "subcategory_id": subcategory_id
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_transaction_without_category(
            amount, description, transaction_type, transaction_date, id_wallet_for_transfer, wallet_id,
            subcategory_id, access_token
    ):
        with allure.step('Создание персональной транзакции без поля category'):
            endpoint = '/api/v1/personal_transaction/'
            post_url = base_url + endpoint
            body = {
                "amount": amount,
                "description": description,
                "transaction_type": transaction_type,
                "transaction_date": transaction_date,
                "id_wallet_for_transfer": id_wallet_for_transfer,
                "wallet_id": wallet_id,
                "subcategory_id": subcategory_id
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_transaction_without_subcategory(
            amount, description, transaction_type, transaction_date, id_wallet_for_transfer, wallet_id, category_id,
            access_token
    ):
        with allure.step('Создание персональной транзакции без поля subcategory'):
            endpoint = '/api/v1/personal_transaction/'
            post_url = base_url + endpoint
            body = {
                "amount": amount,
                "description": description,
                "transaction_type": transaction_type,
                "transaction_date": transaction_date,
                "id_wallet_for_transfer": id_wallet_for_transfer,
                "wallet_id": wallet_id,
                "category_id": category_id
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_transaction_without_auth(
            amount, description, transaction_type, transaction_date, id_wallet_for_transfer, wallet_id, category_id,
            subcategory_id
    ):
        with allure.step('Создание персональной транзакции без авторизации'):
            endpoint = '/api/v1/personal_transaction/'
            post_url = base_url + endpoint
            body = {
                "amount": amount,
                "description": description,
                "transaction_type": transaction_type,
                "transaction_date": transaction_date,
                "id_wallet_for_transfer": id_wallet_for_transfer,
                "wallet_id": wallet_id,
                "category_id": category_id,
                "subcategory_id": subcategory_id
            }
            result = HttpMethods.post_without_auth(post_url, body)
            return result

    @staticmethod
    def create_personal_transaction_without_body(access_token):
        with allure.step('Создание персональной транзакции без body'):
            endpoint = '/api/v1/personal_transaction/'
            post_url = base_url + endpoint
            result = HttpMethods.post_without_body(post_url, access_token)
            return result

    @staticmethod
    def get_personal_transaction(transaction_type, access_token):
        with allure.step('Получение списка персональных транзакций'):
            endpoint = '/api/v1/personal_transaction/'
            transaction_type = f'?transaction_type={transaction_type}'
            get_url = base_url + endpoint + transaction_type
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_personal_transaction_without_transaction_type(access_token):
        with allure.step('Получение списка персональных транзакций без поля transaction type'):
            endpoint = '/api/v1/personal_transaction/'
            get_url = base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_personal_transaction_without_auth(transaction_type):
        with allure.step('Получение списка персональных транзакций без авторизации'):
            endpoint = '/api/v1/personal_transaction/'
            transaction_type = f'?transaction_type={transaction_type}'
            get_url = base_url + endpoint + transaction_type
            result = HttpMethods.get_without_auth(get_url)
            return result

    @staticmethod
    def get_personal_transaction_with_params(transaction_type, day, month, year, access_token):
        with allure.step('Получение списка персональных транзакций'):
            endpoint = '/api/v1/personal_transaction/'
            transaction_type = f'?transaction_type={transaction_type}'
            day = f'&day={day}'
            month = f'&month={month}'
            year = f'&year={year}'
            get_url = base_url + endpoint + transaction_type + day + month + year
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_personal_transaction_with_params_wd(transaction_type, month, year, access_token):
        with allure.step('Получение списка персональных транзакций без поля day'):
            endpoint = '/api/v1/personal_transaction/'
            transaction_type = f'?transaction_type={transaction_type}'
            month = f'&month={month}'
            year = f'&year={year}'
            get_url = base_url + endpoint + transaction_type + month + year
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_personal_transaction_with_params_wm(transaction_type, day, year, access_token):
        with allure.step('Получение списка персональных транзакций без поля month'):
            endpoint = '/api/v1/personal_transaction/'
            transaction_type = f'?transaction_type={transaction_type}'
            day = f'&day={day}'
            year = f'&year={year}'
            get_url = base_url + endpoint + transaction_type + day + year
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_personal_transaction_with_params_wy(transaction_type, day, month, access_token):
        with allure.step('Получение списка персональных транзакций без поля year'):
            endpoint = '/api/v1/personal_transaction/'
            transaction_type = f'?transaction_type={transaction_type}'
            day = f'&day={day}'
            month = f'&month={month}'
            get_url = base_url + endpoint + transaction_type + day + month
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_personal_transaction_by_id(personal_transaction_id, access_token):
        with allure.step('Получение списка персональных транзакций по id'):
            endpoint = f'/api/v1/personal_transaction/{personal_transaction_id}/'
            get_url = base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_personal_transaction_by_id_without_pt_id(access_token):
        with allure.step('Получение списка персональных транзакций по id'):
            endpoint = '/api/v1/personal_transaction/'
            get_url = base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_personal_transaction_without_id_field(access_token):
        with allure.step('Получение списка персональных транзакций по id'):
            endpoint = '/api/v1/personal_transaction/'
            get_url = base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def change_personal_transaction(personal_transaction_id, description, access_token):
        with allure.step('Изменение персональной транзакции'):
            endpoint = f'/api/v1/personal_transaction/{personal_transaction_id}/'
            patch_url = base_url + endpoint
            body = {
                "description": description
            }
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_personal_transaction_without_id(description, access_token):
        with allure.step('Изменение персональной транзакции без поля id'):
            endpoint = '/api/v1/personal_transaction/'
            patch_url = base_url + endpoint
            body = {
                "description": description
            }
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_personal_transaction_without_auth(personal_transaction_id, description):
        with allure.step('Изменение персональной транзакции без авторизации'):
            endpoint = '/api/v1/personal_transaction/'
            personal_transaction_id = str(personal_transaction_id) + '/'
            patch_url = base_url + endpoint + personal_transaction_id
            body = {
                "description": description
            }
            result = HttpMethods.patch_without_auth(patch_url, body)
            return result

    @staticmethod
    def change_personal_transaction_without_body(personal_transaction_id, access_token):
        with allure.step('Изменение персональной транзакции без body'):
            endpoint = '/api/v1/personal_transaction/'
            personal_transaction_id = str(personal_transaction_id) + '/'
            patch_url = base_url + endpoint + personal_transaction_id
            result = HttpMethods.patch_without_body(patch_url, access_token)
            return result

    @staticmethod
    def delete_personal_transaction(personal_transaction_id, access_token):
        with allure.step('Удаление персональной транзакции'):
            endpoint = f'/api/v1/personal_transaction/{personal_transaction_id}/'
            delete_url = base_url + endpoint
            result = HttpMethods.delete(delete_url, access_token)
            return result

    @staticmethod
    def delete_personal_transaction_without_id(access_token):
        with allure.step('Удаление персональной транзакции'):
            endpoint = '/api/v1/personal_transaction/'
            delete_url = base_url + endpoint
            print(delete_url)
            result = HttpMethods.delete(delete_url, access_token)
            return result

    @staticmethod
    def delete_personal_transaction_without_auth(personal_transaction_id):
        with allure.step('Удаление персональной транзакции'):
            endpoint = '/api/v1/personal_transaction/'
            personal_transaction_id = str(personal_transaction_id) + '/'
            delete_url = base_url + endpoint + personal_transaction_id
            result = HttpMethods.delete_without_auth(delete_url)
            return result

    @staticmethod
    def writing_off_money(
            result, description, transaction_type_consume, transaction_date, wallet_id_1, wallet_id_2,
            category_id_consume, amount, access_token
    ):
        with allure.step('Списание средств с копилки'):
            if result.status_code == 422:
                PersonalTransactionMethods.create_personal_transaction(
                    amount, description, transaction_type_consume, transaction_date, None,
                    wallet_id_1, category_id_consume, None, access_token
                )
            elif result.status_code == 404:
                PersonalTransactionMethods.create_personal_transaction(
                    amount, description, transaction_type_consume, transaction_date, None,
                    wallet_id_1, category_id_consume, None, access_token
                )
            elif result.status_code == 400:
                PersonalTransactionMethods.create_personal_transaction(
                    amount, description, transaction_type_consume, transaction_date, None,
                    wallet_id_1, category_id_consume, None, access_token
                )
            elif result.status_code == 201:
                PersonalTransactionMethods.create_personal_transaction(
                    amount, description, transaction_type_consume, transaction_date, None,
                    wallet_id_2, category_id_consume, None, access_token
                )

    @staticmethod
    def check_required_fields_get(data):
        required_fields = {
            "amount": 100.55,
            "description": "Title or description",
            "transaction_type": "Income",
            "transaction_date": "2024-10-23",
            "id_wallet_for_transfer": 1,
            "wallet_id": 1,
            "category_id": 1,
            "subcategory_id": 1,
            "id": 1
        }

        for field in required_fields:
            assert field in data['data'], f'Поле {field} отсутствует'

    @staticmethod
    def get_personal_transaction_id(result):
        with allure.step('Получение id персональной транзакции'):
            result_text = result.text
            data = json.loads(result_text)
            personal_transaction_id = data['data']['id']
            print(personal_transaction_id)
            return personal_transaction_id



