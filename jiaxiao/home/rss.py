#-*- coding: utf-8 -*-

"""RSS订阅"""

from django.views.generic.base import View
from django.http import HttpResponse

class RSSView(View):
    """RSS订阅"""

    def get(self, request):
        """URL GET"""

        return HttpResponse('RSS feed')
