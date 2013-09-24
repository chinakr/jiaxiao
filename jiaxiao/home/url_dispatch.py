#-*- coding: utf-8 -*-

"""URL映射"""

from django.views.generic.base import View
from django.http import HttpResponse

class URLDispatchView(View):
    """URL映射"""

    def get(self, request, page_name=''):
        """URL GET"""

        if page_name == '':
            page_name = 'index'
        return HttpResponse(page_name)