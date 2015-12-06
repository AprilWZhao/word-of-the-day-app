from django.forms import ModelForm
from .models import Comment
from django.utils.translation import ugettext as _


class AddCommentForm(ModelForm):
    """
    This Form Creates a comment
    """

    class Meta:
        model = Comment
        fields = ["body"]
        help_texts = {
            'Comment': _('Comment on this word here!'),
        }