import pytest

from playwright.sync_api import Page

@pytest.mark.skip
def test_open_browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")

def test_openB_browser_1(page:Page):
    page.goto("https://www.facebook.com")