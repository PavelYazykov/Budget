
class Payloads:
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
        for field, value in required_fields_values.items():
            assert field, value in data
