import allure
import pytest
from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking


@pytest.mark.Regular_outcome
@allure.epic('Delete/api/v1/regular_outcome/{regular_outcome}/ Удаление регулярного платежа')
class TestDeleteRegularOutcome:

    @allure.description('Удаление существующего объекта')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 156, None, 'day', 100, False,
            '2030-12-12', access_token,
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        """Запрос на удаление"""
        result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
        Checking.check_statuscode(result_delete, 204)

    @allure.description('Удаление несуществующего объекта')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на удаление"""
        result_delete = RegularOutcomeMethods.delete_regular_outcome(2000, access_token)
        Checking.check_statuscode(result_delete, 404)

    @allure.description('Удаление объекта - Отрицательное значение id')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на удаление"""
        result_delete = RegularOutcomeMethods.delete_regular_outcome( -200, access_token)
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление объекта - Значение id = 0')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на удаление"""
        result_delete = RegularOutcomeMethods.delete_regular_outcome(0, access_token)
        Checking.check_statuscode(result_delete, 422)

    @allure.description('Удаление объекта - Пустое поле')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на удаление"""
        result_delete = RegularOutcomeMethods.delete_regular_outcome('', access_token)
        Checking.check_statuscode(result_delete, 405)

    @allure.description('Удаление объекта - Поле отсутствует')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на удаление"""
        result_delete = RegularOutcomeMethods.delete_regular_outcome_without_id(access_token)
        Checking.check_statuscode(result_delete, 405)

    @allure.description('Удаление объекта - Значение id = Null')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на удаление"""
        result_delete = RegularOutcomeMethods.delete_regular_outcome(None, access_token)
        Checking.check_statuscode(result_delete, 422)