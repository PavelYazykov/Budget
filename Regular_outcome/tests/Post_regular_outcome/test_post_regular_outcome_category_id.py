import allure
import pytest

from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking


@pytest.mark.regular_outcome_id
@allure.epic('Post/api/v1/regular_outcome/ - Создание нового объекта регулярных списаний - проверка поля category_id')
class TestRegularOutcomeCategoryId:

    @allure.description('проверка поля category_id - Существующий id')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'ttt', 156, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Проверка значения поля category_id"""
            assert data['data']['category_id'] == 156
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля category_id - Поле отсутствует')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome_without_category_id(
            'ttt',  None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля category_id - Null')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'ttt', None, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля category_id - Несуществующий id')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'ttt', 1010, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 404)

    @allure.description('проверка поля category_id - Значение id = 0')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'ttt', 0, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля category_id - Отрицательное значение')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'ttt', -156, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля category_id - Пустое поле')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'ttt', '', None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля category_id - Неверный тип данных string')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'ttt', 'string', None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля category_id - Вещественное число')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'ttt', 1.1, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)
