import allure
import psycopg2

from common_methods.http_methods import HttpMethods
from common_methods.variables import CommonVariables, DataBase
from common_methods.checking import Checking


class PersonalBudgetMethods:

    @staticmethod
    def create_personal_budget(
            transaction_type, category_id, subcategory_id, amount, month, year, date_reminder, title, have_to_remind,
            remind_in_days, access_token
    ):
        with allure.step('Создание единоразового объекта персонального бюджета'):
            endpoint = '/api/v1/personal_budget/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "year": year,
                "regular_outcome": {
                    "date_reminder": date_reminder,
                    "title": title,
                    "have_to_remind": have_to_remind,
                    "remind_in_days": remind_in_days
                }
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_without_remind_in_days(
            transaction_type, category_id, subcategory_id, amount, month, year, date_reminder, title, have_to_remind,
            access_token
    ):
        with allure.step('Создание единоразового объекта персонального бюджета без поля remind_in_days'):
            endpoint = '/api/v1/personal_budget/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "year": year,
                "regular_outcome": {
                    "date_reminder": date_reminder,
                    "title": title,
                    "have_to_remind": have_to_remind
                }
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_without_have_to_remind(
            transaction_type, category_id, subcategory_id, amount, month, year, date_reminder, title,
            remind_in_days, access_token
    ):
        with allure.step('Создание единоразового объекта персонального бюджета без поля have_to_remind'):
            endpoint = '/api/v1/personal_budget/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "year": year,
                "regular_outcome": {
                    "date_reminder": date_reminder,
                    "title": title,
                    "remind_in_days": remind_in_days
                }
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_without_title(
            transaction_type, category_id, subcategory_id, amount, month, year, date_reminder, have_to_remind,
            remind_in_days, access_token
    ):
        with allure.step('Создание единоразового объекта персонального бюджета без поля title'):
            endpoint = '/api/v1/personal_budget/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "year": year,
                "regular_outcome": {
                    "date_reminder": date_reminder,
                    "have_to_remind": have_to_remind,
                    "remind_in_days": remind_in_days
                }
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_without_date_reminder(
            transaction_type, category_id, subcategory_id, amount, month, year, title, have_to_remind,
            remind_in_days, access_token
    ):
        with allure.step('Создание единоразового объекта персонального бюджета без поля date_reminder'):
            endpoint = '/api/v1/personal_budget/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "year": year,
                "regular_outcome": {
                    "title": title,
                    "have_to_remind": have_to_remind,
                    "remind_in_days": remind_in_days
                }
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_without_year(
            transaction_type, category_id, subcategory_id, amount, month, date_reminder, title, have_to_remind,
            remind_in_days, access_token
    ):
        with allure.step('Создание единоразового объекта персонального бюджета без поля year'):
            endpoint = '/api/v1/personal_budget/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "regular_outcome": {
                    "date_reminder": date_reminder,
                    "title": title,
                    "have_to_remind": have_to_remind,
                    "remind_in_days": remind_in_days
                }
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_without_month(
            transaction_type, category_id, subcategory_id, amount, year, date_reminder, title, have_to_remind,
            remind_in_days, access_token
    ):
        with allure.step('Создание единоразового объекта персонального бюджета без поля month'):
            endpoint = '/api/v1/personal_budget/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "year": year,
                "regular_outcome": {
                    "date_reminder": date_reminder,
                    "title": title,
                    "have_to_remind": have_to_remind,
                    "remind_in_days": remind_in_days
                }
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_with_amount(
            transaction_type, category_id, subcategory_id, month, year, date_reminder, title, have_to_remind,
            remind_in_days, access_token
    ):
        with allure.step('Создание единоразового объекта персонального бюджета'):
            endpoint = '/api/v1/personal_budget/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "month": month,
                "year": year,
                "regular_outcome": {
                    "date_reminder": date_reminder,
                    "title": title,
                    "have_to_remind": have_to_remind,
                    "remind_in_days": remind_in_days
                }
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_without_subcategory(
            transaction_type, category_id, amount, month, year, date_reminder, title, have_to_remind,
            remind_in_days, access_token
    ):
        with allure.step('Создание единоразового объекта персонального бюджета без поля subcategory_id'):
            endpoint = '/api/v1/personal_budget/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "amount": amount,
                "month": month,
                "year": year,
                "regular_outcome": {
                    "date_reminder": date_reminder,
                    "title": title,
                    "have_to_remind": have_to_remind,
                    "remind_in_days": remind_in_days
                }
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_without_category_id(
            transaction_type, subcategory_id, amount, month, year, date_reminder, title, have_to_remind,
            remind_in_days, access_token
    ):
        with allure.step('Создание единоразового объекта персонального бюджета'):
            endpoint = '/api/v1/personal_budget/'
            body = {
                "transaction_type": transaction_type,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "year": year,
                "regular_outcome": {
                    "date_reminder": date_reminder,
                    "title": title,
                    "have_to_remind": have_to_remind,
                    "remind_in_days": remind_in_days
                }
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_without_transaction_type(
            category_id, subcategory_id, amount, month, year, date_reminder, title, have_to_remind,
            remind_in_days, access_token
    ):
        with allure.step('Создание единоразового объекта персонального бюджета без поля transaction_type'):
            endpoint = '/api/v1/personal_budget/'
            body = {
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "year": year,
                "regular_outcome": {
                    "date_reminder": date_reminder,
                    "title": title,
                    "have_to_remind": have_to_remind,
                    "remind_in_days": remind_in_days
                }
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_without_body(access_token):
        with allure.step('Создание единоразового объекта персонального бюджета'):
            endpoint = '/api/v1/personal_budget/'
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post_without_body(post_url, access_token)
            return result

    @staticmethod
    def create_personal_budget_without_auth(
            transaction_type, category_id, subcategory_id, amount, month, year, date_reminder, title, have_to_remind,
            remind_in_days
    ):
        with allure.step('Создание единоразового объекта персонального бюджета'):
            endpoint = '/api/v1/personal_budget/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "year": year,
                "regular_outcome": {
                    "date_reminder": date_reminder,
                    "title": title,
                    "have_to_remind": have_to_remind,
                    "remind_in_days": remind_in_days
                }
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post_without_auth(post_url, body)
            return result

    @staticmethod
    def create_personal_budget_and_regular_outcome_null(
            transaction_type, category_id, subcategory_id, amount, month, year, access_token):
        with allure.step('Создание единоразового объекта персонального бюджета, regular_outcome = null '):
            endpoint = '/api/v1/personal_budget/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "year": year,
                "regular_outcome": None
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def create_personal_budget_without_regular_outcome(
            transaction_type, category_id, subcategory_id, amount, month, year, access_token):
        with allure.step('Создание единоразового объекта персонального бюджета, без поля regular_outcome '):
            endpoint = '/api/v1/personal_budget/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "year": year
            }
            post_url = CommonVariables.base_url + endpoint
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def get_personal_budget(access_token):
        with allure.step('Получение всех единоразовых объектов объектов бюджета'):
            endpoint = '/api/v1/personal_budget/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_personal_budget_with_params(payloads, access_token):
        with allure.step('Получение всех единоразовых объектов объектов бюджета с параметрами'):
            endpoint = '/api/v1/personal_budget/'
            payload = payloads
            get_url = CommonVariables.base_url + endpoint + payload
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_personal_budget_by_id(personal_budget_id, access_token):
        with allure.step('Получение единоразового объекта бюджета по id'):
            endpoint = f'/api/v1/personal_budget/{personal_budget_id}/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def change_personal_budget(
            personal_budget_id, transaction_type, category_id, subcategory_id, amount, month, year, access_token
    ):
        with allure.step('Редактирование данных единоразового объекта персонального бюджета'):
            endpoint = f'/api/v1/personal_budget/{personal_budget_id}/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "year": year
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_personal_budget_without_year(
            personal_budget_id, transaction_type, category_id, subcategory_id, amount, month, access_token
    ):
        with allure.step('Редактирование данных единоразового объекта персонального бюджета без поля year'):
            endpoint = f'/api/v1/personal_budget/{personal_budget_id}/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_personal_budget_without_month(
            personal_budget_id, transaction_type, category_id, subcategory_id, amount, year, access_token
    ):
        with allure.step('Редактирование данных единоразового объекта персонального бюджета без поля month'):
            endpoint = f'/api/v1/personal_budget/{personal_budget_id}/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "year": year
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_personal_budget_without_amount(
            personal_budget_id, transaction_type, category_id, subcategory_id, month, year, access_token
    ):
        with allure.step('Редактирование данных единоразового объекта персонального бюджета без поля amount'):
            endpoint = f'/api/v1/personal_budget/{personal_budget_id}/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "month": month,
                "year": year
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_personal_budget_without_subcategory(
            personal_budget_id, transaction_type, category_id, amount, month, year, access_token
    ):
        with allure.step('Редактирование данных единоразового объекта персонального бюджета без поля'):
            endpoint = f'/api/v1/personal_budget/{personal_budget_id}/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "amount": amount,
                "month": month,
                "year": year
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_personal_budget_without_category_id(
            personal_budget_id, transaction_type, subcategory_id, amount, month, year, access_token
    ):
        with allure.step('Редактирование данных единоразового объекта персонального бюджета без поля category_id'):
            endpoint = f'/api/v1/personal_budget/{personal_budget_id}/'
            body = {
                "transaction_type": transaction_type,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "year": year
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_personal_budget_without_transaction_type(
            personal_budget_id, category_id, subcategory_id, amount, month, year, access_token
    ):
        with allure.step('Редактирование данных единоразового объекта персонального бюджета без поля transaction_type'):
            endpoint = f'/api/v1/personal_budget/{personal_budget_id}/'
            body = {
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "year": year
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_personal_budget_without_body(
            personal_budget_id, access_token
    ):
        with allure.step('Редактирование данных единоразового объекта персонального бюджета без body'):
            endpoint = f'/api/v1/personal_budget/{personal_budget_id}/'
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch_without_body(patch_url, access_token)
            return result

    @staticmethod
    def delete_personal_budget(personal_budget_id, access_token):
        with allure.step('Удаление единоразового объекта персонального бюджета'):
            endpoint = f'/api/v1/personal_budget/{personal_budget_id}/'
            delete_url = CommonVariables.base_url + endpoint
            result = HttpMethods.delete(delete_url, access_token)
            return result

    @staticmethod
    def delete_personal_budget_without_budget_id(access_token):
        with allure.step('Удаление единоразового объекта персонального бюджета без personal_budget_id'):
            endpoint = f'/api/v1/personal_budget/'
            delete_url = CommonVariables.base_url + endpoint
            result = HttpMethods.delete(delete_url, access_token)
            return result

    @staticmethod
    def patch_personal_budget_auto_use(
            personal_budget_id, transaction_type, category_id, subcategory_id, amount, month, year, access_token
    ):
        with allure.step('Редактирование данных единоразового и регулярного объекта персонального бюджета'):
            endpoint = f'/api/v1/personal_budget/auto_use/{personal_budget_id}/'
            body = {
                "transaction_type": transaction_type,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "amount": amount,
                "month": month,
                "year": year
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def delete_personal_budget_if_bug(result, status_code, access_token):
        with allure.step('Баг. Удаление персонального бюджета'):
            if result.status_code == status_code:
                data = Checking.get_data(result)
                personal_budget_id = data['data']['id']
                PersonalBudgetMethods.delete_personal_budget(personal_budget_id, access_token)
                print(f'Ошибка, статус код: {result.status_code}')
                raise AssertionError

    @staticmethod
    def create_pb_and_pb_auto_use(category_id, user_id, transaction_type, month, year, subcategory_id,
                                  personal_budget_auto_use_id, personal_budget_id, amount, date_reminder):
        with psycopg2.connect(
                host=DataBase.host,
                user=DataBase.user,
                password=DataBase.password,
                dbname=DataBase.dbname,
                port=DataBase.port
        ) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""INSERT INTO personal_budgets_auto_use(category_id, user_id, transaction_type,
                subcategory_id, date_reminder, id, amount)
                VALUES(%s, %s, %s, %s, %s, %s, %s);""", (category_id, user_id, transaction_type, subcategory_id,
                                                         date_reminder, personal_budget_auto_use_id, amount))
            connection.commit()
            cursor.execute(f"""INSERT INTO personal_budgets(category_id, user_id, transaction_type, month, year,
                subcategory_id, personal_budgets_auto_use_id, id, amount)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);""", (category_id, user_id, transaction_type, month, year,
                                                                 subcategory_id, personal_budget_auto_use_id,
                                                                 personal_budget_id, amount))
            connection.commit()


