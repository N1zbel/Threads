from rest_framework import generics, permissions

from .models import Comment, Post, UserProfile
from .permissions import IsOwnerOrAdminPermission
from .serializers import (CommentSerializer, PostSerializer,
                          UserProfileSerializer)


class UserProfileListCreateView(generics.ListCreateAPIView):
    """
    Представление для создания и просмотра списка профилей пользователей.

    Attributes:
        queryset: Запрос к объектам UserProfile.
        serializer_class: Сериализатор для объектов UserProfile.

    """

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для просмотра, обновления и удаления профиля пользователя.

    Attributes:
        queryset: Запрос к объектам UserProfile.
        serializer_class: Сериализатор для объектов UserProfile.
        permission_classes: Классы разрешений для доступа к представлению.

    """

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrAdminPermission]


class PostListCreateView(generics.ListCreateAPIView):
    """
    Представление для создания и просмотра списка постов.

    Attributes:
        queryset: Запрос к объектам Post.
        serializer_class: Сериализатор для объектов Post.
        permission_classes: Классы разрешений для доступа к представлению.

    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для просмотра, обновления и удаления поста.

    Attributes:
        queryset: Запрос к объектам Post.
        serializer_class: Сериализатор для объектов Post.
        permission_classes: Классы разрешений для доступа к представлению.

    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrAdminPermission]


class CommentListCreateView(generics.ListCreateAPIView):
    """
    Представление для создания и просмотра списка комментариев.

    Attributes:
        queryset: Запрос к объектам Comment.
        serializer_class: Сериализатор для объектов Comment.
        permission_classes: Классы разрешений для доступа к представлению.

    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для просмотра, обновления и удаления комментария.

    Attributes:
        queryset: Запрос к объектам Comment.
        serializer_class: Сериализатор для объектов Comment.
        permission_classes: Классы разрешений для доступа к представлению.

    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrAdminPermission]
