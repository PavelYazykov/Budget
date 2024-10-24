from Auth.methods.auth_methods import AuthMethods
from common_methods.checking import Checking
import psycopg2

# email = 'pawel_test_1@rambler.ru'
password = 'Ohranatruda@1'

# result = AuthMethods.forgot_password(None, email)
# Checking.check_statuscode(result, 200)
# result_code = AuthMethods.get_verify_code(result)
# result_check = AuthMethods.code_check(None, email, 111111)
# print(result_check.text)
# print(result_check.status_code)
# check = Checking.check_statuscode(result_check, 422)
# if result_check.status_code == 422:
#     print('Yes')
# else:
#     print('No')
email = 'zx@mail.ru'
with psycopg2.connect(
        host='82.97.248.83',
        user='postgres',
        password='postgres',
        dbname='budget',
        port=25432
) as connection:
    cursor = connection.cursor()
# cursor.execute(f"""SELECT * FROM users WHERE id= '34318bde-4072-4927-b3ec-0319039f9ccd'""")
#         result_db = cursor.fetchall()
#         print(result_db)
    user_id = '34318bde-4072-4927-b3ec-0319039f9ccd'
    cursor.execute(f"""SELECT id FROM users WHERE email= '{email}'""")
    result_db = cursor.fetchone()
    email = result_db[0]
    print(email)




