import allure
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking
from common_methods.variables import MoneyboxVariables
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
amount = MoneyboxVariables.amount


@allure.epic("DELETE /api/v1/moneybox/{moneybox_id}/ Удаление копилок")
class TestDelete:

    @allure.description("Удаление копилки авторизованный пользователь")
    def test_01(self, create_moneybox):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox

        """Delete запрос"""
        result_delete = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 204)

        """Подтверждение удаления"""
        with allure.step('Подтверждение удаления'):
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            Checking.check_statuscode(result_delete, 404)
            print('Невозможно удалить несуществующую копилку')
