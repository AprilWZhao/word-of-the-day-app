from django.contrib import admin

# Register your models here.
from .models import Language
from .models import Word
from .models import Comment

admin.site.register(Word)
admin.site.register(Language)
admin.site.register(Comment)