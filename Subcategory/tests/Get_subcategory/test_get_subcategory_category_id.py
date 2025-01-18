import allure
from Subcategory.methods.subcategory_methods import SubcategoryMethods
from common_methods.checking import Checking
from Subcategory.methods.payloads import SubcategoryPayloads
category_id = 156


@allure.epic('Get/api/v1/subcategory/ - Проверка поля category_id')
class TestGetAllSubcategoriesCategoryId:

    @allure.description('Проверка поля category_id - список подкатегорий по существующей категории')
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
            """Запрос на получение подкатегорий"""
            result_get = SubcategoryMethods.get_subcategory_with_category_id(category_id, access_token)
            Checking.check_statuscode(result_get, 200)

            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_req_fields_get(result_get, SubcategoryPayloads.get_payloads)

            """Проверка статус кода"""
            Checking.check_statuscode(result_get, 200)
        except AssertionError:
            raise AssertionError
        finally:
            result_delete = SubcategoryMethods.delete_subcategory(subcategory_id, access_token)
            Checking.check_statuscode(result_delete, 204)

    @allure.description('Проверка поля category_id - список подкатегорий по несуществующей категории')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на получение подкатегорий"""
        result_get = SubcategoryMethods.get_subcategory_with_category_id(1000, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 404)

    @allure.description('Проверка поля category_id - Значение category_id = 0')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на получение подкатегорий"""
        result_get = SubcategoryMethods.get_subcategory_with_category_id(0, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля category_id - Значение category_id = отрицательное число')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на получение подкатегорий"""
        result_get = SubcategoryMethods.get_subcategory_with_category_id(-5, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля category_id - Значение category_id = пустое поле')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на получение подкатегорий"""
        result_get = SubcategoryMethods.get_subcategory_with_category_id('', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля category_id - Значение category_id Null')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на получение подкатегорий"""
        result_get = SubcategoryMethods.get_subcategory_with_category_id(None, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)

    @allure.description('Проверка поля category_id - Неверный тип данных string')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на получение подкатегорий"""
        result_get = SubcategoryMethods.get_subcategory_with_category_id('string', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 422)












