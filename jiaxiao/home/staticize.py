#-*- coding: utf-8 -*-

"""网站静态化"""

from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render
from jiaxiao.config import site_name, channels, theme

import os
import shutil

class SiteStaticizeView(View):
    """网站静态化"""

    request = None

    def get(self, request):
        """URL GET"""

        self.request = request
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
            page = PageStaticize(self.request, page_name)
            page.staticize()
            msg += '<p>Page `%s` staticized.</p>\n' % page_name
        msg += '<p>%d pages staticied.</p>\n' % len(page_name_list)

        # 拷贝静态文件(CSS、JS、图片)
        try:
            shutil.rmtree('html/static/')
        except:
            pass
        shutil.copytree('templates/static/', 'html/static/')
        os.system('cp -r templates/%s/static/ html/' % theme)

        return '<!DOCTYPE html>\n<html>\n<head>\n<title>Page Staticizing</title>\n</head><body>%s</body>\n</html>' % msg


class PageStaticize(object):
    """页面静态化

    为了支持模板布局文件，需要使用`render()`，也就需要`request`。
    """

    page_name = ''
    request = None
    
    def __init__(self, request, page_name):
        self.request = request
        self.page_name = page_name

    def staticize(self, output_dir='html'):
        # 生成HTML文件
        template_name = '%s/%s' % (theme, self.page_name)
        html = render(self.request, template_name, {
            'site_name': site_name,
            'channels': channels,
        })
        f = open('%s/%s' % (output_dir, self.page_name), 'w')
        print >> f, html.content.strip().replace('/static/', 'static/').replace('/"', '.html"').replace('"/', '"').replace('".html', '"index.html')
        f.close()
