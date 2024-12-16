import json


class Payloads:

    @staticmethod
    def required_fields():
        required_fields = {
            "data": {
                "to_date": "2024-12-30",
                "goal": "1000.00",
                "wallet": {
                    "name": "My Goal_2",
                    "currency_id": 2,
                    "amount": "0"
                }
            }
        }
        return required_fields

    @staticmethod
    def post_required_fields_value(email, last_name, first_name, middle_name, phone, date_of_birth, data):
        required_fields_values = {
            "email": email,
            "last_name": last_name,
            "first_name": first_name,
            "middle_name": middle_name,
            "phone_number": phone,
            "date_of_birth": date_of_birth
        }
        for field, value in required_fields_values.items():
            assert field in data, f'отсутствует обязательное поле {field}'
            assert data[field] == value, f'неверное значение {data[field]} ожидалось: {value}'
            print(field, value)

