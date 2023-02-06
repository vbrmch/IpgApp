from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://aimaidhelp.com/login")
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("vburmich@apro.ai")
    page.get_by_placeholder("Email").press("Enter")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("1111")
    page.get_by_role("button", name="Log In").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
