import time

import allure
import pytest

from common_methods.auth import Auth
from common_methods.checking import Checking
from Wallet.methods.wallet_methods import WalletMethods
from Auth.methods.auth_methods import AuthMethods
from common_methods.variables import AuthVariables


@pytest.mark.Wallet
@allure.epic('Delete/api/v1/wallet/{wallet_id}/ Удаление wallet')
class TestDeleteWallet:

    @allure.description('Удаление wallet - Удаление существующего счета')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание wallet"""
        result_create = WalletMethods.create_wallet(
            'w_2', 2, 0, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        wallet_id = data['data']['id']

        """Удаление wallet"""
        result_delete = WalletMethods.delete_wallet_by_id(wallet_id, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 204)

        """Повторное удаление wallet"""
        result_delete = WalletMethods.delete_wallet_by_id(wallet_id, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 404)

        """Получение информации о wallet"""
        result_get = WalletMethods.get_wallet_by_id(
            wallet_id, access_token
        )
        Checking.check_statuscode(result_get, 403)

    @allure.description('Удаление архивного счета')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание wallet"""
        result_create = WalletMethods.create_wallet(
            'w_2', 2, 0, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        wallet_id = data['data']['id']

        """Перенос wallet в архив"""
        result_archived = WalletMethods.change_wallet_by_id_only_is_archived(wallet_id, True, access_token)
        Checking.check_statuscode(result_archived, 200)
        print(result_archived.json())
        print(data['data']['is_archived'])

        """Проверка статус wallet """
        data = Checking.get_data(result_archived)
        assert data['data']['is_archived'] is True

        """Удаление wallet"""
        result_delete = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
        Checking.check_statuscode(result_delete, 204)

        """Получение информации о wallet"""
        result_get = WalletMethods.get_wallet_by_id(
            wallet_id, access_token
        )
        Checking.check_statuscode(result_get, 403)

    @allure.description('Удаление архивного счета')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание wallet"""
        result_create = WalletMethods.create_wallet(
            'w_2', 2, 100, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        wallet_id = data['data']['id']

        """Проверка баланса wallet """
        data = Checking.get_data(result_create)
        assert data['data']['amount'] == '100.00'

        """Удаление wallet"""
        result_delete = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
        Checking.check_statuscode(result_delete, 204)

        """Получение информации о wallet"""
        result_get = WalletMethods.get_wallet_by_id(
            wallet_id, access_token
        )
        Checking.check_statuscode(result_get, 403)

    @allure.description('Удаление несуществующего счета')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление wallet"""
        result_delete = WalletMethods.delete_wallet_by_id(101010, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 404)

    @allure.description('Удаление wallet - Значение wallet_id = 0')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление wallet"""
        result_delete = WalletMethods.delete_wallet_by_id(0, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление wallet - Отрицательное значение wallet_id')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление wallet"""
        result_delete = WalletMethods.delete_wallet_by_id(-11, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление wallet - Пуcтое поле')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление wallet"""
        result_delete = WalletMethods.delete_wallet_by_id('', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 405)

    @allure.description('Удаление wallet - поле wallet_id отсутствует')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление wallet"""
        result_delete = WalletMethods.delete_wallet_by_id_without_wallet_id(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 405)

    @allure.description('Удаление wallet - поле wallet_id null')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление wallet"""
        result_delete = WalletMethods.delete_wallet_by_id(None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление wallet - Неверный тип данных')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление wallet"""
        result_delete = WalletMethods.delete_wallet_by_id('string', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление wallet другого пользователя')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание wallet"""
        result_create = WalletMethods.create_wallet(
            'w_2', 2, 100, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        wallet_id = data['data']['id']

        """Создание второго пользователя"""
        result_create_second_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_second_user, 201)
        data, user_id = AuthMethods.get_id(result_create_second_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Авторизация второго пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token_2 = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Удаление wallet другого пользователя"""
            result_delete = WalletMethods.delete_wallet_by_id(wallet_id, access_token_2)
            Checking.check_statuscode(result_delete, 403)
        finally:

            """Удаление wallet"""
            result_delete_2 = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
            Checking.check_statuscode(result_delete_2, 204)

            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)



