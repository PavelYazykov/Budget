import allure
import pytest

from common_methods.checking import Checking
from Category.methods.category_methods import CategoryMethods


@pytest.mark.Category
@allure.epic('Get/api/v1/category/{category_id}/ Получение списка категорий по id')
class TestGetCategoryById:

    @allure.description('Получение списка транзакций по  существующей категории')
    def test_01(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Запрос на получение списка категорий"""
        result = CategoryMethods.get_category_by_id(30, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Получение списка транзакций по  несуществующей категории')
    def test_02(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Запрос на получение списка категорий"""
        result = CategoryMethods.get_category_by_id(1000, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 404)

    @allure.description('Значение category_id = 0')
    def test_03(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Запрос на получение списка категорий"""
        result = CategoryMethods.get_category_by_id(0, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Значение category_id = отрицательное число')
    def test_04(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Запрос на получение списка категорий"""
        result = CategoryMethods.get_category_by_id(-20, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Значение category_id = пустое поле -> отрабатывает как ручка get_all_categories')
    def test_05(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Запрос на получение списка категорий"""
        result = CategoryMethods.get_category_by_id('', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Значение category_id = Null')
    def test_06(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Запрос на получение списка категорий"""
        result = CategoryMethods.get_category_by_id(None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Поле category_id = отсутствует -> отрабатывает как ручка get_all_categories')
    def test_07(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Запрос на получение списка категорий"""
        result = CategoryMethods.get_category_by_id_without_id(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Поле category_id = Неверный тип данных')
    def test_08(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Запрос на получение списка категорий"""
        result = CategoryMethods.get_category_by_id('string', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)
