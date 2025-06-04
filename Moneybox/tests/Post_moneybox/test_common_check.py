import time
import allure
import pytest

from Moneybox.methods.payloads import Payloads
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from common_methods.checking import Checking
from common_methods.variables import MoneyboxVariables
from Personal_transaction.methods.personal_transaction_methods import PersonalTransactionMethods
to_date = MoneyboxVariables.to_date
goal = MoneyboxVariables.goal
name = MoneyboxVariables.name
currency_id = MoneyboxVariables.currency_id
amount = MoneyboxVariables.amount


@pytest.mark.post_moneybox
@allure.epic('Post_moneybox /api/v1/moneybox/ Создание копилок общие проверки')
class TestPostMoneyboxCommon:

    @allure.description('Создание новой копилки с валидными значениями (авторизованный пользователь)')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, name, currency_id, amount, access_token
        )
        moneybox_id = MoneyboxMethods.get_moneybox_id(post_result)
        wallet_id = MoneyboxMethods.get_wallet_id(post_result)
        try:
            """Проверка статус кода"""
            Checking.check_statuscode(post_result, 201)

            """Проверка наличия обязательных полей"""
            MoneyboxMethods.post_check_exist_req_fields(post_result, Payloads.required_fields())
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            """Удаление копилки"""
            with allure.step('Удаление копилки'):
                MoneyboxMethods.delete_moneybox_from_bd(moneybox_id, wallet_id)

    @allure.description('Создание новой копилки со значением goal меньше amount')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, 1000, name, currency_id, 2000, access_token
        )

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 400)

    @allure.description('Создание новой копилки с валидными значениями (неавторизованный пользователь)')
    def test_03(self):
        """Запрос на создание копилки"""
        post_result = MoneyboxMethods.create_moneybox_without_auth(to_date, goal, name, currency_id, amount)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 401)

    @allure.description('Создание новой копилки без body')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Post_moneybox запрос"""
        post_result = MoneyboxMethods.create_moneybox_without_body(access_token)

        """Проверка статус кода"""
        Checking.delete_moneybox_if_bug(post_result, 201, access_token)
        Checking.check_statuscode(post_result, 422)

    @allure.description('Автоматическое архивирование после достижения цели и выводе средств')
    def test_05(self, auth_fixture):
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
                None, wallet_id, 30, None, access_token
            )
            Checking.check_statuscode(result_income, 201)
            time.sleep(5)

            """Списание средств с копилки"""
            result_consumption = PersonalTransactionMethods.create_personal_transaction(
                1000, 'name', 'Consumption', '2024-12-12',
                None, wallet_id, 20, None, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_consumption, 201)

            """Проверка значения поля is_archived"""
            result_get = MoneyboxMethods.get_one_moneybox(moneybox_id, access_token)
            Checking.check_statuscode(result_get, 200)
            data = Checking.get_data(result_get)
            assert data['data']['wallet']['is_archived'] is True
        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                # Подробное описание ошибки
                allure.attach(str(e), attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e
        finally:
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id, wallet_id)
    #
    # @allure.description('Создание новой копилки с валидными значениями (авторизованный пользователь)')  # DELETE
    # def test_06(self, auth_fixture):
    #     steps = ['Создание новой копилки с валидными значениями (авторизованный пользователь)']
    #     moneybox_id = None
    #
    #     try:
    #         steps.append("Авторизация пользователя")
    #         access_token = auth_fixture
    #
    #         steps.append("Отправка post_moneybox запроса")
    #         post_result = MoneyboxMethods.create_moneybox(
    #             to_date, goal, name, currency_id, amount, access_token
    #         )
    #
    #         steps.append("Получение ID копилки")
    #         moneybox_id = MoneyboxMethods.get_moneybox_id(post_result)
    #
    #         steps.append("Проверка статус кода")
    #         Checking.check_statuscode(post_result, 201)
    #
    #         steps.append("Проверка обязательных полей")
    #         MoneyboxMethods.post_check_exist_req_fields(post_result, Payloads.required_fields())
    #
    #     except AssertionError as e:
    #         steps.append(f"Ошибка: {e}")
    #         step_log_text = "\n".join(steps)
    #         with allure.step(f'Ошибка проверки: {e}'):
    #             # Сохраняем все шаги в текстовый файл
    #             with open("manual_step_log.txt", "w", encoding="utf-8") as f:
    #                 f.write(step_log_text)
    #             # Прикрепляем файл к Allure-отчёту
    #             allure.attach.file("manual_step_log.txt", name="Шаги до ошибки",
    #                                attachment_type=allure.attachment_type.TEXT)
    #             raise AssertionError from e
    #     finally:
    #         MoneyboxMethods.delete_moneybox_from_bd(moneybox_id)

    @allure.description('Создание новой копилки с валидными значениями (авторизованный пользователь)')
    def test_06(self, auth_fixture):
        test_description = 'Создание новой копилки с валидными значениями (авторизованный пользователь)'
        expected_result = ('Копилка успешно создается, возвращается статус код 201,'
                           'все обязательные поля присутствуют в ответе')
        steps_log = []
        moneybox_id = None
        wallet_id = None

        try:
            # Авторизация
            steps_log.append('Авторизация пользователя')
            access_token = auth_fixture

            # Post_moneybox запрос
            steps_log.append('Создание копилки через POST-запрос')
            post_result = MoneyboxMethods.create_moneybox(
                to_date, goal, name, currency_id, amount, access_token
            )

            moneybox_id = MoneyboxMethods.get_moneybox_id(post_result)
            wallet_id = MoneyboxMethods.get_wallet_id(post_result)

            # Проверка статус кода
            steps_log.append('Проверка, что статус код == 201')
            Checking.check_statuscode(post_result, 201)

            # Проверка обязательных полей
            steps_log.append('Проверка наличия обязательных полей в теле ответа')
            MoneyboxMethods.post_check_exist_req_fields(post_result, Payloads.required_fields())

        except AssertionError as e:
            with allure.step(f'Ошибка проверки: {e}'):
                detailed_log = (
                        f"Описание теста: {test_description}\n"
                        f"\nВыполненные шаги до ошибки:\n"
                        + "\n".join(f"- {step}" for step in steps_log) +
                        f"\n\nОшибка:\n{str(e)}\n"
                        f"\nОжидаемый результат: {expected_result}\n\n"
                )
                allure.attach(detailed_log, name="Подробности ошибки", attachment_type=allure.attachment_type.TEXT)
                raise AssertionError from e

        finally:
            with allure.step('Удаление копилки'):
                MoneyboxMethods.delete_moneybox_from_bd(moneybox_id, wallet_id)

    @allure.description('Изменение цели в просроченной копилке')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Создание копилки"""
        create_result = MoneyboxMethods.create_moneybox(
            '2030-12-12', 1000, 'Pavel_moneybox', 2, 0, access_token
        )
        Checking.check_statuscode(create_result, 201)
        moneybox_id = MoneyboxMethods.get_moneybox_id(create_result)
        wallet_id = MoneyboxMethods.get_wallet_id(create_result)
        try:
            """Изменение даты копилки на Истекшую"""
            MoneyboxMethods.create_expire_moneybox(moneybox_id)

            """Изменение цели в копилке"""
            patch_result = MoneyboxMethods.change_moneybox(
                moneybox_id, '2030-12-12', 2000, 'Pavel_moneybox', 2, False,
                access_token
            )
            """Проверка статус кода"""
            Checking.check_statuscode(patch_result, 422)
        finally:
            MoneyboxMethods.delete_moneybox_from_bd(moneybox_id, wallet_id)










