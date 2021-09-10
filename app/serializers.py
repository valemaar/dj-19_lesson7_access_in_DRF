from rest_framework import serializers

from app.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'text', 'created_at']
        read_only_fields = ['user']
