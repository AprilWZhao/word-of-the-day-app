from django.views.generic import TemplateView
from models import Word
from forms import AddCommentForm


# Create your views here.
class TodaysWordView(TemplateView):
    template_name = 'todays_word.html'
    form_class = AddCommentForm

    def get_context_data(self, **kwargs):
        context = super(TodaysWordView, self).get_context_data(**kwargs)
        context['english_words'] = Word.objects.filter(language_id__language_text="English")
        context['japanese_words'] = Word.objects.filter(language_id__language_text="Japanese")
