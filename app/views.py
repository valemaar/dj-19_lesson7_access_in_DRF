from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

from app.models import Post
from app.permissions import IsAuthOrReadOnly
from app.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # # 1 теперь просматриватьи создавать посты могут только пользоваатели,
    # # прошедшие аутентификацию (у кого есть токен)
    # permission_classes = [IsAuthenticated]

    # 2 откроем доступ на чтение всем пользователям,
    # а на изменение только прошедшим аутентификацию
    permission_classes = [IsAuthOrReadOnly]

    # добавляем на текущий viewset защиту от троттлинга,
    # то есть включаем ограничение на обработку слишком большого кол-ва запросов
    # от одного и того же пользователя
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    # переопределим метод создания объектов
    # при создании поста не надо указывать пользователя
    # он будет определяться автоматически по токену
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
