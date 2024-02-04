from rest_framework import serializers
from uppy.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'excerpt', 'content', 'status']
