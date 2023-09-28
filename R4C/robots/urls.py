from django.urls import path

from .views import index, add_robot_record, download_excel

urlpatterns = [
    path('', index, name='home'),    
    path('create/', add_robot_record, name='add_robot'),
    path('excel/', download_excel, name='download_excel'),
]