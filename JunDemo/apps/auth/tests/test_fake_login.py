from django.conf import settings
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.test import APIClient

#from utils.helpers_for_tests import dump, login_user, create_user


class FakeLoginAPITest(TestCase):

    def setUp(self):
        print('in setup')
        self.c = APIClient()
        self.user = User.objects.create(**{
            'username': 'test.user',
            'password': make_password('111'),
            'email': 'test.user@tt.com'
        })
        pass


    def test_login_user(self):
        response = self.c.get(
            '/api/auth/fake/?username={username}&password={password}'.format(
                username = self.user.username,
                    password = '111'    
            )
        )
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.content, b"")

    def test_login_wrong_password_user(self):
        response = self.c.get(
            '/api/auth/fake/?username={username}&password={password}'.format(
                username = self.user.username,
                    password = '111123123312'    
            )
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.content, b"Wrong password")

    def test_login_user_no_passwd(self):
        response = self.c.get(
            '/api/auth/fake/'
        )
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.content, b"Wrong password")
