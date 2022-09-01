from atexit import register
from django import template

register = template.Library()

@register.filter(name='rank_and_name')
def rank_name(value):
    if value<=1500:
        return str(value) + " " + "(Neophyte)"
    elif value<=1750:
        return str(value) + " " + "(Padawan)"
    elif value<=2000:
        return str(value) + " " + "(Amateur)"
    elif value<=2250:
        return str(value) + " " + "(Skilled)"
    elif value<=2500:
        return str(value) + " " + "(Pro)"
    elif value<=2750:
        return str(value) + " " + "(Master)"
    else:
        return str(value) + " " + "(Champion)"


@register.filter(name='rank_to_name')
def rank_to_name(value):
    if value<=1500:
        return "neophyte"
    elif value<=1750:
        return "padawan"
    elif value<=2000:
        return "amateur"
    elif value<=2250:
        return "skilled"
    elif value<=2500:
        return "pro"
    elif value<=2750:
        return "master"
    else:
        return "champion"