from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date


def validate_author_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError(
            _('Автор должен быть не младше 18 лет для создания поста.')
        )


def validate_title(value):
    forbidden_words = ['ерунда', 'глупость', 'чепуха']
    for word in forbidden_words:
        if word in value.lower():
            raise ValidationError(
                _('Заголовок не может содержать запрещенные слова: ерунда, глупость, чепуха.')
            )


def validate_email_domain(value):
    allowed_domains = ['mail.ru', 'yandex.ru']
    domain = value.split('@')[-1]
    if domain not in allowed_domains:
        raise ValidationError(
            _('Недопустимый домен электронной почты. Разрешенные домены: mail.ru, yandex.ru.')
        )
