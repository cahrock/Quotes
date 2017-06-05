# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Quotes, Favorites, QuoteManager
from ..login_app.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count


# Create your views here.
def quotes(request):

    q = set(Quotes.objects.all())
    u = set(Quotes.objects.filter(quote_fav__user__email=request.session['loggedin_user']))
    allquotes = q.difference(u)

    context = {
        # 'items': Quotes.objects.all().order_by('-created_at'),
        'items': allquotes,
        'itemsfav': Quotes.objects.filter(quote_fav__user_id__email = request.session['loggedin_user']),
        }
    return render(request, 'exam_app/quotes.html', context)

def addquotes(request):
    session = request.session['loggedin_user']
    addquotes = Quotes.objects.addquotes(request.POST, session)

    if addquotes[0]:
        return redirect('/exam_app/quotes')
    else:
        for i in addquotes[1]:
            messages.info(request,i)
            return redirect('/exam_app/quotes')

def addfav(request, id):
    user_ = User.objects.filter(email = request.session['loggedin_user'])
    quotes_ = Quotes.objects.filter(id= id)
    add_fav = Favorites.objects.create(user = user_[0], message= quotes_[0])
    return redirect('/exam_app/quotes')

def removefav(request, id):
    Favorites.objects.filter(message__id = id).filter(user__email = request.session['loggedin_user']).delete()
    return redirect('/exam_app/quotes')

def profile(request, id):
    return render(request, 'exam_app/profile.html',{
        'user': User.objects.filter(id = id),
        'items': Quotes.objects.filter(posted_by_id = id),
        'count': Quotes.objects.filter(posted_by_id = id).count()
    })

def logout(request):
    request.session.clear()
    return redirect('/')
