import allure
import pytest
from Regular_outcome.methods.payloads import RegularOutcomePayloads
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking


@pytest.mark.Regular_outcome
@allure.epic('Get/api/v1/regular_outcome/{regular_outcome}/ - Получение регулярных списаний по id')
class TestGetRegularOutcomeById:

    @allure.description('Получение регулярных списаний с существующим id')
    def test_01(self, auth_fixture):
        """Aвторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result_create = RegularOutcomeMethods.create_regular_outcome(
            'title', 156, None, 'day', 100, False,
            '2030-12-12', access_token,
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        regular_outcome_id = data['data']['id']
        try:
            """Запрос на получение информации о регулярном платеже"""
            result_get = RegularOutcomeMethods.get_regular_outcome_by_id(regular_outcome_id, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка наличия обязательных полей"""
            RegularOutcomePayloads.check_required_fields(result_get, RegularOutcomePayloads.post_payloads)

            """Проверка поля id"""
            get_data = Checking.get_data(result_get)
            assert get_data['data']['id'] == regular_outcome_id
        except AssertionError:
            raise AssertionError
        finally:
            delete_result = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(delete_result, 204)

    @allure.description('Получение регулярных списаний с несуществующим id')
    def test_02(self, auth_fixture):
        """Aвторизация"""
        access_token = auth_fixture

        """Запрос на получение информации о регулярном платеже"""
        result_get = RegularOutcomeMethods.get_regular_outcome_by_id(2000, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 404)

    @allure.description('Получение регулярных списаний с id = 0')
    def test_03(self, auth_fixture):
        """Aвторизация"""
        access_token = auth_fixture

        """Запрос на получение информации о регулярном платеже"""
        result_get = RegularOutcomeMethods.get_regular_outcome_by_id(0, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Получение регулярных списаний с id = пустое поле')
    def test_04(self, auth_fixture):
        """Aвторизация"""
        access_token = auth_fixture

        """Запрос на получение информации о регулярном платеже"""
        result_get = RegularOutcomeMethods.get_regular_outcome_by_id(0, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Получение регулярных списаний с id = Null')
    def test_05(self, auth_fixture):
        """Aвторизация"""
        access_token = auth_fixture

        """Запрос на получение информации о регулярном платеже"""
        result_get = RegularOutcomeMethods.get_regular_outcome_by_id(None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Получение регулярных списаний с id = Неверный тип данных  string')
    def test_06(self, auth_fixture):
        """Aвторизация"""
        access_token = auth_fixture

        """Запрос на получение информации о регулярном платеже"""
        result_get = RegularOutcomeMethods.get_regular_outcome_by_id('string', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Получение регулярных списаний с id = Отрицательное значение')
    def test_07(self, auth_fixture):
        """Aвторизация"""
        access_token = auth_fixture

        """Запрос на получение информации о регулярном платеже"""
        result_get = RegularOutcomeMethods.get_regular_outcome_by_id(-2, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

