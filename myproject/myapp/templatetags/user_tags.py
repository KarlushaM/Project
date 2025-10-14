
from django import template

register = template.Library()

@register.filter
def in_group(user, group_name):
    """Проверяет, состоит ли пользователь в группе"""
    return user.groups.filter(name=group_name).exists()