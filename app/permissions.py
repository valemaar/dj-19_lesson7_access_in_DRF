from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthOrReadOnly(BasePermission):
    # работаем со всеми обектами сразу
    def has_permission(self, request, view):
        # если идет запрос на чтение, то разрешаем всем (SAFE_METHODS=[GET,HEAD,OPTIONS])
        if request.method in SAFE_METHODS:
            return True

        # если иначе, то проверяем есть ли такой пользователь и прошел ли он аутентификацию
        return request.user and request.user.is_authenticated

    # работаем с одним обектом
    def has_object_permission(self, request, view, obj):
        # если идет запрос на чтение, то разрешаем всем (SAFE_METHODS=[GET,HEAD,OPTIONS])
        if request.method in SAFE_METHODS:
            return True
        # если иначе, то проверяем является ли автор запроса автором поста
        return request.user == obj.user
