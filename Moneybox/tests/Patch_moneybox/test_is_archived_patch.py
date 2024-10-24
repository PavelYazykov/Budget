import json

import allure

from common_methods.auth import Auth
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking
from common_methods.variables import MoneyboxVariables
# moneybox_id = 478
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
is_archived = MoneyboxVariables.is_archived
amount = MoneyboxVariables.amount


@allure.epic('Patch_moneybox /api/v1/moneybox/{moneybox_id}/ Проверка поля is_archived')
class TestIsArchivedPatch:

    @allure.description('Перенос копилки в архив')
    def test_01(self, auth_fixture, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id = create_moneybox_and_delete

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, name, currency_id, True, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            result_text = result_patch.text
            data = json.loads(result_text)
            assert data['data']['wallet']['is_archived'] is True
            print('Значение соответствует введенному')

    @allure.description('Поле отсутствует')
    def test_02(self, auth_fixture, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id = create_moneybox_and_delete

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox_without_is_archhived(
            moneybox_id, to_date, goal, name, currency_id, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)

    # @allure.description('Перенос копилки в архив с положительным amount')
    # def test_03(self, auth_fixture):
    #
    #     """Авторизация"""
    #     access_token = auth_fixture
    #
    #     """Создание копилки"""
    #     create_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, '100', access_token)
    #     result_text = create_result.text
    #     data = json.loads(result_text)
    #     moneybox_id = data['data']['moneybox_id']
    #     wallet_id = data
    #
    #     """Пополнение копилки"""
    #     data = Checking.get_data()
    #     income = MoneyboxMethods.income()
    #
    #     """Patch_moneybox запрос"""
    #     result_patch = MoneyboxMethods.change_moneybox_without_is_archhived(
    #         moneybox_id, to_date, goal, name, currency_id, access_token
    #     )
    #
    #     """Проверка статус кода"""
    #     Checking.check_statuscode(result_patch, 200)
