# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'template_tag': 'Template Tag on Help Page'}
    return render(request, "help/index.html", context)
