from .models import Post, Comment
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # Display the username or email of the author

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # Display the username or email of the author
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())  # Validate the post exists

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']