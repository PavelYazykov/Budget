import json

import pytest

from Category.methods.payloads import CategoryPayloads
import allure
from common_methods.checking import Checking
from Category.methods.category_methods import CategoryMethods


@pytest.mark.Category
@allure.epic('Get/api/v1/category/ Получение списка категорий - общие проверки')
class TestGetCategoryCommon:

    @allure.description('Получение списка всех категорий (авторизованный пользователь) без параметров')
    def test_01(self, auth_fixture):
        """Авторизацтя"""
        access_token = auth_fixture

        """Запрос категорий"""
        result = CategoryMethods.get_category(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

        """Проверка наличия обязательных полей"""
        CategoryPayloads.check_required_fields(result, CategoryPayloads.payloads)

    @allure.description('Получение списка всех категорий (неавторизованный пользователь) без параметров')
    def test_02(self):
        """Запрос категорий"""
        result = CategoryMethods.get_category_without_access_token()

        """Проверка статус кода"""
        Checking.check_statuscode(result, 401)
