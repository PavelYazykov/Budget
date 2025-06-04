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
@allure.epic('Post_moneybox /api/v1/moneybox/ Проверка поля currency_id')
class TestPostMoneyboxCurrencyId:

    @allure.description('Проверка поля currency_id - Существующий id')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, amount, access_token)
        moneybox_id = MoneyboxMethods.get_moneybox_id(post_result)
        wallet_id = MoneyboxMethods.get_wallet_id(post_result)
        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        try:
            """Проверка поля currency_id"""
            with allure.step('Проверка значения поля currency_id'):
                data = Checking.get_data(post_result)
                assert data['data']['wallet']['currency_id'] == currency_id
                print('Значение поля currency_id соответствует введенному')
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            with allure.step('Удаление копилки'):
                MoneyboxMethods.delete_moneybox_from_bd(moneybox_id, wallet_id)

    @allure.description('Проверка поля currency_id - Поле отсутствует')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox_without_currency(to_date, goal, name, amount, access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Проверка поля currency_id - Пустое поле')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, '', amount, access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Проверка поля currency_id - Null')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, None, amount, access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Проверка поля currency_id - Несуществующий id')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, 5555, amount, access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 404)

    @allure.description('Проверка поля currency_id - id = 0')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, 0, amount, access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Проверка поля currency_id - Неверный тип данных (string: "строка")')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, 'string', amount, access_token)

        """Проверка статус кода"""
        moneybox_id = Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Проверка поля currency_id - Вещественное число (id = 2,3)')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, 2.3, amount, access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Проверка поля currency_id - Спецсимволы')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, '@#$%', amount, access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Проверка поля currency_id - Отрицательный id')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, -1, amount, access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)


