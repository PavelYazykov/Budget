import allure
from common_methods.checking import Checking
from Category.methods.category_methods import CategoryMethods


@allure.epic('Get/api/v1/category/ Получение списка категорий - проверка поля transaction_type')
class TestGetCategoryTransactionType:  # РЕАЛИЗОВАТЬ СОЗДАНИЕ ТРАНЗАКЦИИ

    @allure.description('Проверка поля transaction type - Значение Income')
    def test_01(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Запрос на получение списка категорий"""
        result = CategoryMethods.get_category_with_transaction_type('Income', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Проверка поля transaction type - Значение Consumption')
    def test_02(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Запрос на получение списка категорий"""
        result = CategoryMethods.get_category_with_transaction_type('Consumption', access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Проверка поля transaction type - Значение Transfer between wallets')
    def test_03(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Запрос на получение списка категорий"""
        result = CategoryMethods.get_category_with_transaction_type(
            'Transfer between wallets', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 200)

    @allure.description('Проверка поля transaction type - Несуществующее значение')
    def test_04(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Запрос на получение списка категорий"""
        result = CategoryMethods.get_category_with_transaction_type(
            'Transfer', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля transaction type - Пустое поле')
    def test_05(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Запрос на получение списка категорий"""
        result = CategoryMethods.get_category_with_transaction_type(
            '', access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля transaction type - Null')
    def test_06(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Запрос на получение списка категорий"""
        result = CategoryMethods.get_category_with_transaction_type(
            None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)

    @allure.description('Проверка поля transaction type - Неверный тип данных integer')
    def test_07(self, auth_fixture):
        """Автризация"""
        access_token = auth_fixture

        """Запрос на получение списка категорий"""
        result = CategoryMethods.get_category_with_transaction_type(
            123456, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 422)
