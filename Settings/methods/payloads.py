import json

import allure


class SettingsPayloads:

    message = 'exttexttexttexttexttexttexttexttexttexttext'
    required_fields = {
            "meta": {},
            "data": {
                "id": 1,
                "personal_accounting": True,
                "business_accounting": True,
                "analytics": True,
                "use_subcategories": True,
                "use_quantity": True,
                "push_notifications": True,
                "email_notifications": True,
                "default_currency_id": 1,
                "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "excluded_categories": [
                    "Title or description"
                ]
            }
        }

    @staticmethod
    def check_required_fields(result, required_fields):
        with allure.step('Проверка наличия обязательных полей'):

            result_text = result.text
            data = json.loads(result_text)
            for field in required_fields:
                assert field in data, f'поле {field} отсутствует'

            for field in required_fields['data']:
                assert field in data['data'], f'поле {field} отсутствует'
            print('Все поля присутствуют')

