#-*- coding: utf-8 -*-

"""URL映射"""

from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render

class URLDispatchView(View):
    """URL映射"""

    def get(self, request, page_name=''):
        """URL GET"""

        if page_name == '':
            #page_name = 'index'
            return render(request, 'default/index.html')
        return HttpResponse(page_name)