import argparse

import allure
from playwright.sync_api import Page, Response
import pytest

import conftest


# def parse_args():
#     """
#     Parse arguments given in the command line. Expects just "--db"
#     """
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--name1', required=True, type=str, help="Your DB name")
#     return parser.parse_args()


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def visit(self, ) -> Response or None:
        with allure.step(f'Opening the url "{self.page.url}"'):
            return self.page.goto("/login", wait_until='networkidle')

    def reload(self) -> Response or None:
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            return self.page.reload(wait_until='domcontentloaded')
