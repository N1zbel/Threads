from rest_framework import serializers

from .models import Comment, Post, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели UserProfile.

    Attributes:
        None

    """

    class Meta:
        model = UserProfile
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Post.

    Attributes:
        None

    """

    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Comment.

    Attributes:
        None

    """

    class Meta:
        model = Comment
        fields = "__all__"
