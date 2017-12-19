# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'my_content': 'Hello, Im from view.py'
	}
	return render(request, "home/index.html", context)
