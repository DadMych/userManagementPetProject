from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create),
    path('save/<int:id>', views.save),
    path('delete/<int:id>', views.delete),
    path('retrieve/<int:id>', views.retrieve)
]
