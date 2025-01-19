import time
import os.path
import allure
import pytest

from common_methods.checking import Checking
from Users.methods.users_methods import UsersMethods
mbJPG = os.path.abspath(os.path.join('..', '..', 'download_files', '1mbJPG.jpg'))


@allure.epic('Post/users/upload_avatar Загрузка аватара')
class TestPostUploadAvatar:
    time.sleep(3)

    @allure.description('Загрузка изображения в формате jpg')
    def test_01(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Загрузка аватара"""
        result = UsersMethods.upload_file(
            '1mbJPG.jpg', '../../download_files/1mbJPG.jpg', access_token
        )
        print(result.json())
        Checking.check_statuscode(result, 200)

    @pytest.mark.path
    @allure.description('Загрузка изображения в формате jpg')
    def test_010(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Загрузка аватара"""
        result = UsersMethods.upload_file(
            '1mbJPG.jpg', os.path.abspath('1mbJPG.jpg'), access_token
        )
        print(result.json())
        Checking.check_statuscode(result, 200)

    @allure.description('Загрузка изображения в формате jpeg')
    def test_02(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Загрузка аватара"""
        result = UsersMethods.upload_file(
            '1mbJPEG.jpeg', '../../download_files/1mbJPEG.jpeg', access_token
        )
        print(result.json())
        Checking.check_statuscode(result, 200)

    @allure.description('Загрузка изображения в формате png')
    def test_03(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Загрузка аватара"""
        result = UsersMethods.upload_file(
            '1mbPNG.png', '../../download_files/1mbPNG.png', access_token
        )
        print(result.json())
        Checking.check_statuscode(result, 200)

    @allure.description('Загрузка изображения меньше 1 Mb')
    def test_04(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Загрузка аватара"""
        result = UsersMethods.upload_file(
            'less1mb.jpg', '../../download_files/less1mb.jpg', access_token
        )
        print(result.json())
        Checking.check_statuscode(result, 200)

    @allure.description('Загрузка изображения 1 Mb')
    def test_05(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Загрузка аватара"""
        result = UsersMethods.upload_file(
            '1mbJPEG.jpeg', '../../download_files/1mbJPEG.jpeg', access_token
        )
        print(result.json())
        Checking.check_statuscode(result, 200)

    @allure.description('Загрузка изображения более 1 Mb')
    def test_06(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Загрузка аватара"""
        result = UsersMethods.upload_file(
            'more1mb.jpg', '../../download_files/more1mb.jpg', access_token
        )
        print(result.json())
        Checking.check_statuscode(result, 413)

    @allure.description('Загрузка изображения - недопустимый формат')
    def test_07(self, auth_fixture):
        """Авторизация"""
        access_token = auth_fixture

        """Загрузка аватара"""
        result = UsersMethods.upload_file(
            'less1mb.txt', '../../download_files/less1mb.txt', access_token
        )
        print(result.json())
        Checking.check_statuscode(result, 200)

