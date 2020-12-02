from django.test import TestCase

from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@mail.com'
        password = '123qwe'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@MAIL.com'
        user = get_user_model().objects.create_user(email, '123qwe')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""    
        with self.assertRaises(ValueError) :
            get_user_model().objects.create_user(None, '123qwe')

    def test_create_new_super_user(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'test@mail.com',
            '123qwe'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)