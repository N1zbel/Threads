from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date


def validate_author_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError(
            _('Author must be at least 18 years old to create a post.')
        )


def validate_title(value):
    forbidden_words = ['ерунда', 'глупость', 'чепуха']
    for word in forbidden_words:
        if word in value.lower():
            raise ValidationError(
                _('Title cannot contain forbidden words: ерунда, глупость, чепуха.')
            )


def validate_email_domain(value):
    allowed_domains = ['mail.ru', 'yandex.ru']
    domain = value.split('@')[-1]
    if domain not in allowed_domains:
        raise ValidationError(
            _('Invalid email domain. Allowed domains are: mail.ru, yandex.ru.')
        )
