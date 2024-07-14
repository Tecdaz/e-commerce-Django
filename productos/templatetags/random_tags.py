from random import randint
from django import template

register = template.Library()


@register.simple_tag
def random_number():
    return randint(20_000, 100_000)
