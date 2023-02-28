from django import template

from menu import models

register = template.Library()


@register.inclusion_tag('menu/items.html')
def show_items(item: models.Item = None) -> dict:
    children = models.Item.objects.filter(parent=item).all()
    return {'item': item, 'children': children}
