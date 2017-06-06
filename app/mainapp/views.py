from django.views import generic
from django.views.decorators.http import require_GET
from django.utils.decorators import method_decorator

# Create your views here.


@method_decorator(require_GET, name='dispatch')
class MainPage(generic.TemplateView):
    template_name = 'mainapp_templates/main_page.html'
