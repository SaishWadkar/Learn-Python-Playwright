from playwright.sync_api import Page

def test_web_tables(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

