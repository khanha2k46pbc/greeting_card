from django.views.generic import TemplateView
from django.shortcuts import render

def index_page_view(request):
    return render(request, 'main/index.html')


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'
