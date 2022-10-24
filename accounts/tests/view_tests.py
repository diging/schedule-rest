from django.test import TestCase, Client
from django.urls import reverse
from ..views import create_user, delete_user, get_current_user, signup, update_user, update_user_role, user_info, user_search, users_list
from ..models import User
from ..serializers import UserSerializer
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory
from django.shortcuts import get_object_or_404
from rest_framework.generics import get_object_or_404
import json

factory = APIRequestFactory()

class ViewTest(APITestCase):
    def setUp(self):
        self.new_user = User(first_name= 'Julian', last_name='Ophals', email='test@asu.edu', is_staff=True, is_superuser=True, password='password')
        self.json_user = {
            'first_name': self.new_user.first_name,
            'last_name': self.new_user.last_name,
            'email': self.new_user.email,
            'is_staff': self.new_user.is_staff,
            'is_superuser': self.new_user.is_superuser,
            'password': self.new_user.password
        }

        self.user_attributes = {
            'first_name': 'Julian',
            'last_name': 'Ophals',
            'email': 'test2@asu.edu',
            'is_staff': True, 
            'is_superuser': True
        }

        self.user = User.objects.create(**self.user_attributes)
        self.serializer = UserSerializer(instance=self.user)

    def tearDown(self):
        self.user.delete()

    def test_create_user(self):
        request = factory.post('create_user', self.json_user, format='json')
        force_authenticate(request, user=self.new_user)
        response = create_user(request)
        self.assertEqual(response.status_code, 201)

    def test_delete_user(self):
        request = factory.delete('delete_user')
        force_authenticate(request, user=self.new_user)
        response = delete_user(request, self.user.id)
        self.assertEqual(response.status_code, 200)

    def test_get_current_user(self):
        request = factory.get('get_current_user', self.serializer.data, format='json')
        force_authenticate(request, user=self.user)
        response = get_current_user(request)
        self.assertEqual(response.status_code, 200)

    def test_user_info(self):
        request = factory.get('user_info', self.serializer.data, format='json')
        force_authenticate(request, user=self.user)
        response = user_info(request)
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        request = factory.post('signup', self.json_user, format='json')
        response = signup(request)
        self.assertEqual(response.status_code, 201)

    def test_update_user(self):
        request = factory.patch('/accounts/users/' + str(self.user.id) + '/update', self.serializer.data, format='json')
        force_authenticate(request, user=self.user)
        response = update_user(request, self.user.id)
        self.assertEqual(response.status_code, 200)

    def test_update_user_role(self):
        request = factory.patch('/accounts/users/' + str(self.user.id), self.json_user, format='json')
        response = update_user_role(request, self.user.id)
        self.assertEqual(response.status_code, 200)

    def test_user_search(self):
        request = factory.get('user_search', {'email': self.user.email}, format='json')
        force_authenticate(request, user=self.user)
        response = user_search(request)
        self.assertEqual(response.status_code, 200)

    def test_users_list(self):
        request = factory.get('users_list')
        response = users_list(request)
        self.assertEqual(response.status_code, 200)