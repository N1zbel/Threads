from django.contrib.auth.models import User
from django.db import models

from .validators import (validate_author_age, validate_email_domain,
                         validate_title)


class UserProfile(models.Model):
    """
    Модель профиля пользователя.

    Attributes:
        user (User): Связь OneToOne с моделью User из django.contrib.auth.models.
        phone_number (str): Номер телефона пользователя.
        email (str): Адрес электронной почты пользователя.
        date_of_birth (date): Дата рождения пользователя.
        created_at (datetime): Дата и время создания профиля.
        updated_at (datetime): Дата и время последнего обновления профиля.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(validators=[validate_email_domain], blank=True, null=True)
    date_of_birth = models.DateField(validators=[validate_author_age])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Метод для представления объекта в виде строки.

        Returns:
            str: Строковое представление объекта.
        """
        return self.user.username


class Post(models.Model):
    """
    Модель поста.

    Attributes:
        title (str): Заголовок поста.
        text (str): Текст поста.
        image (ImageField): Изображение поста.
        author (UserProfile): Связь ForeignKey с моделью UserProfile.
        comments (ManyToManyField): Связь ManyToMany с моделью Comment.
        created_at (datetime): Дата и время создания поста.
        updated_at (datetime): Дата и время последнего обновления поста.
    """

    title = models.CharField(max_length=255, validators=[validate_title])
    text = models.TextField()
    image = models.ImageField(upload_to="post_images/", blank=True, null=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comments = models.ManyToManyField("Comment", related_name="post_comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Метод для представления объекта в виде строки.

        Returns:
            str: Строковое представление объекта.
        """
        return self.title


class Comment(models.Model):
    """
    Модель комментария.

    Attributes:
        author (UserProfile): Связь ForeignKey с моделью UserProfile.
        text (str): Текст комментария.
        created_at (datetime): Дата и время создания комментария.
        updated_at (datetime): Дата и время последнего обновления комментария.
    """

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Метод для представления объекта в виде строки.

        Returns:
            str: Строковое представление объекта.
        """
        return f"{self.author.user.username}: {self.text}"
