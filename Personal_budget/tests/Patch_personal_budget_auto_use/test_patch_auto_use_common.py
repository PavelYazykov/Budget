import time

import allure

from common_methods.checking import Checking
from Personal_budget.methods.personal_budget_methods import PersonalBudgetMethods
from Personal_budget.methods.payloads import Variables
from Personal_budget_auto_use.methods.personal_budget_auto_use_methods import PersonalBudgetAutoUseMethods


@allure.epic('Patch/api/v1/personal_budget/{personal_budget_id}/ - Редактирование единоразового и регулярного бюджета -'
             'общие проверки')
class TestPatchPersonalBudgetCommon:

    @allure.description('общие проверки - Запрос на изменение единоразового и регулярного бюджета с валидными данными')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Cоздание персонального и регулярного объектов бюджета"""
        PersonalBudgetMethods.create_pb_and_pb_auto_use(
            20, 'd9424c2f-085a-4a79-bcb0-b967e3cbbfb1', 'IN', 12, 2026, None,
            '12345', '54321', 10, '2026-01-12'
        )

        # try:
        #     result_patch = PersonalBudgetAutoUseMethods.change_personal_budget_auto_use(
        #         personal_budget_auto_use_id, Variables.transaction_type, Variables.category_id,
        #         Variables.subcategory_id, 1000, access_token
        #     )
        #
        #     """Проверка статус кода"""
        #     Checking.check_statuscode(result_patch, 200)
        #
        #     result_get = PersonalBudgetAutoUseMethods.get_personal_budget_auto_use_by_id(
        #         personal_budget_auto_use_id, access_token
        #     )
        #
        #     """Проверка статус кода"""
        #     Checking.check_statuscode(result_get, 200)
        # finally:
        #     result_delete = PersonalBudgetAutoUseMethods.delete_personal_budget_auto_use(
        #         personal_budget_auto_use_id, access_token
        #     )
        #     Checking.check_statuscode(result_delete, 204)



