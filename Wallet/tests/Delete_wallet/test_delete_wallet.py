import allure
from common_methods.checking import Checking
from Wallet.methods.wallet_methods import WalletMethods
from Auth.methods.auth_methods import AuthMethods
from common_methods.variables import AuthVariables


@allure.epic('Delete/api/v1/wallet/{wallet_id}/ Удаление кошелька')
class TestDeleteWallet:

    @allure.description('Удаление кошелька - Удаление существующего счета')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание кошелька"""
        result_create = WalletMethods.create_wallet(
            'w_2', 2, 0, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        wallet_id = data['data']['id']

        """Удаление кошелька"""
        result_delete = WalletMethods.delete_wallet_by_id(wallet_id, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 204)

        """Получение информации о кошельке"""
        result_get = WalletMethods.get_wallet_by_id(
            wallet_id, access_token
        )
        Checking.check_statuscode(result_get, 403)

    @allure.description('Удаление архивного счета')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание кошелька"""
        result_create = WalletMethods.create_wallet(
            'w_2', 2, 0, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        wallet_id = data['data']['id']

        """Перенос кошелька в архив"""
        result_archived = WalletMethods.change_wallet_by_id_only_is_archived(wallet_id, True, access_token)
        Checking.check_statuscode(result_archived, 200)
        print(result_archived.json())
        print(data['data']['is_archived'])

        """Проверка статус кошелька """
        data = Checking.get_data(result_archived)
        assert data['data']['is_archived'] is True

        """Удаление кошелька"""
        result_delete = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
        Checking.check_statuscode(result_delete, 204)

        """Получение информации о кошельке"""
        result_get = WalletMethods.get_wallet_by_id(
            wallet_id, access_token
        )
        Checking.check_statuscode(result_get, 403)

    @allure.description('Удаление архивного счета')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание кошелька"""
        result_create = WalletMethods.create_wallet(
            'w_2', 2, 100, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        wallet_id = data['data']['id']

        """Проверка баланса кошелька """
        data = Checking.get_data(result_create)
        assert data['data']['amount'] == '100.00'

        """Удаление кошелька"""
        result_delete = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
        Checking.check_statuscode(result_delete, 204)

        """Получение информации о кошельке"""
        result_get = WalletMethods.get_wallet_by_id(
            wallet_id, access_token
        )
        Checking.check_statuscode(result_get, 403)

    @allure.description('Удаление несуществующего счета')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление кошелька"""
        result_delete = WalletMethods.delete_wallet_by_id(101010, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 404)

    @allure.description('Удаление кошелька - Значение wallet_id = 0')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление кошелька"""
        result_delete = WalletMethods.delete_wallet_by_id(0, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление кошелька - Отрицательное значение wallet_id')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление кошелька"""
        result_delete = WalletMethods.delete_wallet_by_id(-11, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление кошелька - Пуcтое поле')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление кошелька"""
        result_delete = WalletMethods.delete_wallet_by_id('', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление кошелька - поле wallet_id отсутствует')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление кошелька"""
        result_delete = WalletMethods.delete_wallet_by_id_without_wallet_id(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 405)

    @allure.description('Удаление кошелька - поле wallet_id null')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление кошелька"""
        result_delete = WalletMethods.delete_wallet_by_id(None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление кошелька - Неверный тип данных')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Удаление кошелька"""
        result_delete = WalletMethods.delete_wallet_by_id('string', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление кошелька другого пользователя')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание кошелька"""
        result_create = WalletMethods.create_wallet(
            'w_2', 2, 100, access_token
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        wallet_id = data['data']['id']

        """Авторизация второго пользователя"""
        result_auth_2 = AuthMethods.login('00002', AuthVariables.auth_payloads_3)
        access_token_2 = result_auth_2.json().get('access_token')

        """Удаление кошелька другого пользователя"""
        result_delete = WalletMethods.delete_wallet_by_id(wallet_id, access_token_2)
        Checking.check_statuscode(result_delete, 403)

        """Удаление кошелька"""
        result_delete_2 = WalletMethods.delete_wallet_by_id(wallet_id, access_token)
        Checking.check_statuscode(result_delete_2, 204)



