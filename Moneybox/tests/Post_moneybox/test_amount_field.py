import allure
import pytest

from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking
from common_methods.variables import MoneyboxVariables
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
amount = MoneyboxVariables.amount


@pytest.mark.post_moneybox
@allure.epic('Post_moneybox /api/v1/moneybox/ Проверка поля amount')
class TestPostMoneyboxAmount:

    @allure.description('Проверка поля amount - Создание копилки со значением 0')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, amount, access_token)
        create_data = Checking.get_data(post_result)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)

        try:
            """Проверка значения поля amount"""
            with allure.step('Проверка значения поля amount'):
                data = Checking.get_data(post_result)
                assert data['data']['wallet']['amount'] == '0.00'
                print('Значение поля amount соответствует введенному')
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            with allure.step('Удаление копилки'):
                moneybox_id = create_data['data']['id']
                wallet_id = MoneyboxMethods.get_wallet_id(post_result)
                MoneyboxMethods.delete_moneybox_from_bd(moneybox_id, wallet_id)

    @allure.description('Проверка поля amount - Поле отсутствует')
    def test_02(self, auth_fixture):  # Тест будет падать

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox_without_amount(
            to_date, goal, name, currency_id, access_token
        )
        data = Checking.get_data(post_result)
        moneybox_id = data['data']['id']
        wallet_id = MoneyboxMethods.get_wallet_id(post_result)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id, wallet_id)

    @allure.description('Проверка поля amount - Целое число')
    def test_03(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture
        wallet_id = None

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, 100, access_token)
        data_create = Checking.get_data(post_result)
        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        try:
            """Проверка значения поля amount"""
            with allure.step('Проверка значения поля amount'):
                data = Checking.get_data(post_result)
                assert data['data']['wallet']['amount'] == '100.00'
                print('Значение поля amount соответствует введенному')

            """Списание средств с копилки"""
            wallet_id = MoneyboxMethods.get_wallet_id(post_result)
            MoneyboxMethods.consumption('5.5', wallet_id, access_token)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            with allure.step('Удаление копилки'):
                moneybox_id = data_create['data']['id']
                MoneyboxMethods.delete_moneybox_from_bd(moneybox_id, wallet_id)

    @allure.description('Проверка поля amount - Вещественное число (5,5)')
    def test_04(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture
        wallet_id = None

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, 5.5, access_token)
        data_create = Checking.get_data(post_result)
        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        try:
            """Проверка значения поля amount"""
            with allure.step('Проверка значения поля amount'):
                data = Checking.get_data(post_result)
                assert data['data']['wallet']['amount'] == '5.50'
                print('Значение поля amount соответствует введенному')

            """Списание средств с копилки"""
            wallet_id = MoneyboxMethods.get_wallet_id(post_result)
            MoneyboxMethods.consumption('5.5', wallet_id, access_token)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            with allure.step('Удаление копилки'):
                moneybox_id = data_create['data']['id']
                MoneyboxMethods.delete_moneybox_from_bd(moneybox_id, wallet_id)

    @allure.description('Проверка поля amount - Null')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, None, access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Проверка поля amount - Пустое поле')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, '', access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Проверка поля amount - Неверный тип данных (string: "строка")')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, 'string', access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Проверка поля amount - Отрицательное значение')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, -2, access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)



