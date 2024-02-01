from rest_framework import permissions


class IsOwnerOrAdminPermission(permissions.BasePermission):
    """
    Пользовательское разрешение для проверки прав доступа к объекту.

    Позволяет доступ только владельцу объекта или администратору.

    Attributes:
        None

    Methods:
        has_object_permission(request, view, obj): Проверяет, имеет ли пользователь доступ к объекту.

    """

    def has_object_permission(self, request, view, obj):
        """
        Проверяет, имеет ли пользователь доступ к объекту.

        Args:
            request (HttpRequest): Запрос пользователя.
            view (APIView): Представление, к которому относится объект.
            obj: Объект, к которому проверяются права доступа.

        Returns:
            bool: True, если пользователь имеет доступ к объекту, иначе False.
        """
        return obj.author == request.user or request.user.is_staff
