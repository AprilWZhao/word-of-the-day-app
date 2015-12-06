from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Language(models.Model):
    language_text = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s'%self.language_text

class Word(models.Model):
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    word_text = models.CharField(max_length=50)
    pronunciation = models.CharField(max_length=50, blank=True)
    part_of_speech1 = models.CharField(max_length=10, blank=True)
    meaning1 = models.TextField(blank=True)
    sentence1 = models.TextField(blank=True)
    part_of_speech2 = models.CharField(max_length=10, blank=True)
    meaning2 = models.TextField(blank=True)
    sentence2 = models.TextField(blank=True)
    part_of_speech3 = models.CharField(max_length=10, blank=True)
    meaning3 = models.TextField(blank=True)
    sentence3 = models.TextField(blank=True)
    created_by = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created']

    def __unicode__(self):
        return u'%s'%self.word_text

class Comment(models.Model):
    body = models.TextField(blank=True)
    word_id = models.ForeignKey(Word, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User,default='guest')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s'%self.body

