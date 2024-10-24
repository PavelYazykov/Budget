from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking, Moneybox
import allure
from common_methods.variables import MoneyboxVariables
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
amount = MoneyboxVariables.amount
moneybox_id = 410


@allure.epic('GET /api/v1/moneybox/{moneybox_id}/ Получение списка копилок по id')
class TestGetById:

    @allure.description('Существующим ID (авторизованный пользователь)')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Get запрос"""
        result_get = MoneyboxMethods.get_one_moneybox(
            moneybox_id, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

        """Проверка id копилки"""
        data = Checking.get_data(result_get)
        assert data['data']['id'] == 410
        print('id копилки соответствует введенному')

        """Проверка наличия обязательных полей и типа данных"""
        with allure.step('Проверка наличия обязательных полей и типа двнных'):
            check_fields = Moneybox()

    @allure.description('Существующим ID (неавторизованный пользователь)')
    def test_02(self):

        """Get запрос"""
        result_get = MoneyboxMethods.get_one_moneybox_without_auth(
            moneybox_id
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 401)

    @allure.description('Несуществующий id')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Get запрос"""
        result_get = MoneyboxMethods.get_one_moneybox(
            1, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 404)

    @allure.description('id = вещественное число')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Get запрос"""
        result_get = MoneyboxMethods.get_one_moneybox(
            2.3, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('id = 0')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Get запрос"""
        result_get = MoneyboxMethods.get_one_moneybox(
            0, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Отрицательное число')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Get запрос"""
        result_get = MoneyboxMethods.get_one_moneybox(
            -1, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('id = string ("строка")')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Get запрос"""
        result_get = MoneyboxMethods.get_one_moneybox(
            'string', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Пустое поле')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Get запрос"""
        result_get = MoneyboxMethods.get_one_moneybox(
            '', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Получение чужой копилки')
    def test_09(self, auth_fixture):
        pass  # Дописать метод

