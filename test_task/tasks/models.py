from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, unique=True)

    groups = models.ManyToManyField(
        Group,
        related_name='user_group',  
        blank=True,
        help_text='Группы, к которым принадлежит этот пользователь. Пользователь получит все разрешения, предоставленные каждой из его групп',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_permissions_set',  
        blank=True,
        help_text='Особые разрешения для этого пользователя',
        related_query_name='user',
    )

    def save(self, *args, **kwargs):
        if self.is_employee and self.is_customer:
            raise ValueError("Пользователь не может быть одновременно сотрудником и клиентом")
        super().save(*args, **kwargs)

class Task(models.Model):
    STATUS_CHOICES = [
        ('P', 'Ожидает исполнителя'),
        ('I', 'В процессе'),
        ('C', 'Выполнена'),
    ]

    customer = models.ForeignKey(User, related_name='created_tasks', on_delete=models.CASCADE, limit_choices_to={'is_customer': True})
    employee = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'is_employee': True})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    report = models.TextField(blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def save(self, *args, **kwargs):
        if self.status == 'C' and not self.report:
            raise ValueError("Отчет не может быть пустым при закрытии задачи")
        super().save(*args, **kwargs)