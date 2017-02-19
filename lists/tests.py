import re

from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from .views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('lists/home.html')
        source_html = response.content.decode()
        result = re.sub(r'<input\stype=\'hidden\'\sname=\'csrfmiddlewaretoken\'\svalue=\'\w+\'\s/>', '', source_html, 1)
        # print(result)
        self.assertEqual(result, expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'

        response = home_page(request)

        self.assertIn('신규 작업 아이템', response.content.decode())
        expected_html = render_to_string(
            'lists/home.html',
            {'new_item_text': '신규 작업 아이템'}
        )
        source_html = response.content.decode()
        result = re.sub(r'<input\stype=\'hidden\'\sname=\'csrfmiddlewaretoken\'\svalue=\'\w+\'\s/>', '', source_html, 1)
        self.assertEqual(result, expected_html)
