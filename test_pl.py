import re

import playwright
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import Page


class TestPlay:
    email = "Email"

    def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(self, page: Page) -> None:
        # browser = playwright.chromium.launch(headless=False)
        # context = browser.new_context()
        # page = context.new_page()
        page.goto("https://aimaidhelp.com/login")
        # a = page.video
        # print(type(a))
        page.get_by_placeholder("Email").fill("vburmich@apro.ai")
        page.get_by_placeholder("Email").press("Enter")
        page.get_by_placeholder("Password").click()
        a = page.get_by_placeholder("Password").count()
        print(a)
        page.get_by_placeholder("Password").fill("1111")
        page.get_by_role("button", name="Log In").click()

        b = page.get_by_role("heading", name="Property User Settings")
        expect(b).to_contain_text('Property User Settings!')


        # ---------------------
        # context.close()
        # browser.close()
