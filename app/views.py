from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app.models import Post
from app.permissions import IsAuthOrReadOnly
from app.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # # теперь просматриватьи создавать посты могут только пользоваатели,
    # # прошедшие аутентификацию (у кого есть токен)
    # permission_classes = [IsAuthenticated]
    
    permission_classes = [IsAuthOrReadOnly]

    # переопределим метод создания объектов
    # при создании поста не надо указывать пользователя, он будет определяться
    # автоматически по токену
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
