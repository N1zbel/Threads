from datetime import date

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_author_age(value):
    """
    Проверяет, достиг ли автор поста 18 лет.

    Args:
        value (date): Дата рождения автора.

    Raises:
        ValidationError: Если автор не достиг 18 лет.

    """
    today = date.today()
    age = (
        today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    )
    if age < 18:
        raise ValidationError(
            _("Author must be at least 18 years old to create a post.")
        )


def validate_title(value):
    """
    Проверяет, содержит ли заголовок поста запрещенные слова.

    Args:
        value (str): Заголовок поста.

    Raises:
        ValidationError: Если заголовок содержит запрещенные слова.

    """
    forbidden_words = ["ерунда", "глупость", "чепуха"]
    for word in forbidden_words:
        if word in value.lower():
            raise ValidationError(
                _("Title cannot contain forbidden words: ерунда, глупость, чепуха.")
            )


def validate_email_domain(value):
    """
    Проверяет, принадлежит ли домен электронной почты к разрешенным доменам.

    Args:
        value (str): Адрес электронной почты.

    Raises:
        ValidationError: Если домен электронной почты не принадлежит разрешенным доменам.

    """
    allowed_domains = ["mail.ru", "yandex.ru"]
    domain = value.split("@")[-1]
    if domain not in allowed_domains:
        raise ValidationError(
            _("Invalid email domain. Allowed domains are: mail.ru, yandex.ru.")
        )
