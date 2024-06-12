from rest_framework import permissions

class IsEmployee(permissions.BasePermission):
    """
    Настраиваемое разрешение, позволяющее сотрудникам получать доступ только к определенным действиям
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_employee

class IsCustomer(permissions.BasePermission):
    """
    Настраиваемое разрешение, позволяющее клиентам получать доступ только к определенным действиям
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_customer

class IsTaskAssigneeOrReadOnly(permissions.BasePermission):
    """
    Разрешение, позволяющее редактировать задачу только ответственным за нее
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.employee == request.user or request.user.has_perm('tasks.view_all_tasks')