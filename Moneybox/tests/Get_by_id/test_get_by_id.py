import time

import pytest
from common_methods.variables import AuthVariables
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.auth import Auth
from common_methods.checking import Checking
import allure
from common_methods.variables import MoneyboxVariables
from Auth.methods.auth_methods import AuthMethods
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
amount = MoneyboxVariables.amount


@pytest.mark.get_moneybox_by_id
@pytest.mark.Moneybox
@allure.epic('GET /api/v1/moneybox/{moneybox_id}/ Получение списка копилок по id')
class TestGetMoneyboxById:

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

    @allure.description('Получение чужой копилки')
    def test_09(self, create_moneybox_and_delete):
        """Создание копилки первого пользователя"""
        moneybox_id_first_user, access_token_first_user = create_moneybox_and_delete

        """Создание второго пользователя"""
        result_create_second_user = AuthMethods.registration(
            AuthVariables.email_for_create_user, AuthVariables.password, AuthVariables.last_name,
            AuthVariables.first_name,
            AuthVariables.middle_name, AuthVariables.phone_for_create_user, AuthVariables.date_of_birth
        )
        Checking.check_statuscode(result_create_second_user, 201)
        data, user_id = AuthMethods.get_id(result_create_second_user)
        try:
            """Верификация пользователя"""
            AuthMethods.verification_user(user_id)
            time.sleep(2)

            """Авторизация второго пользователя"""
            auth_result = Auth.auth_with_params(
                '00002', f'username={AuthVariables.email_for_create_user}&password={AuthVariables.password}'
            )
            check = auth_result.json()
            access_token_2 = check.get('access_token')
            Checking.check_statuscode(auth_result, 200)

            """Получение чужой копилки"""
            result_get = MoneyboxMethods.get_one_moneybox(moneybox_id_first_user, access_token_2)
            Checking.check_statuscode(result_get, 404)
        finally:

            """Удаление пользователя из БД"""
            AuthMethods.delete_user(user_id)


