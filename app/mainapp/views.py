from django.shortcuts import render

# Create your views here.

def main_page(request):
    return render(request, 'mainapp_templates/main_page.html')