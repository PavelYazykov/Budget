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
class TestGetAllMoneyboxIsArchived:

    @allure.description('Проверка поля is_archived - Пустое поле')
    def test_01(self, create_moneybox_and_delete):
        """Авторизация"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Get запрос"""
        result_get = MoneyboxMethods.get_all_moneybox_with_params(access_token, '')

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля is_archived - Null')
    def test_02(self, create_moneybox_and_delete):
        """Авторизация"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Get запрос"""
        result_get = MoneyboxMethods.get_all_moneybox_with_params(access_token, None)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля is_archived - Неверный тип данных')
    def test_03(self, create_moneybox_and_delete):
        """Авторизация"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Get запрос"""
        result_get = MoneyboxMethods.get_all_moneybox_with_params(access_token, 123456)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)
