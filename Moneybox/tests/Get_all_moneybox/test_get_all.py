from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking, AuthUser
import allure

from common_methods.variables import MoneyboxVariables
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
amount = MoneyboxVariables.amount


@allure.epic('GET /api/v1/moneybox/ Получение списка всех копилок')
class TestGetAll:

    @allure.description('Получение списка всех копилок (авторизованный пользователь)')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        create_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, amount, access_token)

        """Get запрос"""
        result_get = MoneyboxMethods.get_all_moneybox(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

        """Проверка наличия обязательных полей и типа данных в полях"""
        with allure.step('Проверка наличия обязательных полей и типа данных в полях'):
            check_fields = AuthUser()
            print('Все обязательнные поля присутствуют, тип данных соответствует документации')

        """Удаление копилки"""
        data = Checking.get_data(create_result)
        moneybox_id = data['data']['id']
        result_delete = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
        Checking.check_statuscode(result_delete, 204)

    @allure.description('Получение списка всех активных копилок')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Get запрос"""
        result_get = MoneyboxMethods.get_all_moneybox_with_params(access_token, True)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

    @allure.description('Получение списка всех архивных копилок')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Get запрос"""
        result_get = MoneyboxMethods.get_all_moneybox_with_params(access_token, False)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

    @allure.description('Получение списка всех копилок (неавторизованный пользователь)')
    def test_04(self):
        """Get запрос"""
        result_get = MoneyboxMethods.get_all_moneybox_without_auth()

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 401)


