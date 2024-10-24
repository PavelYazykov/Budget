import allure
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking

from common_methods.variables import MoneyboxVariables
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
amount = MoneyboxVariables.amount


@allure.epic('Post_moneybox /api/v1/moneybox/ Проверка поля name')
class TestName:

    @allure.description('1 символ')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'М', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)

        """Проверка значения поля name"""
        with allure.step('Проверка значения поля name'):
            data = Checking.get_data(post_result)
            assert data['data']['wallet']['name'] == 'М'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

    @allure.description('19 символов')
    def test_02(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'мумумумумумумумумум', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)

        """Проверка значения поля name"""
        with allure.step('Проверка значения поля name'):
            data = Checking.get_data(post_result)
            assert data['data']['wallet']['name'] == 'мумумумумумумумумум'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

    @allure.description('20 символов')
    def test_03(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'мумумумумумумумумуму', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)

        """Проверка значения поля name"""
        with allure.step('Проверка значения поля name'):
            data = Checking.get_data(post_result)
            assert data['data']['wallet']['name'] == 'мумумумумумумумумуму'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

    @allure.description('Цифры (0123456789)')
    def test_04(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, '0123456789', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)

        """Проверка значения поля name"""
        with allure.step('Проверка значения поля name'):
            data = Checking.get_data(post_result)
            assert data['data']['wallet']['name'] == '0123456789'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

    @allure.description('Кириллица (Счёт)')
    def test_05(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'Счёт', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)

        """Проверка значения поля name"""
        with allure.step('Проверка значения поля name'):
            data = Checking.get_data(post_result)
            assert data['data']['wallet']['name'] == 'Счёт'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

    @allure.description('Латиница (Moneybox)')
    def test_06(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'Moneybox', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)

        """Проверка значения поля name"""
        with allure.step('Проверка значения поля name'):
            data = Checking.get_data(post_result)
            assert data['data']['wallet']['name'] == 'Moneybox'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

    @allure.description('Пробел')
    def test_07(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'Мой счет', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)

        """Проверка значения поля name"""
        with allure.step('Проверка значения поля name'):
            data = Checking.get_data(post_result)
            assert data['data']['wallet']['name'] == 'Мой счет'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

    @allure.description('Нижнее подчеркивание')
    def test_08(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'Мой_счет', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)

        """Проверка значения поля name"""
        with allure.step('Проверка значения поля name'):
            data = Checking.get_data(post_result)
            assert data['data']['wallet']['name'] == 'Мой_счет'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

    @allure.description('Тире')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'Мой-счет', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)

        """Проверка значения поля name"""
        with allure.step('Проверка значения поля name'):
            data = Checking.get_data(post_result)
            assert data['data']['wallet']['name'] == 'Мой-счет'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

    @allure.description('Точка')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'Мой.счет', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)

        """Проверка значения поля name"""
        with allure.step('Проверка значения поля name'):
            data = Checking.get_data(post_result)
            assert data['data']['wallet']['name'] == 'Мой.счет'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

    @allure.description('Поле отсутствует')
    def test_11(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox_without_name(
            to_date, goal, currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Пустое поле')
    def test_12(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, '', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Null')
    def test_13(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, None, currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('21 символ')
    def test_14(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'ZzzzzzzzzqZzzzzzzzzqw', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Спецсимволы')
    def test_15(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, '@#$%^&', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)


