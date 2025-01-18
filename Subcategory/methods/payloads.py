import json

import allure


class SubcategoryPayloads:
    get_payloads = {
        "meta": {},
        "data": [
            {
                "category_id": 1,
                "title": "Title or description",
                "id": 1,
                "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "is_archived": True
            }
        ]
    }

    get_payloads_by_id = {
        "meta": {},
        "data":
            {
                "category_id": 1,
                "title": "Title or description",
                "id": 1,
                "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "is_archived": True
            }
    }

    post_payloads = {
        "meta": {},
        "data":
            {
                "category_id": 1,
                "title": "Title or description",
                "id": 1,
                "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "is_archived": True
            }
    }

    @staticmethod
    def check_req_fields_get(result, required_fields):
        with allure.step('Проверка наличия обязательных полей'):
            result_text = result.text
            data = json.loads(result_text)
            for field in required_fields:
                assert field in data, f'Отсутствует обязательное поле {field}'

            for field in required_fields['data'][0]:
                assert field in data['data'][0], f'Отсутствует обязательное поле {field}'

            print('Все поля присутствуют')

    @staticmethod
    def check_req_fields_get_by_id(result, required_fields):
        with allure.step('Проверка наличия обязательных полей'):
            result_text = result.text
            data = json.loads(result_text)
            for field in required_fields:
                assert field in data, f'Отсутствует обязательное поле {field}'

            for field in required_fields['data']:
                assert field in data['data'], f'Отсутствует обязательное поле {field}'

            print('Все поля присутствуют')

    @staticmethod
    def check_required_fields_post(result, required_fields):
        with allure.step('Проверка наличия обязательных полей'):
            result_text = result.text
            data = json.loads(result_text)
            for field in required_fields:
                assert field in data, f'Отсутствует обязательное поле {field}'

            for field in required_fields['data']:
                assert field in data['data'], f'Отсутствует обязательное поле {field}'

            print('Все поля присутствуют')



