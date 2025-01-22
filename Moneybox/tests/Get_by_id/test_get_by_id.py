import pytest

from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.auth import Auth
from common_methods.checking import Checking
import allure
from common_methods.variables import MoneyboxVariables
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
amount = MoneyboxVariables.amount
payloads_second_user = 'username=pawel_test_1@rambler.ru&password=Ohranatruda@2'


@pytest.mark.get_moneybox_by_id
@pytest.mark.Moneybox
@allure.epic('GET /api/v1/moneybox/{moneybox_id}/ Получение списка копилок по id')
class TestGetById:

    @allure.description('Существующим ID (авторизованный пользователь)')
    def test_01(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Get запрос"""
        result_get = MoneyboxMethods.get_one_moneybox(
            moneybox_id, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

        """Проверка id копилки"""
        data = Checking.get_data(result_get)
        assert data['data']['id'] == moneybox_id
        print('id копилки соответствует введенному')

        """Проверка наличия обязательных полей и типа данных"""
        # with allure.step('Проверка наличия обязательных полей и типа двнных'):

    @allure.description('Существующим ID (неавторизованный пользователь)')
    def test_02(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

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

    @allure.description('Пустое поле -> Отработает как ручка "получение общего списка копилок"')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Get запрос"""
        result_get = MoneyboxMethods.get_one_moneybox(
            '', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)

    @allure.description('Получение чужой копилки')
    def test_09(self, create_moneybox_and_delete):
        """Создание копилки первого пользователя"""
        moneybox_id_first_user, access_token_first_user = create_moneybox_and_delete

        """Авторизация второго пользователя"""
        auth_result = Auth.auth_with_params('00002', payloads_second_user)
        check = auth_result.json()
        access_token = check.get('access_token')
        Checking.check_statuscode(auth_result, 200)

        """Создание копилки второго пользователя"""
        create_result = MoneyboxMethods.create_moneybox(
            to_date, goal, name, currency_id, amount, access_token
        )
        moneybox_id_second_user = MoneyboxMethods.get_moneybox_id(create_result)
        try:
            """Получение чужой копилки"""
            result_get = MoneyboxMethods.get_one_moneybox(moneybox_id_first_user, access_token)
            Checking.check_statuscode(result_get, 404)
        except AssertionError:
            raise AssertionError
        finally:
            MoneyboxMethods.delete_moneybox(moneybox_id_second_user, access_token)

