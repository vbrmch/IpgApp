import sys

import pytest
from playwright.sync_api import sync_playwright, Page
from pytest_playwright.pytest_playwright import browser_context_args
from pytest_playwright.pytest_playwright import BrowserType


# @pytest.fixture
# def browser_fixture():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         yield page
#         page.close()
#         browser.close()


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="default name")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")




# def pytest_generate_tests(metafunc):
#     # This is called for every test. Only get/set command line arguments
#     # if the argument is specified in the list of test "fixturenames".
#     option_value = metafunc.config.option.url2
#     if 'url2' in metafunc.fixturenames and option_value is not None:
#         metafunc.parametrize("url2", [option_value])


# def pytest_addoption(parser):
#     parser.addoption("--url1", action="store")
#
#
# # @pytest.fixture(scope='session')
# def url1(request):
#     url_value = request.config.option.url1
#     if url_value is None:
#         pytest.skip(msg="Please enter URL")
#     return "https://" + url_value

# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#
#         "viewport": {
#             "width": 1920,
#             "height": 1080,
#         }
#     }
#
# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     response = authenticate(user)
#     return {
#         **browser_context_args
#         "storage_state": {
#             "cookies": [
#                 {
#                     "name": "token",
#                     "value": "sd4fFfv!x_cfc",
#                 },
#             ]
#         },
#     }
