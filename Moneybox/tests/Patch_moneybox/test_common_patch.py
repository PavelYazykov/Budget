import allure
from Moneybox.methods.payloads import Payloads
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking
from common_methods.variables import MoneyboxVariables
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
from Auth.methods.auth_methods import AuthMethods
from common_methods.variables import AuthVariables
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
is_archived = MoneyboxVariables.is_archived
amount = MoneyboxVariables.amount


@allure.epic('Patch_moneybox /api/v1/moneybox/{moneybox_id}/ Редактирование копилок, общие проверки')
class TestCommonPatch:

    @allure.description('С существующим ID и валидными значениями в полях (авторизованный пользователь')
    def test_01(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)
        try:
            """Проверка наличия обязательных полей"""
            MoneyboxMethods.post_check_exist_req_fields(result_patch, Payloads.required_fields())
        except AssertionError:
            print(result_patch.text)
            raise AssertionError
        finally:
            """Удаление копилки"""
            with allure.step('Удаление копилки'):
                moneybox_id = MoneyboxMethods.get_moneybox_id(result_patch)
                MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

    @allure.description('С существующим ID и валидными значениями в полях (неавторизованный пользователь')
    def test_02(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox_without_auth(
            moneybox_id, to_date, goal, name, currency_id, is_archived
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 401)

    @allure.description('C пустым body')
    def test_03(self, create_moneybox_and_delete):
        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox_without_body(moneybox_id, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Несуществующий id')
    def test_04(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            '1', to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 404)

    @allure.description('id = 0')
    def test_05(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            '0', to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('id = вещественное число (1,5)')
    def test_06(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            '1.5', to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('id = -1')
    def test_07(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            '-1', to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('id = -1')
    def test_08(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            '-1', to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('id = string ("строка")')
    def test_09(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            'string', to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Пустое поле')
    def test_10(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            '', to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 405)

    @allure.description('Отсутствует id')
    def test_11(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox_without_moneybox_id(
            to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 405)

    @allure.description('Null')
    def test_12(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Patch_moneybox запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            None, to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 422)

    @allure.description('Попытка внести изменения в копилку после достижения цели')
    def test_13(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        result_create = MoneyboxMethods.create_moneybox(
            to_date, 1000, 'name', 2, 0, access_token
        )

        """Получение moneybox_id и wallet_id"""
        data = Checking.get_data(result_create)
        moneybox_id = data['data']['id']
        wallet_id = data['data']['wallet']['id']
        try:
            """Создание транзакции"""
            result_income = PersonalTransactionMethods.create_personal_transaction(
                1000, 'description', 'Income', '2024-12-12',
                None, wallet_id, 156, None, access_token
            )
            Checking.check_statuscode(result_income, 201)
            result_get = MoneyboxMethods.get_one_moneybox(moneybox_id, access_token)
            Checking.check_statuscode(result_get, 200)

            """Запрос на изменение копилки"""
            result_change = MoneyboxMethods.change_moneybox(
                moneybox_id, to_date, 2000, name, currency_id, None, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_change, 400)
        except AssertionError:
            raise AssertionError
        finally:
            PersonalTransactionMethods.create_personal_transaction(
                1000, 'name', 'Consumption', '2024-12-12',
                None, wallet_id, 136, None, access_token
            )
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)

    @allure.description('Редактирование чужой копилки')
    def test_14(self, create_moneybox_and_delete):

        """Создание копилки"""
        moneybox_id, access_token = create_moneybox_and_delete

        """Авторизация второго пользователя"""
        result_auth = AuthMethods.login('000011', AuthVariables.auth_payloads_3)
        Checking.check_statuscode(result_auth, 200)
        data = Checking.get_data(result_auth)
        access_token_2 = data['access_token']

        """Запрос на редактирование чужой копилки"""
        result_change = MoneyboxMethods.change_moneybox(
            moneybox_id, '2030-12-12', 1000, 'name_2', 2, None, access_token
        )
        print(result_change.status_code)
        print(result_change.text)
