import playwright
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import Page
from requests import request

import conftest
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.email_field = page.locator('//input[@id="email"]')
        self.password_field = page.locator('//input[@id="password"]')

    def login(self, email: str, password: str):
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.password_field.input_value()
