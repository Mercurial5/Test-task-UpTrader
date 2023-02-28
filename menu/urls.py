from django.urls import path
from menu import views

urlpatterns = [
    path('<int:item_id>', views.index, name='index'),
    path('', views.index, name='index'),
]
