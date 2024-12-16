import allure
from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
from Auth.methods.payloads import Payloads
from common_methods.variables import AuthVariables
email = AuthVariables.email_for_create_user
password = AuthVariables.password_for_create_user
last_name = AuthVariables.last_name
first_name = AuthVariables.first_name
middle_name = AuthVariables.middle_name
phone = AuthVariables.phone_for_create_user
date_of_birth = AuthVariables.date_of_birth


@allure.epic('Post/registration Проверка поля lastname')
class TestRegistrationLastnameField:

    @allure.description('1 символ')
    def test_01(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Z', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, 'Z', first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, 'Z', first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('2 символа')
    def test_02(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Zz', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, 'Zz', first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, 'Zz', first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Кириллица')
    def test_03(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Ффф', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, 'Ффф', first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, 'Ффф', first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Латиница')
    def test_04(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Aaa', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, 'Aaa', first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, 'Aaa', first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('63 символа')
    def test_05(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            'Automationautomationautomationautomationautomationautomationasd',
            first_name,
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email,
                'Automationautomationautomationautomationautomationautomationasd',
                first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id,
                'Automationautomationautomationautomationautomationautomationasd',
                first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('64 символа')
    def test_06(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            'Automationautomationautomationautomationautomationautomationasdd',
            first_name,
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email,
                'Automationautomationautomationautomationautomationautomationasdd',
                first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id,
                'Automationautomationautomationautomationautomationautomationasdd',
                first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Пробел')
    def test_07(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            'Automation Aut',
            first_name,
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        result_code = result.status_code
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, 'Automation Aut', first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, 'Automation Aut', first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Тире')
    def test_08(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Фф-ф', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, 'Фф-Ф', first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, 'Фф-Ф', first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Текст в верхнем регистре')
    def test_09(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'QQQ', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, 'Qqq', first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, 'Qqq', first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Текст в нижнем регистре')
    def test_10(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'йййй', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, 'Йййй', first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, 'Йййй', first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Текст в верхнем и нижнем регистре')
    def test_11(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Фйййй', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, 'Фйййй', first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, 'Фйййй', first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('2 пробела подряд')
    def test_12(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Фййй  й', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, 'Фййй Й', first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, 'Фййй Й', first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('2 тире подряд')
    def test_13(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Фййй--й', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, 'Фййй-Й', first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, 'Фййй-Й', first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Пустое поле')
    def test_14(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, '', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('65 Символов')
    def test_15(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email,
            password,
            'AaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqAaaaaaaaaqzxcvb',
            first_name,
            middle_name,
            phone,
            date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('Латиница + Кириллица')
    def test_16(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'AAAфффф', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('3 пробела подряд')
    def test_17(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Фййй   Й', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, 'Фййй Й', first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, 'Фййй Й', first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('3 тире подряд')
    def test_18(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Фййй---й', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, 'Фййй-Й', first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, 'Фййй-Й', first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Цифры')
    def test_19(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, '0123456', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('Спецсимволы')
    def test_20(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, '!№?%', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)

    @allure.description('Начинается пробелом')
    def test_21(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, ' Фывв', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, 'Фывв', first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, 'Фывв', first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Заканчивается пробелом')
    def test_22(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Фывв ', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, 'Фывв', first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, 'Фывв', first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Начинается с "тире"')
    def test_23(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, '-Фывв', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, 'Фывв', first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, 'Фывв', first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Заканчивается "тире"')
    def test_24(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, 'Фывв-', first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result, 201)

        """Проверка наличия обязательных полей в ответе"""
        try:
            data, user_id = AuthMethods.check_required_fields(result, Payloads.required_fields())

            """Проверка значений обязательных полей"""
            Payloads.required_fields_value(
                email, 'Фывв', first_name, middle_name, phone, date_of_birth, data
            )

            """Проверка наличия пользователя в БД"""
            AuthMethods.connect_db_check_user(
                user_id, 'Фывв', first_name, middle_name, phone, email, date_of_birth
            )
        except AssertionError:
            print('Ошибка!')
            raise AssertionError
        else:
            print('Значения полей в БД соответствуют введенным')
        finally:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)

    @allure.description('Null')
    def test_25(self):
        """Регистрация"""
        result = AuthMethods.registration(
            email, password, None, first_name, middle_name, phone, date_of_birth
        )

        """Проверка статус кода"""
        if result.status_code == 201:
            """Удаление пользователя из БД"""
            AuthMethods.delete_user(email)
        Checking.check_statuscode(result, 422)
