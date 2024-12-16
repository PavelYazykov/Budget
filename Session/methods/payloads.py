import json

import allure


class SessionPayloads:
    get_payloads = {
        "meta": {},
        "data": [
            {
                "device_id": "string",
                "last_active": "string",
                "system": "string",
                "client": "string",
                "location": "string"
            }
        ]
    }

    @staticmethod
    def check_required_fields(result, required_fields):
        with allure.step('Проверка наличия обязательных полей'):
            result_text = result.text
            data = json.loads(result_text)

            for field in required_fields:
                assert field in data, f'обязательное поле {field} отсутствует'

            for field in required_fields['data']:
                for i_field in field:
                    assert i_field in data['data'][0]
