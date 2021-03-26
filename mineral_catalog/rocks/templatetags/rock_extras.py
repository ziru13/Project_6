import string

from django import template

register = template.Library()


@register.simple_tag
def rock_letter():
    letters = '  '.join(string.ascii_uppercase)
    return letters
