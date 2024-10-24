import allure
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking

moneybox_id = 606


@allure.epic("DELETE /api/v1/moneybox/{moneybox_id}/ Удаление копилок")
class TestDelete:

    @allure.description("Удаление копилки авторизованный пользователь")
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Delete запрос"""
        result_delete = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
        print(result_delete.text)

        """Проверка статус кода"""
        Checking.check_statuscode(result_delete, 204)
        print(f'Копилка № {moneybox_id} удалена')

        """Подтверждение удаления"""
        with allure.step('Подтверждение удаления'):
            result_delete = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            Checking.check_statuscode(result_delete, 404)
            print('Невозможно удалить несуществующую копилку')
