import time

from playwright.sync_api import Page, expect


def test_other_locators_web_elements(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.locator("#hide-textbox").click()
    time.sleep(2)
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(2)