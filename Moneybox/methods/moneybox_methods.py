import json
import allure
from common_methods.http_methods import HttpMethods
import psycopg2
from common_methods.variables import CommonVariables
from common_methods.variables import DataBase
base_url = CommonVariables.base_url


class MoneyboxMethods:
    """Методы для тестрования Копилок"""

    @staticmethod
    def create_moneybox(to_date, goal, name, currency_id, amount, access_token):
        with allure.step('Создание копилки'):
            post_endpoint = '/api/v1/moneybox/'
            post_url = base_url + post_endpoint
            print(post_url)
            body = {
                "to_date": to_date,
                "goal": goal,
                "wallet": {
                    "name": name,
                    "currency_id": currency_id,
                    "amount": amount
                }
            }
            post_response = HttpMethods.post(post_url, body, access_token)
            return post_response

    @staticmethod
    def create_moneybox_without_amount(to_date, goal, name, currency_id, access_token):
        with allure.step('Создание копилки без поля amount'):
            post_endpoint = '/api/v1/moneybox/'
            post_url = base_url + post_endpoint
            print(post_url)
            body = {
                "to_date": to_date,
                "goal": goal,
                "wallet": {
                    "name": name,
                    "currency_id": currency_id
                }
            }
            post_response = HttpMethods.post(post_url, body, access_token)
            return post_response

    @staticmethod
    def create_moneybox_without_currency(to_date, goal, name, amount, access_token):
        with allure.step('Создание копилки без поля currency'):
            post_endpoint = '/api/v1/moneybox/'
            post_url = base_url + post_endpoint
            print(post_url)
            body = {
                "to_date": to_date,
                "goal": goal,
                "wallet": {
                    "name": name,
                    "amount": amount
                }
            }
            post_response = HttpMethods.post(post_url, body, access_token)
            return post_response

    @staticmethod
    def create_moneybox_without_name(to_date, goal, currency_id, amount, access_token):
        with allure.step('Создание копилки без поля name'):
            post_endpoint = '/api/v1/moneybox/'
            post_url = base_url + post_endpoint
            print(post_url)
            body = {
                "to_date": to_date,
                "goal": goal,
                "wallet": {
                    "currency_id": currency_id,
                    "amount": amount
                }
            }
            post_response = HttpMethods.post(post_url, body, access_token)
            return post_response

    @staticmethod
    def create_moneybox_without_to_date(goal, name, currency_id, amount, access_token):
        with allure.step('Создание копилки без поля date'):
            post_endpoint = '/api/v1/moneybox/'
            post_url = base_url + post_endpoint
            print(post_url)
            body = {
                "goal": goal,
                "wallet": {
                    "name": name,
                    "currency_id": currency_id,
                    "amount": amount
                }
            }
            post_response = HttpMethods.post(post_url, body, access_token)
            return post_response

    @staticmethod
    def create_moneybox_without_goal(to_date, name, currency_id, amount, access_token):
        with allure.step('Создание копилки без поля goal'):
            post_endpoint = '/api/v1/moneybox/'
            post_url = base_url + post_endpoint
            print(post_url)
            body = {
                "to_date": to_date,
                "wallet": {
                    "name": name,
                    "currency_id": currency_id,
                    "amount": amount
                }
            }
            post_response = HttpMethods.post(post_url, body, access_token)
            return post_response

    @staticmethod
    def create_moneybox_without_body(access_token):
        with allure.step('Создание копилки без body'):
            post_endpoint = '/api/v1/moneybox/'
            post_url = base_url + post_endpoint
            print(post_url)
            post_response = HttpMethods.post_without_body(post_url, access_token)
            return post_response

    @staticmethod
    def create_moneybox_without_auth(to_date, goal, name, currency_id, amount):
        with allure.step('Создание копилки без авторизации'):
            post_endpoint = '/api/v1/moneybox/'
            post_url = base_url + post_endpoint
            print(post_url)
            body = {
                "to_date": to_date,
                "goal": goal,
                "wallet": {
                    "name": name,
                    "currency_id": currency_id,
                    "amount": amount
                }
            }
            post_response = HttpMethods.post_without_auth(post_url, body)
            return post_response

    @staticmethod
    def get_all_moneybox(access_token):
        with allure.step('Получение списка всех копилок'):
            get_endpoint = '/api/v1/moneybox/'
            get_url = base_url + get_endpoint
            print(get_url)
            get_response = HttpMethods.get(get_url, access_token)
            return get_response

    @staticmethod
    def get_all_moneybox_without_auth():
        with allure.step('Получение списка всех копилок без авторизации'):
            get_endpoint = '/api/v1/moneybox/'
            get_url = base_url + get_endpoint
            print(get_url)
            get_response = HttpMethods.get_without_auth(get_url)
            return get_response

    @staticmethod
    def get_all_moneybox_with_params(access_token, check):
        with allure.step('Получение списка всех копилок c выбором активные/архивные'):
            get_endpoint = '/api/v1/moneybox/?'
            is_archived = f'is_archived={check}'
            get_url = base_url + get_endpoint + is_archived
            print(get_url)
            get_response = HttpMethods.get(get_url, access_token)
            return get_response

    @staticmethod
    def get_one_moneybox(moneybox_id, access_token):
        with allure.step('Получение копилки по id'):
            get_endpoint = f'/api/v1/moneybox/{moneybox_id}/'
            get_url = base_url + get_endpoint
            print(get_url)
            get_response = HttpMethods.get(get_url, access_token)
            return get_response

    @staticmethod
    def get_one_moneybox_without_auth(moneybox_id):
        with allure.step('Получение копилки по id'):
            get_endpoint = '/api/v1/moneybox/'
            id_moneybox = str(moneybox_id) + "/"
            get_url = base_url + get_endpoint + id_moneybox
            get_response = HttpMethods.get_without_auth(get_url)
            return get_response

    @staticmethod
    def change_moneybox(moneybox_id, to_date, goal,  name, currency_id, is_archived, access_token):
        with allure.step('Внесение изменений в копилку'):
            patch_endpoint = f'/api/v1/moneybox/{moneybox_id}/'
            body = {
                "to_date": to_date,
                "goal": goal,
                "wallet": {
                    "name": name,
                    "currency_id": currency_id,
                    "is_archived": is_archived
                }
            }
            patch_url = base_url + patch_endpoint
            print(patch_url)
            patch_response = HttpMethods.patch(patch_url, body, access_token)
            return patch_response

    @staticmethod
    def change_moneybox_only_goal(moneybox_id, goal, access_token):
        with allure.step('Внесение изменений в копилку'):
            patch_endpoint = f'/api/v1/moneybox/{moneybox_id}/'
            body = {
                "goal": goal
            }
            patch_url = base_url + patch_endpoint
            print(patch_url)
            patch_response = HttpMethods.patch(patch_url, body, access_token)
            return patch_response

    @staticmethod
    def change_moneybox_without_name(moneybox_id, to_date, goal, currency_id, is_archived, access_token):
        with allure.step('Внесение изменений в копилку поле  name отсутствует'):
            patch_endpoint = '/api/v1/moneybox/'
            id_moneybox = str(moneybox_id) + "/"
            body = {
                "to_date": to_date,
                "goal": goal,
                "wallet": {
                    "currency_id": currency_id,
                    "is_archived": is_archived}
            }
            patch_url = base_url + patch_endpoint + id_moneybox
            print(patch_url)
            patch_response = HttpMethods.patch(patch_url, body, access_token)
            return patch_response

    @staticmethod
    def change_moneybox_without_is_archhived(moneybox_id, to_date, goal, name, currency_id, access_token):
        with allure.step('Внесение изменений в копилку без поля is_archived'):
            patch_endpoint = '/api/v1/moneybox/'
            id_moneybox = str(moneybox_id) + "/"
            body = {
                "to_date": to_date,
                "goal": goal,
                "wallet": {
                    "name": name,
                    "currency_id": currency_id}
            }
            patch_url = base_url + patch_endpoint + id_moneybox
            print(patch_url)
            patch_response = HttpMethods.patch(patch_url, body, access_token)
            return patch_response

    @staticmethod
    def change_moneybox_without_currency_id(moneybox_id, to_date, goal, name, is_archived, access_token):
        with allure.step('Внесение изменений в копилку без поля currency_id'):
            patch_endpoint = '/api/v1/moneybox/'
            id_moneybox = str(moneybox_id) + "/"
            body = {
                "to_date": to_date,
                "goal": goal,
                "wallet": {
                    "name": name,
                    "is_archived": is_archived}
            }
            patch_url = base_url + patch_endpoint + id_moneybox
            print(patch_url)
            patch_response = HttpMethods.patch(patch_url, body, access_token)
            return patch_response

    @staticmethod
    def change_moneybox_without_goal(moneybox_id, to_date, name, currency_id, is_archived, access_token):
        with allure.step('Внесение изменений в копилку без поля goal'):
            patch_endpoint = '/api/v1/moneybox/'
            id_moneybox = str(moneybox_id) + "/"
            body = {
                "to_date": to_date,
                "wallet": {
                    "name": name,
                    "currency_id": currency_id,
                    "is_archived": is_archived}
            }
            patch_url = base_url + patch_endpoint + id_moneybox
            print(patch_url)
            patch_response = HttpMethods.patch(patch_url, body, access_token)
            return patch_response

    @staticmethod
    def change_moneybox_without_to_date(moneybox_id, goal, name, currency_id, is_archived, access_token):
        with allure.step('Внесение изменений в копилку без поля to_date'):
            patch_endpoint = '/api/v1/moneybox/'
            id_moneybox = str(moneybox_id) + "/"
            body = {
                "goal": goal,
                "wallet": {
                    "name": name,
                    "currency_id": currency_id,
                    "is_archived": is_archived}
            }
            patch_url = base_url + patch_endpoint + id_moneybox
            print(patch_url)
            patch_response = HttpMethods.patch(patch_url, body, access_token)
            return patch_response

    @staticmethod
    def change_moneybox_without_moneybox_id(to_date, goal, name, currency_id, is_archived, access_token):
        with allure.step('Внесение изменений в копилку без поля moneybox_id'):
            patch_endpoint = '/api/v1/moneybox/'
            body = {
                "to_date": to_date,
                "goal": goal,
                "wallet": {
                    "name": name,
                    "currency_id": currency_id,
                    "is_archived": is_archived}
            }
            patch_url = base_url + patch_endpoint
            print(patch_url)
            patch_response = HttpMethods.patch(patch_url, body, access_token)
            return patch_response

    @staticmethod
    def change_moneybox_without_body(moneybox_id, access_token):
        with allure.step('Внесение изменений в копилку без body'):
            patch_endpoint = '/api/v1/moneybox/'
            id_moneybox = str(moneybox_id) + "/"
            patch_url = base_url + patch_endpoint + id_moneybox
            print(patch_url)
            patch_response = HttpMethods.patch_without_body(patch_url, access_token)
            return patch_response

    @staticmethod
    def change_moneybox_without_auth(moneybox_id, to_date, goal, name, currency_id, is_archived):
        with allure.step('Внесение изменений в копилку без авторизации'):
            patch_endpoint = '/api/v1/moneybox/'
            id_moneybox = str(moneybox_id) + "/"
            body = {
                "to_date": to_date,
                "goal": goal,
                "wallet": {
                    "name": name,
                    "currency_id": currency_id,
                    "is_archived": is_archived}
            }
            patch_url = base_url + patch_endpoint + id_moneybox
            print(patch_url)
            patch_response = HttpMethods.patch_without_auth(patch_url, body)
            return patch_response

    @staticmethod
    def delete_moneybox(moneybox_id, access_token):
        with allure.step('Удаление копилки'):
            endpoint = f'/api/v1/moneybox/{moneybox_id}/'
            delete_url = base_url + endpoint
            delete_result = HttpMethods.delete(delete_url, access_token)
            print(f'delete_result: {delete_result.text}')
            return delete_result

    @staticmethod
    def delete_moneybox_wo_access_token(moneybox_id):
        with allure.step('Удаление копилки без access_token'):
            endpoint = f'/api/v1/moneybox/{moneybox_id}/'
            delete_url = base_url + endpoint
            delete_result = HttpMethods.delete_without_auth(delete_url)
            print(f'delete_result: {delete_result.text}')
            return delete_result

    @staticmethod
    def consumption(amount, wallet_id, access_token):
        with allure.step("Транзакция по списанию средств с копилки"):
            post_resource = '/api/v1/personal_transaction/'
            post_url = base_url + post_resource
            body = {
                "amount": amount,
                "description": "consumption",
                "transaction_type": "Consumption",
                "wallet_id": wallet_id,
                "category_id": 20
            }
            result = HttpMethods.post(post_url, body, access_token)
            print(result.text)
            return result

    @staticmethod
    def income(amount, wallet_id, access_token):
        with allure.step("Транзакция по пополнению средств в копилку"):
            post_resource = '/api/v1/personal_transaction/'
            post_url = base_url + post_resource
            body = {
                "amount": amount,
                "description": "Income",
                "transaction_type": "Income",
                "wallet_id": wallet_id,
                "category_id": 30
            }
            result = HttpMethods.post(post_url, body, access_token)
            print(result.text)
            return result

    @staticmethod
    def get_wallet_id(result):
        with allure.step("Получение wallet_id"):
            result_text = result.text
            data = json.loads(result_text)
            wallet_id = data['data']['wallet']['id']
            print(f'Wallet_id: {wallet_id}')
            return wallet_id

    @staticmethod
    def get_moneybox_id(result):
        with allure.step("Получение moneybox_id"):
            result_text = result.text
            data = json.loads(result_text)
            moneybox_id = data['data']['id']
            print(f'Moneybox_id: {moneybox_id}')
            return moneybox_id

    @staticmethod
    def get_data(result):
        result_text = result.text
        data = json.loads(result_text)
        return data

    @staticmethod
    def post_check_exist_req_fields(result, required_fields):
        with allure.step('Проверка наличия обязательных полей'):
            result_text = result.text
            data = json.loads(result_text)

            for field in required_fields:
                assert field in data, f"Отсутствует обязательное поле: {field}"
                print(f'Обязательное поле {field} присутствует')

            for field in required_fields['data']:
                assert field in data['data'], f"Отсутствует обязательное поле: {field}"
                print(f'Обязательное поле {field} присутствует')

            for field in required_fields['data']['wallet']:
                assert field in data['data']['wallet'], f"Отсутствует обязательное поле: {field}"
                print(f'Обязательное поле {field} присутствует')

    @staticmethod
    def delete_moneybox_from_bd(moneybox_id):
        with allure.step('Удаление копилки из базы данных'):
            with psycopg2.connect(
                    host=DataBase.host,
                    user=DataBase.user,
                    password=DataBase.password,
                    dbname=DataBase.dbname,
                    port=DataBase.port
            ) as connection:
                cursor = connection.cursor()
                cursor.execute(f"""DELETE FROM moneyboxies WHERE id={moneybox_id}""")
                connection.commit()
                print(f'Копилка с id: {moneybox_id} удалена')

