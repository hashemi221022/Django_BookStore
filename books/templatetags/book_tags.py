from django import template

register = template.Library()

@register.filter(name='kocholo')
def to_lowercase(value):
    return value.lower()

#! mishe az tabe ba do vorodi mesle shekle zir estefade kard
@register.filter(name='bozorg')
def to_upper(value, arg):
    return f'{arg} : {value.upper()}'
