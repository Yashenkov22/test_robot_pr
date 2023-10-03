from django.urls import path

from .views import excel_link, download_excel


urlpatterns = [
    path('', excel_link, name='excel_link'),    
    path('download_excel/', download_excel, name='download_excel'),
]