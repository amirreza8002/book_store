from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    USER = get_user_model()

    def test_create_user(self):
        user = self.USER.objects.create_user(
            username="amir",
            email="amir@email.com",
            password="testpass123",
        )

        self.assertEqual(user.username, "amir")
        self.assertEqual(user.email, "amir@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user = self.USER.objects.create_superuser(
            username="superadmin",
            email="superadmin@email.com",
            password="testpass123",
        )

        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
