import requests
data = {
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


required_fields_values = {
    "email": "user@example.com",
    "last_name": "Иванов",
    "first_name": "Иван",
    "middle_name": 'middle_name',
    "phone_number": "88005555535",
    "date_of_birth": "2024-10-09"
}
for field, exp in required_fields_values.items():
    assert field in data, f'отсутствует обязательное поле {field}'
    assert data[field] == exp, f'неверное значение {data[field]} ожидалось: {exp}'
    print(field, exp)
