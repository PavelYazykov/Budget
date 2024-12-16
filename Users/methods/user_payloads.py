import json


class UserResponse:

    @staticmethod
    def check_required_fields(result):
        result_text = result.text
        data = json.loads(result_text)
        print(data)
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
            "date_of_birth": "2024-11-11",
            "avatar": "string"
        }

        for field in required_fields:
            assert field in data, f'поле {field} отсутствует'
        print('Все поля присутствуют')

    @staticmethod
    def check_required_fields_value(
            result, email, last_name, first_name, middle_name, phone_number, date_of_birth
    ):
        result_text = result.text
        data = json.loads(result_text)
        required_fields = {
            "email": email,
            "last_name": last_name,
            "first_name": first_name,
            "middle_name": middle_name,
            "phone_number": phone_number,
            "date_of_birth": date_of_birth,
        }

        for field, value in required_fields.items():
            assert data[field] == value

