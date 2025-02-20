import allure
import pytest

from Subcategory.methods.subcategory_methods import SubcategoryMethods
from common_methods.checking import Checking
from Subcategory.methods.payloads import SubcategoryPayloads
category_id = 30


@pytest.mark.Subcategory
@allure.epic('Post/api/v1/subcategory/ - Создание новой подкатеогии - Проверка поля title')
class TestCreateSubcategoriesTitle:

    @allure.description('Проверка поля title - 1 символ')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(category_id, 'd', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_required_fields_post(result_create, SubcategoryPayloads.post_payloads)

            """Проверка значения поля title"""
            assert data['data']['title'] == 'd'
        except AssertionError:
            raise AssertionError
        finally:
            SubcategoryMethods.delete_subcategory(subcategory_id, access_token)

    @allure.description('Проверка поля title - 19 символов')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(
            category_id, 'AssertionAssertionn', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_required_fields_post(result_create, SubcategoryPayloads.post_payloads)

            """Проверка значения поля title"""
            assert data['data']['title'] == 'AssertionAssertionn'
        except AssertionError:
            raise AssertionError
        finally:
            SubcategoryMethods.delete_subcategory(subcategory_id, access_token)

    @allure.description('Проверка поля title - 20 символов')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(
            category_id, 'AssertionAssertionnn', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_required_fields_post(result_create, SubcategoryPayloads.post_payloads)

            """Проверка значения поля title"""
            assert data['data']['title'] == 'AssertionAssertionnn'
        except AssertionError:
            raise AssertionError
        finally:
            SubcategoryMethods.delete_subcategory(subcategory_id, access_token)

    @allure.description('Проверка поля title - цифры')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(
            category_id, '12345', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_required_fields_post(result_create, SubcategoryPayloads.post_payloads)

            """Проверка значения поля title"""
            assert data['data']['title'] == '12345'
        except AssertionError:
            raise AssertionError
        finally:
            SubcategoryMethods.delete_subcategory(subcategory_id, access_token)

    @allure.description('Проверка поля title - Кириллица')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(
            category_id, 'фыва', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_required_fields_post(result_create, SubcategoryPayloads.post_payloads)

            """Проверка значения поля title"""
            assert data['data']['title'] == 'фыва'
        except AssertionError:
            raise AssertionError
        finally:
            SubcategoryMethods.delete_subcategory(subcategory_id, access_token)

    @allure.description('Проверка поля title - Латиница')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(
            category_id, 'asdf', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_required_fields_post(result_create, SubcategoryPayloads.post_payloads)

            """Проверка значения поля title"""
            assert data['data']['title'] == 'asdf'
        except AssertionError:
            raise AssertionError
        finally:
            SubcategoryMethods.delete_subcategory(subcategory_id, access_token)

    @allure.description('Проверка поля title - Пробел')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(
            category_id, 'фыва фыва', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_required_fields_post(result_create, SubcategoryPayloads.post_payloads)

            """Проверка значения поля title"""
            assert data['data']['title'] == 'фыва фыва'
        except AssertionError:
            raise AssertionError
        finally:
            SubcategoryMethods.delete_subcategory(subcategory_id, access_token)

    @allure.description('Проверка поля title - Нижнее подчеркивание')
    def test_08(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(
            category_id, 'фыва_фыва', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_required_fields_post(result_create, SubcategoryPayloads.post_payloads)

            """Проверка значения поля title"""
            assert data['data']['title'] == 'фыва_фыва'
        except AssertionError:
            raise AssertionError
        finally:
            SubcategoryMethods.delete_subcategory(subcategory_id, access_token)

    @allure.description('Проверка поля title - Тире')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(
            category_id, 'фыва-фыва', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_required_fields_post(result_create, SubcategoryPayloads.post_payloads)

            """Проверка значения поля title"""
            assert data['data']['title'] == 'фыва-фыва'
        except AssertionError:
            raise AssertionError
        finally:
            SubcategoryMethods.delete_subcategory(subcategory_id, access_token)

    @allure.description('Проверка поля title - Точка')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(
            category_id, 'фыва.фыва', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 201)

        """Получение id подкатегории"""
        data = Checking.get_data(result_create)
        subcategory_id = data['data']['id']
        try:
            """Проверка наличия обязательных полей"""
            SubcategoryPayloads.check_required_fields_post(result_create, SubcategoryPayloads.post_payloads)

            """Проверка значения поля title"""
            assert data['data']['title'] == 'фыва.фыва'
        except AssertionError:
            raise AssertionError
        finally:
            SubcategoryMethods.delete_subcategory(subcategory_id, access_token)

    @allure.description('Проверка поля title - Существующее наименование подкатегории')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегорий_1"""
        result_create_1 = SubcategoryMethods.create_subcategory(
            category_id, 'Категория_1', access_token
        )
        Checking.check_statuscode(result_create_1, 201)
        data = Checking.get_data(result_create_1)
        subcategory_id = data['data']['id']

        try:
            """Создание подкатегорий_2"""
            result_create_2 = SubcategoryMethods.create_subcategory(
                category_id, 'Категория_1', access_token
            )
            Checking.check_statuscode(result_create_2, 400)

        except AssertionError:
            raise AssertionError
        finally:
            SubcategoryMethods.delete_subcategory(subcategory_id, access_token)

    @allure.description('Проверка поля title - Null')
    def test_12(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(
            category_id, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля title - 21  символ')
    def test_13(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(
            category_id, '123456789012345678901', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля title - Пустое поле')
    def test_14(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(
            category_id, '', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля title - Неверный тип данный integer')
    def test_15(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(
            category_id, 123456, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля title - Спецсимволы')
    def test_16(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory(
            category_id, '!@#$%^&', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)

    @allure.description('Проверка поля title - Поле отсутсвует')
    def test_17(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание подкатегории"""
        result_create = SubcategoryMethods.create_subcategory_without_title(
            category_id, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_create, 422)
