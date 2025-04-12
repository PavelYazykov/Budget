import allure
import pytest

from Subcategory.methods.subcategory_methods import SubcategoryMethods
from common_methods.checking import Checking
from Subcategory.methods.payloads import SubcategoryPayloads
category_id = 30


@pytest.mark.Subcategory
@allure.epic('Get/api/v1/subcategory/ - Получение информации о подкатегорий по id')
class TestGetSubcategoriesById:

    @allure.description('Получение информации о подкатегорий по id - Cуществующая подкатегория')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'name', access_token)
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        print(subcategory_id)
        try:
            """Запрос на получение информации о подкатегории"""
            result_get = SubcategoryMethods.get_subcategory_by_id(subcategory_id, access_token)

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get_by_id(result_get, SubcategoryPayloads.get_payloads_by_id)
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Получение информации о подкатегорий по id - несуществующая подкатегория')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на получение информации о подкатегории"""
        result_get = SubcategoryMethods.get_subcategory_by_id(1000, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 404)

    @allure.description('Получение информации о подкатегорий по id - несуществующая подкатегория')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на получение информации о подкатегории"""
        result_get = SubcategoryMethods.get_subcategory_by_id(1000, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 404)

    @allure.description('Получение информации о подкатегорий по id - Значение subcategory_id = 0')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на получение информации о подкатегории"""
        result_get = SubcategoryMethods.get_subcategory_by_id(0, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Получение информации о подкатегорий по id - Значение subcategory_id = отрицательное число')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на получение информации о подкатегории"""
        result_get = SubcategoryMethods.get_subcategory_by_id(-30, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Получение информации о подкатегорий по id - Значение subcategory_id = пустое поле')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на получение информации о подкатегории"""
        result_get = SubcategoryMethods.get_subcategory_by_id('', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 404)

    @allure.description('Получение информации о подкатегорий по id - Значение subcategory_id = Null')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на получение информации о подкатегории"""
        result_get = SubcategoryMethods.get_subcategory_by_id(None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Получение информации о подкатегорий по id - Неверный тип данных string')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на получение информации о подкатегории"""
        result_get = SubcategoryMethods.get_subcategory_by_id('string', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)



