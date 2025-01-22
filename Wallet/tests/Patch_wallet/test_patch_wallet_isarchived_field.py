import allure
import pytest

from common_methods.checking import Checking
from Wallet.methods.wallet_methods import WalletMethods


@pytest.mark.Wallet
@allure.epic('Patch/api/v1/wallet/{wallet_id}/ Редактирование кошелька - Проверка поля is_archived')
class TestPatchWalletIsArchivedField:

    @allure.description('Проверка поля is_archived - Перенос счета в архив')
    def test_01(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на изменение кошелька"""
        result = WalletMethods.change_wallet_by_id_only_is_archived(
            wallet_id, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения поля"""
        data = Checking.get_data(result)
        assert data['data']['is_archived'] is True

    @allure.description('Проверка поля is_archived - Поле отсутствует')
    def test_02(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на изменение кошелька"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            wallet_id, 2, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Проверка поля is_archived - Перенос счета в архив с положительным amount')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание счета"""
        result_create = WalletMethods.create_wallet(
            'w_1', 2, 10, access_token
        )
        Checking.check_statuscode(result_create, 201)

        data = Checking.get_data(result_create)
        wallet_id = data['data']['id']
        try:
            """Запрос на изменение кошелька"""
            result = WalletMethods.change_wallet_by_id_only_is_archived(
                wallet_id, True, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка значения поля"""
            data = Checking.get_data(result)
            assert data['data']['is_archived'] is True
        except AssertionError:
            raise AssertionError
        finally:
            WalletMethods.delete_wallet_by_id(wallet_id, access_token)

    @allure.description('Проверка поля is_archived - Возврат счета из архива')
    def test_04(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet
        try:
            """Запрос на изменение кошелька"""
            result = WalletMethods.change_wallet_by_id_only_is_archived(
                wallet_id, True, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result, 200)

            """Проверка значения поля"""
            data = Checking.get_data(result)
            assert data['data']['is_archived'] is True

            """Запрос на изменение кошелька"""
            result = WalletMethods.change_wallet_by_id_only_is_archived(
                wallet_id, False, access_token
            )

            """Проверка статус кода"""
            print(result.json())
            Checking.check_statuscode(result, 200)

        except AssertionError:
            raise AssertionError
        finally:
            WalletMethods.delete_wallet_by_id(wallet_id, access_token)

    @allure.description('Проверка поля is_archived - Неверный тип данных (string)')
    def test_05(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на изменение кошелька"""
        result = WalletMethods.change_wallet_by_id_only_is_archived(
            wallet_id, 'string', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля is_archived - Неверный тип данных (integer)')
    def test_06(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на изменение кошелька"""
        result = WalletMethods.change_wallet_by_id_only_is_archived(
            wallet_id, 1234566, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля is_archived - Пустое поле')
    def test_07(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на изменение кошелька"""
        result = WalletMethods.change_wallet_by_id_only_is_archived(
            wallet_id, '', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля is_archived - Null')
    def test_08(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на изменение кошелька"""
        result = WalletMethods.change_wallet_by_id_only_is_archived(
            wallet_id, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)
