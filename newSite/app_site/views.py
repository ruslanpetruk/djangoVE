from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self,request, **kwards):
        return render (request, 'index.html', context=None)
