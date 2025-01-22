import allure
import pytest

from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking
from Subcategory.methods.subcategory_methods import SubcategoryMethods
from Regular_outcome.methods.payloads import RegularOutcomePayloads


@pytest.mark.Regular_outcome
@allure.epic('Post/api/v1/regular_outcome/ - Создание нового объекта регулярных списаний - проверка поля subcategory_id')
class TestRegularOutcomeSubcategoryId:

    @allure.description('проверка поля subcategory_id - Существующий id')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание подкатегории"""
        subcategory_result = SubcategoryMethods.create_subcategory(
            156, 'desr', access_token
        )
        Checking.check_statuscode(subcategory_result, 201)
        data = Checking.get_data(subcategory_result)
        subcategory_id = data['data']['id']

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'ttt', 156, subcategory_id, 'day', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Проверка значения поля subcategory_id"""
            assert data['data']['subcategory_id'] == subcategory_id
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

            delete_subcategory = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(delete_subcategory, 204)

    @allure.description('проверка поля subcategory_id - Поле отсутствует')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome_without_subcategory(
            'ttt', 156, 'day', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """проверка наличия обязательных полей"""
            RegularOutcomePayloads.check_required_fields(result, RegularOutcomePayloads.post_payloads)
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля subcategory_id - Null')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'ttt', 156, None, 'day', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """проверка наличия обязательных полей"""
            RegularOutcomePayloads.check_required_fields(result, RegularOutcomePayloads.post_payloads)
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля subcategory_id - Несуществующий id')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'ttt', 156, 1000, 'day', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 404)

    @allure.description('проверка поля subcategory_id - Значение id = 0')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'ttt', 156, 0, 'day', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля subcategory_id - Отрицательное значение')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'ttt', 156, -5, 'day', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля subcategory_id - Пустое поле')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'ttt', 156, '', 'day', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля subcategory_id - Неверный тип данных string')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'ttt', 156, 'string', 'day', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля subcategory_id - Вещественное число')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'ttt', 156, 1.1, 'day', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)
