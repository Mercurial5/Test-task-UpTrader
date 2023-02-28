from django.shortcuts import render
from menu import models
from django.shortcuts import get_object_or_404


def index(request, item_id: int = None):
    item = get_object_or_404(models.Item, pk=item_id) if item_id else None
    return render(request, 'menu/index.html', {'item': item})
