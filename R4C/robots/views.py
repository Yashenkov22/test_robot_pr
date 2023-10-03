import os

from django.shortcuts import render
from django.http import  HttpResponse

from .services import make_excel_file


#Page with link to download excel file
def excel_link(request):
    return render(request, 'robots/download_excel.html')


def download_excel(_):

    make_excel_file()

    with open('excel_file.xlsx', 'rb') as f:
        response = HttpResponse(f, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="File.xlsx"'

    if os.path.exists('excel_file.xlsx'):
        os.remove('excel_file.xlsx')
    
    return response