from django.db import models


class Item(models.Model):
    """
    Item - one piece in the menu.

    Naming: I decided to name the model `Item`, because in menu you can have drinks, food, something sweat to eat,
    something sweat to drink...

    Item can have parent and children.
    """
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField()
    parent = models.ForeignKey('Item', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name
