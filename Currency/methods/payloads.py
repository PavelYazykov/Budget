import json

import allure


class CurrencyPayloads:
    post_payloads = {
        "meta": {},
        "data":
            {
                "code": 0,
                "full_title": "Russian ruble",
                "short_title": "RUB",
                "id": 1
            }
    }

    @staticmethod
    def check_required_fields(result, required_fields):
        with allure.step('Проверка наличия обязательных полей'):
            result_text = result.text
            data = json.loads(result_text)
            for field in required_fields:
                assert field in data, f'отсутствует обязательное поле {field}'

            for field in required_fields['data']:
                assert field in data['data'], f'отсутствует обязательное поле {field}'

            print('Все поля присутствуют')
