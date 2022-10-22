from django.test import TestCase
from ..models import UserManager, User
from ..serializers import UserSerializer, UserInfoSerializer, UserInfoTransSerializer, UserSerializerAdminAccess
import unittest

class UserSerializerTest(unittest.TestCase):
    def setUp(self):
        self.user_attributes = {
            'first_name': 'Julian',
            'last_name': 'Ophals',
            'email': 'blank@asu.edu'
        }

        self.serializer_data = {
            'first_name': 'Bob',
            'last_name': 'Jones'
        }

        self.user = User.objects.create(**self.user_attributes)
        print(self.user)
        self.serializer = UserSerializer(instance=self.user)
        print(self.serializer)

    def tearDown(self):
        self.user.delete()

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'email', 'first_name', 'last_name' , 'is_staff', 'is_superuser'])

    def test_email_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['email'], self.user_attributes['email'])

    def test_firstname_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['first_name'], self.user_attributes['first_name'])

    def test_id_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['id'], self.user.id)

    def test_is_staff_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['is_staff'], self.user.is_staff)
    
    def test_is_super_content(self):
        data = self.serializer.data
        self.assertEqual(data['is_superuser'], self.user.is_superuser)

    def test_lastname_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['last_name'], self.user_attributes['last_name'])
