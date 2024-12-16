import json
from datetime import date
import allure
from Moneybox.methods.moneybox_methods import MoneyboxMethods


class Checking:
    """Проверки"""

    @staticmethod
    def check_statuscode(result, status_code):
        with allure.step('Проверка статус кода'):
            assert result.status_code == status_code, f"Ошибка {result.text}"
            print(
                f'Успешно статус код: {result.status_code}\n {result.text}'
            )

    @staticmethod
    def get_data(result):
        with allure.step(f'Получение данных'):
            result_text = result.text
            data = json.loads(result_text)
            return data

    @staticmethod
    def delete_moneybox_if_bug(result, status_code, access_token):
        with allure.step('Удаление копилки при баге'):
            result_code = result.status_code
            if result_code == status_code:
                result_text = result.text
                data = json.loads(result_text)
                moneybox_id = data['data']['id']
                result_delete = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
                print(f'Копилка удалена {result_delete}')
