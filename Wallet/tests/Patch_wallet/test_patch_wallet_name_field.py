import allure
from common_methods.checking import Checking
from Wallet.methods.wallet_methods import WalletMethods


@allure.epic('Patch/api/v1/wallet/{wallet_id}/ Редактирование кошелька - Проверка поля name')
class TestPatchWalletName:

    @allure.description('Проверка поля name - 1 символ')
    def test_01(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_name_field(
            wallet_id, 'a', access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения изменяемого поля"""
        data = Checking.get_data(result)
        assert data['data']['name'] == 'a'

    @allure.description('Проверка поля name - 19 символов')
    def test_02(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_name_field(
            wallet_id, 'aaaaaaaaaaaaaaaaaaa', access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения изменяемого поля"""
        data = Checking.get_data(result)
        assert data['data']['name'] == 'aaaaaaaaaaaaaaaaaaa'

    @allure.description('Проверка поля name - 20 символов')
    def test_03(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_name_field(
            wallet_id, 'aaaaaaaaaaaaaaaaaaaq', access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения изменяемого поля"""
        data = Checking.get_data(result)
        assert data['data']['name'] == 'aaaaaaaaaaaaaaaaaaaq'

    @allure.description('Проверка поля name - Цифры')
    def test_04(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_name_field(
            wallet_id, '123456', access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения изменяемого поля"""
        data = Checking.get_data(result)
        assert data['data']['name'] == '123456'

    @allure.description('Проверка поля name - Кириллица')
    def test_05(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_name_field(
            wallet_id, 'йцуке', access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения изменяемого поля"""
        data = Checking.get_data(result)
        assert data['data']['name'] == 'йцуке'

    @allure.description('Проверка поля name - Латиница')
    def test_06(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_name_field(
            wallet_id, 'asdf', access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения изменяемого поля"""
        data = Checking.get_data(result)
        assert data['data']['name'] == 'asdf'

    @allure.description('Проверка поля name - Пробел')
    def test_07(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_name_field(
            wallet_id, 'as df', access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения изменяемого поля"""
        data = Checking.get_data(result)
        assert data['data']['name'] == 'as df'

    @allure.description('Проверка поля name - Нижнее подчеркивание')
    def test_08(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_name_field(
            wallet_id, 'as_df', access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения изменяемого поля"""
        data = Checking.get_data(result)
        assert data['data']['name'] == 'as_df'

    @allure.description('Проверка поля name - тире')
    def test_09(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_name_field(
            wallet_id, 'as-df', access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения изменяемого поля"""
        data = Checking.get_data(result)
        assert data['data']['name'] == 'as-df'

    @allure.description('Проверка поля name - Точка')
    def test_10(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_name_field(
            wallet_id, 'as.df', access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка значения изменяемого поля"""
        data = Checking.get_data(result)
        assert data['data']['name'] == 'as.df'

    @allure.description('Проверка поля name - Поле отсутствует')
    def test_11(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_currency_field(
            wallet_id, 2, access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Проверка поля name - Пустое поле')
    def test_12(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_name_field(
            wallet_id, '', access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля name - Null')
    def test_13(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_name_field(
            wallet_id, None, access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля name - 21 символ')
    def test_14(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_name_field(
            wallet_id, 'aaaaaaaaaaaaaaaaaaaqw', access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля name - Спецсимволы')
    def test_15(self, create_and_delete_wallet):
        """Авторизация"""
        access_token, wallet_id = create_and_delete_wallet

        """Запрос на редактирование кошелька"""
        result = WalletMethods.change_wallet_by_id_only_name_field(
            wallet_id, '!@#$%^^&&*', access_token
        )

        """Провекрка статус кода"""
        Checking.check_statuscode(result, 422)



