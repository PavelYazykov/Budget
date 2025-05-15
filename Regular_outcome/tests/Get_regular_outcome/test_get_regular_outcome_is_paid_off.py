import allure
import pytest

from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking


@pytest.mark.Regular_outcome
@allure.epic('Get/api/v1/regular_outcome/ - Получение всех регулярных списаний - Проверка поля is_paid_off')
class TestGetRegularOutcomeIsPaidOff:

    @allure.description('Проверка поля is_paid_off - Значение True')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result_create = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        regular_outcome_id = data['data']['id']

        try:
            """Запрос на получение списка"""
            result_get = RegularOutcomeMethods.get_regular_outcome_with_is_paid_off(True, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля is_paid_off - Значение False')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result_create = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        regular_outcome_id = data['data']['id']

        try:
            """Запрос на получение списка"""
            result_get = RegularOutcomeMethods.get_regular_outcome_with_is_paid_off(False, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля is_paid_off - Поле отсутствует')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result_create = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        regular_outcome_id = data['data']['id']

        try:
            """Запрос на получение списка"""
            result_get = RegularOutcomeMethods.get_regular_outcome_with_limit(1, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля is_paid_off - Значение Null')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result_create = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        regular_outcome_id = data['data']['id']

        try:
            """Запрос на получение списка"""
            result_get = RegularOutcomeMethods.get_regular_outcome_with_is_paid_off(None, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля is_paid_off - Пустое поле')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result_create = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        regular_outcome_id = data['data']['id']

        try:
            """Запрос на получение списка"""
            result_get = RegularOutcomeMethods.get_regular_outcome_with_is_paid_off('', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля is_paid_off - Неверный тип данных integer')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result_create = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        regular_outcome_id = data['data']['id']

        try:
            """Запрос на получение списка"""
            result_get = RegularOutcomeMethods.get_regular_outcome_with_is_paid_off(1234, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля is_paid_off - Неверный тип данных string')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result_create = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )
        Checking.check_statuscode(result_create, 201)
        data = Checking.get_data(result_create)
        regular_outcome_id = data['data']['id']

        try:
            """Запрос на получение списка"""
            result_get = RegularOutcomeMethods.get_regular_outcome_with_is_paid_off('string', access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 422)
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)