from ..models import UserManager, User
from ..serializers import UserSerializer, UserInfoSerializer, UserInfoTransSerializer, UserSerializerAdminAccess
import unittest

class UserSerializerTest(unittest.TestCase):
    def setUp(self):
        self.user_attributes = {
            'first_name': 'Julian',
            'last_name': 'Ophals',
            'email': 'test@asu.edu'
        }

        self.admin_attributes = {
            'first_name': 'Julian',
            'last_name': 'Ophals',
            'email': 'test_admin@asu.edu',
            'is_staff': True,
            'is_superuser': True
        }

        self.serializer_data = {
            'first_name': 'Bob',
            'last_name': 'Jones'
        }

        self.user = User.objects.create(**self.user_attributes)
        self.serializer = UserSerializer(instance=self.user)

        self.admin = User.objects.create(**self.admin_attributes)
        self.admin_serializer = UserSerializerAdminAccess(instance=self.admin)

    def tearDown(self):
        self.user.delete()
        self.admin.delete()

    def test_contains_expected_fields_user(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'email', 'first_name', 'last_name' , 'is_staff', 'is_superuser'])

    def test_email_field_content_user(self):
        data = self.serializer.data
        self.assertEqual(data['email'], self.user_attributes['email'])

    def test_firstname_field_content_user(self):
        data = self.serializer.data
        self.assertEqual(data['first_name'], self.user_attributes['first_name'])

    def test_id_field_content_user(self):
        data = self.serializer.data
        self.assertEqual(data['id'], self.user.id)

    def test_is_staff_field_content_user(self):
        data = self.serializer.data
        self.assertEqual(data['is_staff'], self.user.is_staff)
    
    def test_is_super_content_user(self):
        data = self.serializer.data
        self.assertEqual(data['is_superuser'], self.user.is_superuser)

    def test_lastname_field_content_user(self):
        data = self.serializer.data
        self.assertEqual(data['last_name'], self.user_attributes['last_name'])

    def test_contains_expected_fields_admin(self):
        data = self.admin_serializer.data
        self.assertCountEqual(data.keys(), ['id', 'email', 'first_name', 'last_name','is_superuser', 'date_joined', 'is_active', 'is_staff'])

    def test_email_field_content_admin(self):
        data = self.admin_serializer.data
        self.assertEqual(data['email'], self.admin_attributes['email'])

    def test_firstname_field_content_admin(self):
        data = self.admin_serializer.data
        self.assertEqual(data['first_name'], self.admin_attributes['first_name'])

    def test_id_field_content_admin(self):
        data = self.admin_serializer.data
        self.assertEqual(data['id'], self.admin.id)

    def test_is_staff_field_content_admin(self):
        data = self.admin_serializer.data
        self.assertEqual(data['is_staff'], self.admin.is_staff)
    
    def test_is_super_content_admin(self):
        data = self.admin_serializer.data
        self.assertEqual(data['is_superuser'], self.admin.is_superuser)

    def test_lastname_field_content_admin(self):
        data = self.admin_serializer.data
        self.assertEqual(data['last_name'], self.admin_attributes['last_name'])
