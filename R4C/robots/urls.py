from django.urls import path

from .views import add_robot_record

urlpatterns = [
    path('add/', add_robot_record, name='add_robot')
]