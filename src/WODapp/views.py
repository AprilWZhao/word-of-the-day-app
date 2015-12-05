from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class TodaysWordView(TemplateView):
    template_name = 'todays_word.html'