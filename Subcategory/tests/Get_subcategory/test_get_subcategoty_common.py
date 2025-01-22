import allure
import pytest

from Subcategory.methods.subcategory_methods import SubcategoryMethods
from common_methods.checking import Checking


@pytest.mark.Subcategory
@allure.epic('Get/api/v1/subcategory/ - Получение списка всех подкатегорий без параметров')
class TestGetAllSubcategoriesCommon:

    @allure.description('Получение списка всех подкатегорий без параметров - авторизованный пользователь')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Get запрос"""
        result = SubcategoryMethods.get_subcategory(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)
        # data = Checking.get_data(result)
        # category_id = data['data'][0]['category_id']
        # print(category_id)

    @allure.description('Получение списка всех подкатегорий без параметров - неавторизованный пользователь')
    def test_02(self):

        """Get запрос"""
        result = SubcategoryMethods.get_subcategory_without_auth()

        """Проверка статус кода"""
        Checking.check_statuscode(result, 401)


