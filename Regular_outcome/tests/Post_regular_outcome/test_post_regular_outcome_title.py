import allure
import pytest

from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking


@pytest.mark.regular_outcome_id
@allure.epic('Post/api/v1/regular_outcome/ - Создание нового объекта регулярных списаний - проверка поля title')
class TestRegularOutcomeTitle:

    @allure.description('проверка поля title - 1 символ')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            't', 156, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Проверка значения поля title"""
            assert data['data']['title'] == 't'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - 20 символов')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'tttttttttttttttttttt', 156, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Проверка значения поля title"""
            assert data['data']['title'] == 'tttttttttttttttttttt'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Цифры')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            '123', 156, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Проверка значения поля title"""
            assert data['data']['title'] == '123'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Кириллица')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'йцу', 156, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Проверка значения поля title"""
            assert data['data']['title'] == 'йцу'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Латиница')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'qwe', 156, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Проверка значения поля title"""
            assert data['data']['title'] == 'qwe'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - пробел')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'qwe r', 156, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Проверка значения поля title"""
            assert data['data']['title'] == 'qwe r'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Нижнее подчеркивание')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'qwe_r', 156, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Проверка значения поля title"""
            assert data['data']['title'] == 'qwe_r'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Тире')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'qwe-r', 156, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Проверка значения поля title"""
            assert data['data']['title'] == 'qwe-r'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - Точка ')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'qwe.r', 156, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']
        try:
            """Проверка значения поля title"""
            assert data['data']['title'] == 'qwe.r'
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('проверка поля title - null ')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            None, 156, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля title - 21 символ ')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'ttttttttttttttttttttq', 156, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля title - Пустое поле')
    def test_12(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            '', 156, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля title - Неверный тип данный integer')
    def test_13(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            1234, 156, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля title - Спецсимволы')
    def test_14(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            '!@#$%', 156, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)

    @allure.description('проверка поля title - Поле отсутствует')
    def test_15(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome_without_title(
            156, None, 'День', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            data = Checking.get_data(result)
            regular_outcome_id = data['data']['id']
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
        Checking.check_statuscode(result, 422)





