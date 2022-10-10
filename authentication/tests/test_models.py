from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):

  def test_creates_user(self):
    user = User.objects.create_user('Dini', 'dini@example.com', 'password')
    self.assertIsInstance(user, User)
    self.assertEqual(user.username, 'Dini')
    self.assertEqual(user.email, 'dini@example.com')
    self.assertFalse(user.is_staff)

  def test_creates_superuser(self):
    user = User.objects.create_superuser(
        'Dini', 'dini@example.com', 'password')
    self.assertIsInstance(user, User)
    self.assertEqual(user.username, 'Dini')
    self.assertEqual(user.email, 'dini@example.com')
    self.assertTrue(user.is_staff)

  def test_raises_error_when_no_username_is_supplied(self):
    self.assertRaises(ValueError, User.objects.create_user,
                      username="", email='dini@example.com', password='password')
    self.assertRaisesMessage(ValueError, "The given username must be set")

  def test_raises_error_with_message_when_no_username_is_supplied(self):
    with self.assertRaisesMessage(ValueError, "The given username must be set"):
      User.objects.create_user(
          username="", email='dini@example.com', password='password')

  def test_raises_error_when_no_email_is_supplied(self):
    self.assertRaises(ValueError, User.objects.create_user,
                      username="Dini", email="", password='password')
    self.assertRaisesMessage(ValueError, "The given email must be set")

  def test_raises_error_with_message_when_no_email_is_supplied(self):
    with self.assertRaisesMessage(ValueError, "The given email must be set"):
      User.objects.create_user(
          username="Dini", email='', password='password')

  def test_cant_create_superuser_with_no_is_staff_status(self):
    with self.assertRaisesMessage(ValueError, "Superuser must have is_staff=True."):
      User.objects.create_superuser(
          username="Dini", email='', password='password', is_staff=False)

  def test_cant_create_superuser_with_no_superuser_status(self):
    with self.assertRaisesMessage(ValueError, "Superuser must have is_superuser=True."):
      User.objects.create_superuser(
          username="Dini", email='', password='password', is_superuser=False)
