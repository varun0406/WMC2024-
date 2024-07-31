from django import template

register = template.Library()

@register.filter
def generate_range(value):
    """Generates a range of numbers from 0 to the given value."""
    return range(value)