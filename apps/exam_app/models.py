# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models

# Create your models here.

class QuoteManager(models.Manager):

    def addquotes(self, data, session):
        flag = True
        error = []
        if len(data['quotedby']) < 1:
            flag = False
            error.append('Please insert the author name')

        if len(data['addquotes']) < 1:
            flag = False
            error.append('Please quotes can not be blank')

        if flag:
            user = User.objects.filter(email= session)
            quotes_ = self.create(posted_by= user[0], quote = data['addquotes'], quoted_by = data['quotedby'])
            return (True, quotes_)
        else:
            return (False, error)

class Quotes(models.Model):
    # posted_by = models.CharField(max_length=100)
    posted_by = models.ForeignKey(User, related_name='postedby')
    quoted_by = models.CharField(max_length=45)
    quote = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = QuoteManager()

class Favorites(models.Model):
    user = models.ForeignKey(User, related_name="user_fav")
    message = models.ForeignKey(Quotes, related_name="quote_fav")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
