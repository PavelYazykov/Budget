import allure
import psycopg2

from common_methods.checking import Checking
from common_methods.http_methods import HttpMethods
from common_methods.variables import CommonVariables, DataBase


class WalletMethods:

    @staticmethod
    def get_all_wallet(access_token):
        with allure.step('Получение списка всех счетов'):
            endpoint = '/api/v1/wallet/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_all_wallet_without_auth():
        with allure.step('Получение списка всех счетов без авторизации'):
            endpoint = '/api/v1/wallet/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get_without_auth(get_url)
            return result

    @staticmethod
    def create_wallet(name, currency_id, amount, access_token):
        with allure.step('Создание счета'):
            endpoint = '/api/v1/wallet/'
            body = {
                "name": name,
                "currency_id": currency_id,
                "amount": amount
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_wallet_without_amount(name, currency_id, access_token):
        with allure.step('Создание счета'):
            endpoint = '/api/v1/wallet/'
            body = {
                "name": name,
                "currency_id": currency_id
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_wallet_without_currency(name, amount, access_token):
        with allure.step('Создание счета без поля currency id'):
            endpoint = '/api/v1/wallet/'
            body = {
                "name": name,
                "amount": amount
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_wallet_without_name(currency_id, amount, access_token):
        with allure.step('Создание счета без поля name'):
            endpoint = '/api/v1/wallet/'
            body = {
                "currency_id": currency_id,
                "amount": amount
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_wallet_without_body(access_token):
        with allure.step('Создание счета'):
            endpoint = '/api/v1/wallet/'
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post_without_body(post_url, access_token)
            return result

    @staticmethod
    def get_wallet_by_id(wallet_id, access_token):
        with allure.step('Получение счета по id'):
            endpoint = f'/api/v1/wallet/{wallet_id}/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_wallet_by_id_without_auth(wallet_id):
        with allure.step('Получение счета по id'):
            endpoint = f'/api/v1/wallet/{wallet_id}/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get_without_auth(get_url)
            return result

    @staticmethod
    def change_wallet_by_id(wallet_id, name, currency_id, is_archived, access_token):
        with allure.step('Изменение информации по выбранному счету'):
            endpoint = f'/api/v1/wallet/{wallet_id}/'
            body = {
                "name": name,
                "currency_id": currency_id,
                "is_archived": is_archived
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_wallet_by_id_only_is_archived(wallet_id, is_archived, access_token):
        with allure.step('Изменение информации по выбранному счету только поле is_archived'):
            endpoint = f'/api/v1/wallet/{wallet_id}/'
            body = {
                "is_archived": is_archived
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_wallet_by_id_only_name_field(wallet_id, name, access_token):
        with allure.step('Изменение информации по выбранному счету только поле name'):
            endpoint = f'/api/v1/wallet/{wallet_id}/'
            body = {
                "name": name
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_wallet_by_id_without_id(name, currency_id, is_archived, access_token):
        with allure.step('Изменение информации по выбранному счету без поля id'):
            endpoint = f'/api/v1/wallet/'
            body = {
                "name": name,
                "currency_id": currency_id,
                "is_archived": is_archived
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_wallet_by_id_only_currency_field(wallet_id, currency_id, access_token):
        with allure.step('Изменение информации по выбранному счету'):
            endpoint = f'/api/v1/wallet/{wallet_id}/'
            body = {
                "currency_id": currency_id
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_wallet_by_id_without_body(wallet_id, access_token):
        with allure.step('Изменение информации по выбранному счету'):
            endpoint = f'/api/v1/wallet/{wallet_id}/'
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch_without_body(patch_url, access_token)
            return result

    @staticmethod
    def delete_wallet_by_id(wallet_id, access_token):
        with allure.step('Удаление выбранного wallet'):
            endpoint = f'/api/v1/wallet/{wallet_id}/'
            delete_url = CommonVariables.base_url + endpoint
            result = HttpMethods.delete(delete_url, access_token)
            print(f'Wallet c id {wallet_id} удален')
            return result

    @staticmethod
    def delete_wallet_by_id_without_wallet_id(access_token):
        with allure.step('Удаление выбранного wallet'):
            endpoint = f'/api/v1/wallet/'
            delete_url = CommonVariables.base_url + endpoint
            result = HttpMethods.delete(delete_url, access_token)
            return result

    @staticmethod
    def delete_wallet_sql(wallet_id):
        with allure.step('Удаление wallet'):
            with psycopg2.connect(
                    host=DataBase.host,
                    user=DataBase.user,
                    password=DataBase.password,
                    dbname=DataBase.dbname,
                    port=DataBase.port
            ) as connection:
                cursor = connection.cursor()
                cursor.execute(f"""DELETE FROM wallets WHERE id='{wallet_id}'""")
                connection.commit()

    @staticmethod
    def delete_wallet_if_bug(result):
        if result.status_code == 201:
            data = Checking.get_data(result)
            wallet_id = data['data']['id']
            WalletMethods.delete_wallet_sql(wallet_id)
            raise AssertionError
