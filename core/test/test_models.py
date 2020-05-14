from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email successufl"""
        email = 'omolayoabegunde@gmail.com'
        password = 'csc2009001'
        user = get_user_model().objects.create_user(
            email = email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test the email for a new user is normalized"""
        email = 'omolayoabegunde@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'csc2009001')
        
        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'csc2009001')

    def test_create_new_superuer(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'omolayoabegunde@gmail.com',
            'csc2009001',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

