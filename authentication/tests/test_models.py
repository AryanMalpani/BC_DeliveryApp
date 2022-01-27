from rest_framework.test import APITestCase
from authentication.models import User

class TestModel(APITestCase):
    
    def test_creates_user(self):
        user = User.objects.create_user('aryan','dude@gmail.com','pwdpwdpwd')
        self.assertIsInstance(user,User) #used to check is the user is an instance of User
        self.assertFalse(user.is_staff) #used to check for no superuser
        self.assertEqual(user.email,'dude@gmail.com')

    def test_creates_super_user(self):
        user = User.objects.create_superuser('aryan','dude@gmail.com','pwdpwdpwd')
        self.assertIsInstance(user,User) #used to check is the user is an instance of User
        self.assertTrue(user.is_staff) #used to check for superuser
        self.assertEqual(user.email,'dude@gmail.com')

    def test_raises_error_when_no_username_is_supplied(self):

        self.assertRaises(ValueError, User.objects.create_user,username = '', email = 'dude@gmail.com',password = 'pwdpwdpwd')

    def test_raises_error_when_no_email_is_supplied(self):

        self.assertRaises(ValueError, User.objects.create_user,username = 'asdfasdg', email = '',password = 'pwdpwdpwd')

    def test_cant_create_super_user_with_no_is_staff_status(self):

        self.assertRaises(ValueError, User.objects.create_superuser, username = 'asdfasdg', email = 'asdf@gmail.com',password = 'pwdpwdpwd', is_staff = False)

    def test_cant_create_super_user_with_no_is_super_user_status(self):

        self.assertRaises(ValueError, User.objects.create_superuser, username = 'asdfasdg', email = 'asdf@gmail.com',password = 'pwdpwdpwd', is_superuser = False)