from django.test import TestCase
from django.contrib.auth import get_user_model

from model_mommy import mommy


class ModelTests(TestCase):
    def gen_number(self, _next=[7788480000]):
        # use mutable arg as a sequence to avoid dupe numbers
        value = '+1 {}'.format(_next[0])
        _next[0] += 1
        return value

    def setUp(self):
        mommy.generators.add('phonenumber_field.modelfields.PhoneNumberField', self.gen_number)

    def test_create_user_with_email_successful(self):
        """Test creating a new userwith an email is successful."""
        email = "test@andrew.com"
        password = "Password123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized."""
        email = 'test@ANDREW.COM'
        user = user = get_user_model().objects.create_user(
            email=email,
            password='test123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_valid_email(self):
        """Test creating user with no email raises error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        """Test creating a new superuser."""
        user = get_user_model().objects.create_superuser(
            'test@andrew.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_mommy(self):
        user = mommy.make('core.User')
        print("*" * 20)
        print(user.__dict__)
        print("*" * 20)
