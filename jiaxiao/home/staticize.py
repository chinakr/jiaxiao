#-*- coding: utf-8 -*-

"""网站静态化"""

from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render
from jiaxiao.config import site_name, channels, theme

import os

class SiteStaticizeView(View):
    """网站静态化"""

    def get(self, request):
        """URL GET"""

        msg = self.staticize()
        return HttpResponse(msg)

    def get_all_pages(self):
        """获得所有需要静态化的页面"""

        page_name_list = []
        filenames = os.listdir('templates/%s/' % theme)
        for filename in filenames:
            if filename in ('layout.html', 'header.html', 'sidebar.html', 'footer.html', 'links.html'):    # 跳过页面布局文件
                continue
            if '.html' not in filename:    # 跳过目录
                continue
            if 'block_' in filename:    # 跳过页面嵌入模块
                continue
            page_name_list.append(filename)

        return page_name_list

    def staticize(self):
        """静态化所有页面"""

        msg = ''
        page_name_list = self.get_all_pages()
        for page_name in page_name_list:
            page = PageStaticize(page_name)
            page.staticize()
            msg += '<p>Page `%s` staticized.</p>\n' % page_name
        msg += '<p>%d pages staticied.</p>\n' % len(page_name_list)

        return '<!DOCTYPE html>\n<html>\n<head>\n<title>Page Staticizing</title>\n</head><body>%s</body>\n</html>' % msg


class PageStaticize(object):
    """页面静态化"""

    page_name = ''
    
    def __init__(self, page_name):
        self.page_name = page_name

    def staticize(self, output_dir='html'):
        pass