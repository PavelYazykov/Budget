# ВЕРНУТЬ НАЗВАНИЕ ФАЙЛА НА YML
# workflow:
#     rules:
#         - if: '$CI_PIPELINE_SOURCE == "push"'
#           when: never
#         - when: always
#
# default:
#     tags:
#         - god_docker_02
#
# stages:
#     - test
#
# run_tests:
#     stage: test
#     image: python
#     artifacts:
#         when: always
#         expire_in: 5 days
#         paths:
#             - allure-report
#     before_script:
#         - wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
#         - apt update && apt install -y openjdk-17-jdk openjdk-17-jre
#         - wget https://github.com/allure-framework/allure2/releases/download/2.30.0/allure-2.30.0.tgz && tar
#             -zxvf allure-2.30.0.tgz -C /opt/ && ln -s /opt/allure-2.30.0/bin/allure /usr/bin/allure
#         - pip install -r requirements.txt
#     script:
#         - pytest -v --alluredir=allure-results
#     after_script:
#         - allure generate -c allure-results -o allure-report