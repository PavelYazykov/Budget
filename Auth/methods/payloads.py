import json

import allure


class Payloads:
    auth_data = 'username=y.pawel_test1@mail.ru&password=Ohranatruda@1'

    required_fields_login = {
        "access_token": "string",
        "refresh_token": "string",
        "token_type": "string"
    }

    @staticmethod
    def required_fields():
        required_fields = {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "email": "user@example.com",
            "is_active": True,
            "is_email_verified": False,
            "is_phone_verified": False,
            "last_name": "Иванов",
            "first_name": "Иван",
            "middle_name": "Иванович",
            "phone_number": "88005555535",
            "date_of_birth": "2024-10-09",
            "avatar": "string"
        }
        return required_fields

    @staticmethod
    def required_fields_value(email, last_name, first_name, middle_name, phone, date_of_birth, data):
        required_fields_values = {
            "email": email,
            "last_name": last_name,
            "first_name": first_name,
            "middle_name": middle_name,
            "phone_number": phone,
            "date_of_birth": date_of_birth
        }
        for field, exp in required_fields_values.items():
            assert field in data, f'отсутствует обязательное поле {field}'
            assert data[field] == exp, f'неверное значение {data[field]} ожидалось: {exp}'
            print(field, exp)

    @staticmethod
    def check_required_fields(result, required_fields):
        with allure.step('Проверка наличия обязательныхп полей'):
            result_text = result.text
            data = json.loads(result_text)
            for field in required_fields:
                assert field in data, f'отсутствует обязательное поле {field}'
            print('Все поля присутствуют')
