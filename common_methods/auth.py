import allure
import requests


class Auth:
    """Авторизация пользователя"""
    @staticmethod
    def auth():
        with allure.step('Авторизация'):
            # base_url = 'https://budget-test.god-it.ru/api/auth/jwt/login'
            base_url = 'http://localhost:8000/auth/jwt/login'
            device_id = '?device_id=11111'
            auth_url = base_url + device_id
            body = 'username=y.pawel_test1%40mail.ru&password=Ohranatruda%401'
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }

            post_response = requests.post(auth_url, headers=headers, data=body)
            return post_response

    @staticmethod
    def auth_2():
        with allure.step('Авторизация'):
            # base_url = 'https://budget-test.god-it.ru/api/auth/jwt/login'
            base_url = 'http://localhost:8000/auth/jwt/login'
            device_id = '?device_id=11111'
            auth_url = base_url + device_id
            body = 'username=bmk20283%40nowni.com&password=Ohranatruda%402'
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }

            post_response = requests.post(auth_url, headers=headers, data=body)
            return post_response

