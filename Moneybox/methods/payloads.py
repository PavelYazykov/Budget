import json


class Payloads:

    get_response = {
      "meta": {},
      "data": [
        {
          "to_date": "2025-06-15",
          "goal": 100.55,
          "id": 1,
          "wallet": {
            "name": "Title or description",
            "currency_id": 1,
            "id": 1,
            "goal_is_achieved": True,
            "amount": 100.55,
            "is_archived": True
          }
        }
      ]
    }

    get_by_id_response = {
      "meta": {},
      "data":
        {
          "to_date": "2025-06-15",
          "goal": 100.55,
          "id": 1,
          "wallet": {
            "name": "Title or description",
            "currency_id": 1,
            "id": 1,
            "goal_is_achieved": True,
            "amount": 100.55,
            "is_archived": True
          }
        }
    }

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
    def check_fields(result, req_fields):
        data = json.loads(result.text)
        for field in req_fields['data'][0]:
            assert field in data['data'][0], f'отсутствует обязательное поле {field}'
        for field in req_fields['data'][0]['wallet']:
            assert field in data['data'][0]['wallet']
        print('Все поля присутствуют')

    @staticmethod
    def check_fields_get_by_id(result, req_fields):
        data = json.loads(result.text)
        for field in req_fields['data']:
            assert field in data['data'], f'отсутствует обязательное поле {field}'
        for field in req_fields['data']['wallet']:
            assert field in data['data']['wallet']
        print('Все поля присутствуют')

    # @staticmethod  #DELETE
    # def post_required_fields_value(email, last_name, first_name, middle_name, phone, date_of_birth, data):
    #     required_fields_values = {
    #         "email": email,
    #         "last_name": last_name,
    #         "first_name": first_name,
    #         "middle_name": middle_name,
    #         "phone_number": phone,
    #         "date_of_birth": date_of_birth
    #     }
    #     for field, value in required_fields_values.items():
    #         assert field in data, f'отсутствует обязательное поле {field}'
    #         assert data[field] == value, f'неверное значение {data[field]} ожидалось: {value}'
    #         print(field, value)

