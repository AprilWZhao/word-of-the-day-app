from django.shortcuts import render
from django.views.generic import TemplateView
from models import Word

# Create your views here.
class TodaysWordView(TemplateView):
    template_name = 'todays_word.html'
    word_list = Word