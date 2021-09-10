from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from app.views import PostViewSet

r = DefaultRouter()
r.register('posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
] + r.urls
