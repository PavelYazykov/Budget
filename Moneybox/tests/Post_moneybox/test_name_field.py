import allure
import pytest

from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking

from common_methods.variables import MoneyboxVariables
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
amount = MoneyboxVariables.amount


@pytest.mark.post_moneybox
@allure.epic('Post_moneybox /api/v1/moneybox/ Проверка поля name')
class TestPostMoneyboxName:

    @allure.description('Проверка поля name  - 1 символ')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'М', currency_id, amount, access_token
        )
        moneybox_id = MoneyboxMethods.get_moneybox_id(post_result)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        try:
            """Проверка значения поля name"""
            with allure.step('Проверка значения поля name'):
                data = Checking.get_data(post_result)
                assert data['data']['wallet']['name'] == 'М'
                print('Значение поля соответствует введенному')
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('Проверка поля name - 19 символов')
    def test_02(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'мумумумумумумумумум', currency_id, amount, access_token
        )
        moneybox_id = MoneyboxMethods.get_moneybox_id(post_result)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        try:
            """Проверка значения поля name"""
            with allure.step('Проверка значения поля name'):
                data = Checking.get_data(post_result)
                assert data['data']['wallet']['name'] == 'мумумумумумумумумум'
                print('Значение поля соответствует введенному')
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('Проверка поля name - 20 символов')
    def test_03(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'мумумумумумумумумуму', currency_id, amount, access_token
        )
        moneybox_id = MoneyboxMethods.get_moneybox_id(post_result)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        try:
            """Проверка значения поля name"""
            with allure.step('Проверка значения поля name'):
                data = Checking.get_data(post_result)
                assert data['data']['wallet']['name'] == 'мумумумумумумумумуму'
                print('Значение поля соответствует введенному')
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('Проверка поля name - Цифры (0123456789)')
    def test_04(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, '0123456789', currency_id, amount, access_token
        )
        moneybox_id = MoneyboxMethods.get_moneybox_id(post_result)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        try:
            """Проверка значения поля name"""
            with allure.step('Проверка значения поля name'):
                data = Checking.get_data(post_result)
                assert data['data']['wallet']['name'] == '0123456789'
                print('Значение поля соответствует введенному')
        finally:
            """Удаление копилки"""
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('Проверка поля name - Кириллица (Счёт)')
    def test_05(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'Счёт', currency_id, amount, access_token
        )
        moneybox_id = MoneyboxMethods.get_moneybox_id(post_result)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        try:
            """Проверка значения поля name"""
            with allure.step('Проверка значения поля name'):
                data = Checking.get_data(post_result)
                assert data['data']['wallet']['name'] == 'Счёт'
                print('Значение поля соответствует введенному')
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('Проверка поля name - Латиница (Moneybox)')
    def test_06(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'Moneybox', currency_id, amount, access_token
        )
        moneybox_id = MoneyboxMethods.get_moneybox_id(post_result)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        try:
            """Проверка значения поля name"""
            with allure.step('Проверка значения поля name'):
                data = Checking.get_data(post_result)
                assert data['data']['wallet']['name'] == 'Moneybox'
                print('Значение поля соответствует введенному')
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

    @allure.description('Проверка поля name - Пробел')
    def test_07(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'Мой счет', currency_id, amount, access_token
        )
        moneybox_id = MoneyboxMethods.get_moneybox_id(post_result)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        try:
            """Проверка значения поля name"""
            with allure.step('Проверка значения поля name'):
                data = Checking.get_data(post_result)
                assert data['data']['wallet']['name'] == 'Мой счет'
                print('Значение поля соответствует введенному')
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('Проверка поля name - Нижнее подчеркивание')
    def test_08(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'Мой_счет', currency_id, amount, access_token
        )
        moneybox_id = MoneyboxMethods.get_moneybox_id(post_result)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        try:
            """Проверка значения поля name"""
            with allure.step('Проверка значения поля name'):
                data = Checking.get_data(post_result)
                assert data['data']['wallet']['name'] == 'Мой_счет'
                print('Значение поля соответствует введенному')
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('Проверка поля name - Тире')
    def test_09(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'Мой-счет', currency_id, amount, access_token
        )
        moneybox_id = MoneyboxMethods.get_moneybox_id(post_result)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        try:
            """Проверка значения поля name"""
            with allure.step('Проверка значения поля name'):
                data = Checking.get_data(post_result)
                assert data['data']['wallet']['name'] == 'Мой-счет'
                print('Значение поля соответствует введенному')
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('Проверка поля name - Точка')
    def test_10(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'Мой.счет', currency_id, amount, access_token
        )
        moneybox_id = MoneyboxMethods.get_moneybox_id(post_result)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        try:
            """Проверка значения поля name"""
            with allure.step('Проверка значения поля name'):
                data = Checking.get_data(post_result)
                assert data['data']['wallet']['name'] == 'Мой.счет'
                print('Значение поля соответствует введенному')
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('Проверка поля name - Поле отсутствует')
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

    @allure.description('Проверка поля name - Null')
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

    @allure.description('Проверка поля name - 21 символ')
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

    @allure.description('Проверка поля name - Спецсимволы')
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


