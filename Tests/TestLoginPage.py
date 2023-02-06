import time
import pytest_base_url as base_u

import pytest
import pytest_base_url.plugin

from playwright.sync_api import Page
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage


class TestLoginPage:
    def test_login(self, page: Page):
        login_page = LoginPage(page)
        login_page.visit()
        login_page.login(email='smit71257@gmail.com', password='1111')
        time.sleep(23)
