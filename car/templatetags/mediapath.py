from django import template
from django.conf import settings
from django.db.models.fields.files import FieldFile

register = template.Library()


@register.simple_tag
@register.filter()
def mediapath(data: FieldFile) -> str:
    """
    Возвращает URL загруженного файла, если он существует, или символ '#', если файл не загружен
    Make url path to media

    Examples:
        <img src="{{ object.image|mediapath }}" />
        or
        <img src="{% mediapath object.image %}" />
    """
    return data.url if data else 'Нет фотографии'


@register.filter
def path_filter(text):
    return settings.MEDIA_URL + str(text)
