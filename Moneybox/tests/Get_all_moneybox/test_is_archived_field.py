import pytest

from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking
import allure
from common_methods.variables import MoneyboxVariables
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
amount = MoneyboxVariables.amount


@pytest.mark.get_moneybox
@pytest.mark.Moneybox
@allure.epic('GET /api/v1/moneybox/ Проверка поля is_archived')
class TestGetAll:

    @allure.description('Пустое поле')
    def test_01(self, auth_fixture, create_moneybox_and_delete):
        """Авторизация"""
        access_token = auth_fixture

        """Get запрос"""
        result_get = MoneyboxMethods.get_all_moneybox_with_params(access_token, '')

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Null')
    def test_02(self, auth_fixture, create_moneybox_and_delete):
        """Авторизация"""
        access_token = auth_fixture

        """Get запрос"""
        result_get = MoneyboxMethods.get_all_moneybox_with_params(access_token, None)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Неверный тип данных')
    def test_03(self, auth_fixture, create_moneybox_and_delete):
        """Авторизация"""
        access_token = auth_fixture

        """Get запрос"""
        result_get = MoneyboxMethods.get_all_moneybox_with_params(access_token, 123456)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
