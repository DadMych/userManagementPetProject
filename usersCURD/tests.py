from django.test import TestCase
from usersCURD.models import User


class RegistrationTest(TestCase):
    def setUp(self):
        self.user = User()
        self.user.username = "aaa"
        self.user.first_name = "bbb"
        self.user.last_name = "ccc"
        self.user.email = "dadmych@gmail.com"
        self.user.user_type = "Administrator"
        self.user.password = "312312a"
        self.user.save()

        self.user2 = User()
        self.user2.username = "aaas"
        self.user2.first_name = "bbb"
        self.user2.last_name = "cscc"
        self.user2.email = "dadmych.com"
        self.user2.user_type = "Administrator"
        self.user2.password = "312312aa"
        self.user2.save()

    def tearDown(self):
        self.user.delete()

    def test_password(self):
        self.assertEqual(self.user.password, "^(?=.*[A-Za-z])(?=.*?[0-9]).{8,}$'")
        self.assertEqual(self.user2.password, r'^(?=.*[A-Za-z])(?=.*?[0-9]).{8,}$')

    def test_email(self):
        self.assertEqual(self.user.email, r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$')
        self.assertEqual(self.user2.email, r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$')
