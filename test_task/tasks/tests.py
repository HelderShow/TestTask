from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Task

class UserTests(APITestCase):

    def setUp(self):
        self.admin_user = User.objects.create_user(username='Adminus', password='helloworldadmin', is_staff=True)
        self.employee_user = User.objects.create_user(username='TraineeAlexander', password='ilovepython2024', is_employee=True)
        self.customer_user = User.objects.create_user(username='Dmitry', password='bhil32rfewt', is_customer=True)

    def test_create_user(self):
        self.client.login(username='Adminus', password='helloworldadmin')
        url = reverse('user-list')
        data = {
            'username': 'new_user',
            'password': 'new_password',
            'is_employee': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 4)

    def test_get_current_user(self):
        url = reverse('current_user')
        self.client.force_authenticate(user=self.employee_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.employee_user.username)

class TaskTests(APITestCase):

    def setUp(self):
        self.customer_user = User.objects.create_user(username='Dmitry', password='bhil32rfewt', is_customer=True)
        self.employee_user = User.objects.create_user(username='TraineeAlexander', password='ilovepython2024', is_employee=True)
        self.task = Task.objects.create(customer=self.customer_user, status='P')

    def test_create_task(self):
        self.client.login(username='Dmitry', password='bhil32rfewt')
        url = reverse('task-list')
        data = {
            'customer': self.customer_user.id,
            'status': 'P',
            'report': ''
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_update_task(self):
        self.client.force_authenticate(user=self.employee_user)
        url = reverse('task-detail', args=[self.task.id])
        data = {
            'status': 'I',
            'report': 'Задача в процессе выполнения'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.status, 'I')
        self.assertEqual(self.task.report, 'Задача в процессе выполнения')

    def test_delete_task(self):
        self.client.force_authenticate(user=self.employee_user)
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TokenTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='TestUser227', password='wegwe331e2dfewr')
        self.url = reverse('token_obtain_pair')

    def test_get_tokens(self):
        data = {
            'username': self.user.username,
            'password': 'wegwe331e2dfewr'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
