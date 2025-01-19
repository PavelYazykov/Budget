import allure
from common_methods.variables import CommonVariables
from common_methods.http_methods import HttpMethods
import psycopg2


class UsersMethods:

    @staticmethod
    def connect_db(email, user_id):
        with allure.step('Подключение к БД, восстановление верификации email'):
            with psycopg2.connect(
                    host='82.97.248.83',
                    user='postgres',
                    password='postgres',
                    dbname='budget',
                    port=25432
            ) as connection:
                cursor = connection.cursor()
                cursor.execute(f"""UPDATE users SET email = '{email}' WHERE id = '{user_id}'""")
                connection.commit()
                cursor.execute(f"""UPDATE users SET is_email_verified = True, is_phone_verified = True
                 WHERE email = '{email}'""")
                connection.commit()

    @staticmethod
    def delete_users(users_id):
        with allure.step('Удаление пользователя из базы данных'):
            with psycopg2.connect(
                    host='82.97.248.83',
                    user='postgres',
                    password='postgres',
                    dbname='budget',
                    port=25432
            ) as connection:
                cursor = connection.cursor()
                cursor.execute(f"""DELETE FROM settings WHERE user_id = '{users_id}'""")
                connection.commit()
                cursor.execute(f"""DELETE FROM users WHERE id = '{users_id}'""")
                connection.commit()
                print(f'Пользователь с id: {users_id} удален')

    @staticmethod
    def get_user(access_token):
        with allure.step('Получение информации о текущем пользователе'):
            endpoint = '/users/me'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_user_without_auth():
        with allure.step('Получение информации о текущем пользователе без авторизации'):
            endpoint = '/users/me'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get_without_auth(get_url)
            return result

    @staticmethod
    def get_telegram_link(access_token):
        with allure.step('Получение ссылки на телеграм-бота, напоминающего пользователю о предстоящих платежах'):
            endpoint = '/users/get_telegram_link'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_telegram_link_without_access_token():
        with allure.step('Получение ссылки на телеграм-бота, без access_token'):
            endpoint = '/users/get_telegram_link'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get_without_auth(get_url)
            return result

    @staticmethod
    def change_user_info(email, last_name, first_name, middle_name, phone_number, date_of_birth, access_token):
        with allure.step('Изменение информации о текущем пользователе'):
            endpoint = '/users/me'
            body = {
                "email": email,
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "phone_number": phone_number,
                "date_of_birth": date_of_birth
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_user_info_without_phone(email, last_name, first_name, middle_name, date_of_birth, access_token):
        with allure.step('Изменение информации о текущем пользователе'):
            endpoint = '/users/me'
            body = {
                "email": email,
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "date_of_birth": date_of_birth
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_user_email(email, access_token):
        with allure.step('Изменение поля email'):
            endpoint = '/users/me'
            body = {
                "email": email
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_user_info_without_email(last_name, first_name, middle_name, phone_number, date_of_birth, access_token):
        with allure.step('Изменение информации о текущем пользователе без поля email'):
            endpoint = '/users/me'
            body = {
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "phone_number": phone_number,
                "date_of_birth": date_of_birth
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_user_info_without_email_phone(
            last_name, first_name, middle_name, date_of_birth, access_token
    ):
        with allure.step('Изменение информации о текущем пользователе без поля email, phone'):
            endpoint = '/users/me'
            body = {
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "date_of_birth": date_of_birth
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_user_info_without_email_phone_date_of_birth(
            last_name, first_name, middle_name, access_token
    ):
        with allure.step('Изменение информации о текущем пользователе без поля email, phone'):
            endpoint = '/users/me'
            body = {
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_user_info_without_email_phone_middlename(
            last_name, first_name, date_of_birth, access_token
    ):
        with allure.step('Изменение информации о текущем пользователе без поля email, phone, middlename'):
            endpoint = '/users/me'
            body = {
                "last_name": last_name,
                "first_name": first_name,
                "date_of_birth": date_of_birth
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_user_info_without_email_phone_lastname(
            first_name, middle_name, date_of_birth, access_token
    ):
        with allure.step('Изменение информации о текущем пользователе без поля email, phone, lastname'):
            endpoint = '/users/me'
            body = {
                "first_name": first_name,
                "middle_name": middle_name,
                "date_of_birth": date_of_birth
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_user_info_without_email_phone_firstname(
            last_name, middle_name, date_of_birth, access_token
    ):
        with allure.step('Изменение информации о текущем пользователе без поля email, phone, firstname'):
            endpoint = '/users/me'
            body = {
                "last_name": last_name,
                "middle_name": middle_name,
                "date_of_birth": date_of_birth
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def get_user_by_id(user_id, access_token):
        with allure.step('Получение информации о текущем пользователе по id'):
            endpoint = '/users/'
            user_id = user_id
            get_url = CommonVariables.base_url + endpoint + user_id
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def get_user_by_id_without_id(access_token):
        with allure.step('Получение информации о текущем пользователе по id  без поля id'):
            endpoint = '/users/'
            get_url = CommonVariables.base_url + endpoint
            result = HttpMethods.get(get_url, access_token)
            return result

    @staticmethod
    def change_user_info_by_id(
            email, last_name, first_name, middle_name, phone_number, date_of_birth, user_id, access_token
    ):
        with allure.step('Изменение информации о текущем пользователе по id'):
            endpoint = '/users/'
            user_id = user_id
            body = {
                "email": email,
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "phone_number": phone_number,
                "date_of_birth": date_of_birth
            }
            patch_url = CommonVariables.base_url + endpoint + user_id
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_user_info_by_id_without_phone(
            email, last_name, first_name, middle_name, date_of_birth, user_id, access_token
    ):
        with allure.step('Изменение информации о текущем пользователе по id'):
            endpoint = '/users/'
            user_id = user_id
            body = {
                "email": email,
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "date_of_birth": date_of_birth
            }
            patch_url = CommonVariables.base_url + endpoint + user_id
            print(patch_url)
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_user_info_by_id_without_email(
            last_name, first_name, middle_name, phone_number, date_of_birth, user_id, access_token
    ):
        with allure.step('Изменение информации о текущем пользователе по id'):
            endpoint = '/users/'
            user_id = user_id
            body = {
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "phone_number": phone_number,
                "date_of_birth": date_of_birth
            }
            patch_url = CommonVariables.base_url + endpoint + user_id
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_user_info_by_id_without_email_phone(
            last_name, first_name, middle_name, date_of_birth, user_id, access_token
    ):
        with allure.step('Изменение информации о текущем пользователе по id'):
            endpoint = '/users/'
            user_id = user_id
            body = {
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "date_of_birth": date_of_birth
            }
            patch_url = CommonVariables.base_url + endpoint + user_id
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_user_info_by_id_without_email_phone_date_of_birth(
            last_name, first_name, middle_name, user_id, access_token
    ):
        with allure.step('Изменение информации о текущем пользователе по id'):
            endpoint = '/users/'
            user_id = user_id
            body = {
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name
            }
            patch_url = CommonVariables.base_url + endpoint + user_id
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_user_info_by_id_without_email_phone_firstname(
            last_name, middle_name, date_of_birth, user_id, access_token
    ):
        with allure.step('Изменение информации о текущем пользователе по id'):
            endpoint = '/users/'
            user_id = user_id
            body = {
                "last_name": last_name,
                "middle_name": middle_name,
                "date_of_birth": date_of_birth
            }
            patch_url = CommonVariables.base_url + endpoint + user_id
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_user_info_by_id_without_email_phone_middlename(
            last_name, first_name, date_of_birth, user_id, access_token
    ):
        with allure.step('Изменение информации о текущем пользователе по id'):
            endpoint = '/users/'
            user_id = user_id
            body = {
                "last_name": last_name,
                "first_name": first_name,
                "date_of_birth": date_of_birth
            }
            patch_url = CommonVariables.base_url + endpoint + user_id
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_user_info_by_id_without_email_phone_lastname(
            first_name, middle_name, date_of_birth, user_id, access_token
    ):
        with allure.step('Изменение информации о текущем пользователе по id'):
            endpoint = '/users/'
            user_id = user_id
            body = {
                "first_name": first_name,
                "middle_name": middle_name,
                "date_of_birth": date_of_birth
            }
            patch_url = CommonVariables.base_url + endpoint + user_id
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def change_user_info_by_id_without_email_phone_user_id(
            last_name, first_name, middle_name, date_of_birth, access_token
    ):
        with allure.step('Изменение информации о текущем пользователе по id'):
            endpoint = '/users/'
            body = {
                "last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name,
                "date_of_birth": date_of_birth
            }
            patch_url = CommonVariables.base_url + endpoint
            result = HttpMethods.patch(patch_url, body, access_token)
            return result

    @staticmethod
    def delete_user(user_id, access_token):
        with allure.step('Удаление пользователя'):
            endpoint = '/users/'
            user_id = user_id
            delete_url = CommonVariables.base_url + endpoint + user_id
            result = HttpMethods.delete(delete_url, access_token)
            print(f'Пользователь с id: {user_id} удален')
            return result

    @staticmethod
    def delete_user_without_user_id(access_token):
        with allure.step('Удаление пользователя'):
            endpoint = '/users/'
            delete_url = CommonVariables.base_url + endpoint
            result = HttpMethods.delete(delete_url, access_token)
            return result

    @staticmethod
    def upload_file(name, path_to_file, access_token):
        post_url = 'https://budget-test.god-it.ru/users/upload_avatar'
        result = HttpMethods.post_download_files(post_url, name, path_to_file, access_token)
        return result

    @staticmethod
    def recover_user_info_if_bag(result, email, last_name, first_name, middle_name, phone,
                                 date_of_birth, access_token):
        if result.status_code == 200:
            UsersMethods.change_user_info(
                email, last_name, first_name, middle_name, phone, date_of_birth, access_token)
            UsersMethods.connect_db(email)

    @staticmethod
    def delete_avatar(access_token):
        endpoint = '/users/delete_avatar'
        delete_url = CommonVariables.base_url + endpoint
        print(delete_url)
        result = HttpMethods.post_without_body(delete_url, access_token)
        return result

    @staticmethod
    def get_user_id(access_token):
        result_get = UsersMethods.get_user(access_token)
        data = result_get.json()
        user_id = data.get('id')
        print(user_id)
        return user_id




