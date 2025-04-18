import json
import allure
import psycopg2
from common_methods.variables import CommonVariables
from common_methods.http_methods import HttpMethods
from common_methods.variables import DataBase
import requests

base_url = CommonVariables.base_url


class AuthMethods:

    @staticmethod
    def connect_db():
        with allure.step('Подключение к БД'):
            with psycopg2.connect(
                    host=DataBase.host,
                    user=DataBase.user,
                    password=DataBase.password,
                    dbname=DataBase.dbname,
                    port=DataBase.port
            ) as connection:
                cursor = connection.cursor()
                return cursor

    @staticmethod
    def connect_db_check_user(user_id, last_name, first_name, middle_name, phone, email, date_of_birth):
        with allure.step('Подключение к БД Проверка полей и значений'):
            with psycopg2.connect(
                    host=DataBase.host,
                    user=DataBase.user,
                    password=DataBase.password,
                    dbname=DataBase.dbname,
                    port=DataBase.port
            ) as connection:
                cursor = connection.cursor()
                cursor.execute(f"""SELECT * FROM users WHERE id= '{user_id}'""")
                result_db = cursor.fetchone()
                print(result_db)
                assert result_db[1] == last_name, f'Неверное значение в поле last_name'
                assert result_db[2] == first_name, f'Неверное значение в поле first_name'
                assert result_db[3] == middle_name, f'Неверное значение в поле middle_name'
                assert result_db[5] == phone, f'Неверное значение в поле phone'
                assert result_db[6] == email, f'Неверное значение в поле email'
                assert str(result_db[7]) == date_of_birth, f'Неверное значение в поле date_of_birth'

    @staticmethod
    def delete_user(users_id):
        with allure.step('Удаление пользователя из базы данных'):
            with psycopg2.connect(
                host=DataBase.host,
                user=DataBase.user,
                password=DataBase.password,
                dbname=DataBase.dbname,
                port=DataBase.port
            ) as connection:
                cursor = connection.cursor()
                cursor.execute(f"""DELETE FROM settings WHERE user_id = '{users_id}'""")
                connection.commit()
                cursor.execute(f"""DELETE FROM users WHERE id = '{users_id}'""")
                connection.commit()
                print(f'Пользователь с id: {users_id} удален')

    @staticmethod
    def verification_user(user_id):
        with allure.step('Верификация пользоваетля'):
            with psycopg2.connect(
                    host=DataBase.host,
                    user=DataBase.user,
                    password=DataBase.password,
                    dbname=DataBase.dbname,
                    port=DataBase.port
            ) as connection:
                cursor = connection.cursor()
                cursor.execute(f"""UPDATE users SET is_active=True, is_email_verified=True, is_phone_verified=True
                    WHERE id='{user_id}'""")
                connection.commit()

    @staticmethod
    def check_required_fields(result, required_fields):
        with allure.step('Проверка наличия всех полей'):
            result_text = result.text
            data = json.loads(result_text)
            user_id = data['id']
            required_fields = required_fields
            for field in required_fields:
                assert field in data, f'отсутствует обязательное поле {field}'
                print(f'Обязательное поле {field} присутствует')

    @staticmethod
    def get_id(result):
        """Получение user id, data """
        result_text = result.text
        data = json.loads(result_text)
        user_id = data['id']
        print(f'User id: {user_id}')
        return data, user_id

    @staticmethod
    def registration(email, password, last_name, first_name, middle_name, phone, date_of_birth):
        with allure.step('Регистрация пользователя'):
            post_resource = '/auth/register'
            post_url = CommonVariables.base_url + post_resource
            body = {
                "email": email,
                "password": password,
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "phone_number": phone,
                "date_of_birth": date_of_birth
            }
            result = HttpMethods.post_without_auth(post_url, body)
            return result

    @staticmethod
    def registration_without_body():
        with allure.step('Регистрация пользователя без тела запроса'):
            post_resource = '/auth/register'
            post_url = CommonVariables.base_url + post_resource
            result = requests.post(post_url)
            return result

    @staticmethod
    def login(device_id, payload):
        with allure.step('Авторизация'):
            post_resource = '/auth/jwt/login'
            device_id = '?device_id=' + str(device_id)
            post_url = CommonVariables.base_url + post_resource + device_id
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
            }
            body = payload
            result = requests.post(post_url, headers=headers, data=body)
            return result

    @staticmethod
    def login_without_device_id(payload):
        with allure.step('Авторизация без device_id'):
            post_resource = '/auth/jwt/login'
            post_url = CommonVariables.base_url + post_resource
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
            }
            body = payload
            result = requests.post(post_url, headers=headers, data=body)
            return result

    @staticmethod
    def refresh(refresh_token, payload):
        with allure.step('Обновление access_token и refresh_token'):
            post_resource = '/auth/jwt/refresh'
            post_url = CommonVariables.base_url + post_resource
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": f"Bearer {refresh_token}"
            }
            body = payload
            result = requests.post(post_url, headers=headers, data=body)
            return result

    @staticmethod
    def refresh_without_refresh(payload):
        with allure.step('Обновление access_token и refresh_token'):
            post_resource = '/auth/jwt/refresh'
            post_url = CommonVariables.base_url + post_resource
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": "Bearer"
            }
            body = payload
            result = requests.post(post_url, headers=headers, data=body)
            return result

    @staticmethod
    def logout(refresh_token, payload):
        with allure.step('Отзыв refresh_token'):
            post_resource = '/auth/jwt/logout'
            post_url = CommonVariables.base_url + post_resource
            headers = {
                "Content-type": "application/x-www-form-urlencoded",
                "Authorization": f"Bearer {refresh_token}"
            }
            body = payload
            result = requests.post(post_url, headers=headers, data=body)
            return result

    @staticmethod
    def request_verify_code(user_id):
        with allure.step('Создание кода для верификации'):
            post_resource = '/auth/request-verify-code'
            user_id = '?user_id=' + user_id
            post_url = CommonVariables.base_url + post_resource + user_id
            print(post_url)
            result = requests.post(post_url)
            return result

    @staticmethod
    def request_verify_code_without_userid():
        with allure.step('Создание кода для верификации без указания user_id'):
            post_resource = '/auth/request-verify-code'
            post_url = CommonVariables.base_url + post_resource
            print(post_url)
            result = requests.post(post_url)
            return result

    @staticmethod
    def verify(user_id, code_from_user):
        with allure.step('Верификация по коду'):
            post_resource = '/auth/verify'
            user_id = '?user_id=' + user_id
            code_from_user = '&code_from_user=' + code_from_user
            post_url = CommonVariables.base_url + post_resource + user_id + code_from_user
            print(post_url)
            result = requests.post(post_url)
            return result

    @staticmethod
    def verify_without_userid(code_from_user):
        with allure.step('Верификация по коду без поля user_id'):
            post_resource = '/auth/verify'
            code_from_user = '&code_from_user=' + code_from_user
            post_url = CommonVariables.base_url + post_resource + code_from_user
            print(post_url)
            result = requests.post(post_url)
            return result

    @staticmethod
    def verify_without_code(user_id):
        with allure.step('Верификация по коду без code_from_user'):
            post_resource = '/auth/verify'
            user_id = '?user_id=' + user_id
            post_url = CommonVariables.base_url + post_resource + user_id
            print(post_url)
            result = requests.post(post_url)
            return result

    @staticmethod
    def change_password(old_password, new_password, access_token):
        with allure.step('Изменение пароля пользователя'):
            post_resource = '/auth/change_password'
            post_url = CommonVariables.base_url + post_resource
            body = {
                "old_password": old_password,
                "new_password": new_password
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def change_password_without_old_password(new_password, access_token):
        with allure.step('Изменение пароля пользователя без старого парполя'):
            post_resource = '/auth/change_password'
            post_url = CommonVariables.base_url + post_resource
            body = {
                "new_password": new_password
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def change_password_without_new_password(old_password, access_token):
        with allure.step('Изменение пароля пользователя без нового пароля'):
            post_resource = '/auth/change_password'
            post_url = CommonVariables.base_url + post_resource
            body = {
                "old_password": old_password
            }
            result = HttpMethods.post(post_url, body, access_token)
            return result

    @staticmethod
    def forgot_password(email):
        with allure.step('Запрос одноразового кода для смены пароля'):
            post_resource = '/auth/forgot-password'
            post_url = CommonVariables.base_url + post_resource
            body = {
                "email": email
            }
            result = HttpMethods.post_without_auth(post_url, body)
            return result

    @staticmethod
    def forgot_password_without_body():
        with allure.step('Запрос одноразового кода для смены пароля (без body)'):
            post_resource = '/auth/forgot-password'
            post_url = CommonVariables.base_url + post_resource
            headers = {"Content-type": "application/json"}
            result = requests.post(post_url, headers=headers)
            return result

    @staticmethod
    def code_check(email, code):
        with allure.step('Проверка кода на смену забытого пароля'):
            post_resource = '/auth/code-check'
            post_url = CommonVariables.base_url + post_resource
            body = {
                "email": email,
                "code": code
            }
            result = HttpMethods.post_without_auth(post_url, body)
            return result

    @staticmethod
    def code_check_without_code(email):
        with allure.step('Проверка кода на смену забытого пароля без поля code'):
            post_resource = '/auth/code-check'
            post_url = CommonVariables.base_url + post_resource
            body = {
                "email": email
            }
            result = HttpMethods.post_without_auth(post_url, body)
            return result

    @staticmethod
    def code_check_without_email(code):
        with allure.step('Проверка кода на смену забытого пароля без поля email'):
            post_resource = '/auth/code-check'
            post_url = CommonVariables.base_url + post_resource
            body = {
                "code": code
            }
            result = HttpMethods.post_without_auth(post_url, body)
            return result

    @staticmethod
    def reset_password(email, new_password):
        with allure.step('Изменение пароля'):
            post_resource = '/auth/reset-password'
            post_url = CommonVariables.base_url + post_resource
            body = {
                "email": email,
                "new_password": new_password
            }
            result = HttpMethods.post_without_auth(post_url, body)
            return result

    @staticmethod
    def reset_password_without_email(new_password):
        with allure.step('Изменение пароля без роля email'):
            post_resource = '/auth/reset-password'
            post_url = CommonVariables.base_url + post_resource
            body = {
                "new_password": new_password
            }
            result = HttpMethods.post_without_auth(post_url, body)
            return result

    @staticmethod
    def reset_password_without_body():
        with allure.step('Изменение пароля без body'):
            post_resource = '/auth/reset-password'
            post_url = CommonVariables.base_url + post_resource
            result = requests.post(post_url)
            return result

    @staticmethod
    def reset_password_without_password(email):
        with allure.step('Изменение пароля'):
            post_resource = '/auth/reset-password'
            post_url = CommonVariables.base_url + post_resource
            body = {
                "email": email
            }
            result = HttpMethods.post_without_auth(post_url, body)
            return result

    @staticmethod
    def get_refresh_token(result):
        with allure.step('Получение refresh_token'):
            check = result.json()
            refresh_token = check.get('refresh_token')
            return refresh_token

    @staticmethod
    def get_verify_code(result):
        with allure.step('Получение кода'):
            check = result.json()
            data = check['message']
            code = data[-6:]
            print(f'Code: {code}')
            return code

    @staticmethod
    def change_password_back(result, old_password, new_password, access_token):
        with allure.step('Восстановление предыдущего пароля'):
            result_code = result.status_code
            if result_code == 200:
                result_change = AuthMethods.change_password(old_password, new_password, access_token)
                assert result_change.status_code == 200
                print('Предыдущий пароль восстановлен')

