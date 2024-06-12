from rest_framework import serializers
from .models import Task, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone', 'is_employee', 'is_customer']

    def validate(self, data):
        if data.get('is_employee') and data.get('is_customer'):
            raise serializers.ValidationError("User cannot be both employee and customer")
        return data

class TaskSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.username')
    employee = serializers.ReadOnlyField(source='employee.username')

    class Meta:
        model = Task
        fields = ['id', 'customer', 'employee', 'created_at', 'updated_at', 'closed_at', 'report', 'status']
        read_only_fields = ['created_at', 'updated_at', 'closed_at']

    def update(self, instance, validated_data):
        if instance.status == 'C':
            raise serializers.ValidationError("Выполненную задачу редактировать нельзя")
        return super().update(instance, validated_data)
