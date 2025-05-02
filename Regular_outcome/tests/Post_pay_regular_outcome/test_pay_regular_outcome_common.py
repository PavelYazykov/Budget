import allure

from Regular_outcome.methods.regular_outcome_methods import RegularOutcomeMethods
from common_methods.checking import Checking
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from Regular_outcome.methods.payloads import RegularOutcomePayloads


@allure.epic('POST/api/v1/regular_outcome/pay_regular_outcome/{regular_outcome_id}/ - оплата регулярных списаний по id')
class TestPayRegularOutcomeCommon:

    @allure.description('Общие проверки - Отправка запроса  с валидными данными')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Запрос на создание regular_outcome"""
        result = RegularOutcomeMethods.create_regular_outcome(
            'title', 20, None, 'day', 100, False,
            '2030-12-12', access_token,
        )

        Checking.check_statuscode(result, 201)
        data = Checking.get_data(result)
        regular_outcome_id = data['data']['id']

        """Создание копилки"""
        result_create_moneybox = MoneyboxMethods.create_moneybox(
            '2030-12-12', 1000, 'name', 2, 100, access_token
        )
        Checking.check_statuscode(result_create_moneybox, 201)
        data = Checking.get_data(result_create_moneybox)
        wallet_id = data['data']['wallet']['id']
        moneybox_id = data['data']['id']
        try:
            """списание регулярного плтаежа"""
            result_pay = RegularOutcomeMethods.post_pay_regular_outcome(
                regular_outcome_id, wallet_id, access_token
            )

            """Проверка статус кода"""
            Checking.check_statuscode(result_pay, 200)

            """Проверка наличия обязательных полей"""
            RegularOutcomePayloads.check_required_fields(result_pay, RegularOutcomePayloads.pay_regular_outcome)
        finally:
            result_delete = RegularOutcomeMethods.delete_regular_outcome(regular_outcome_id, access_token)
            Checking.check_statuscode(result_delete, 204)
            result_delete_2 = MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            Checking.check_statuscode(result_delete_2, 204)



