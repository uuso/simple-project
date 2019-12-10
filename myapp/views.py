from django.shortcuts           import render
from myapp.models               import Dummy

from django.views.generic.base  import TemplateView
from django.views.generic       import ListView


class DummyTemplateView(TemplateView):
    # указываем имя используемого шаблона
    template_name = "home.html"

    # для формирования словаря параметров мы переопределяем метод get_context_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Dummy.objects.all()
        return context

class DummyListView(ListView):
    model = Dummy