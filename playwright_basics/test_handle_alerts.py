import time

import pytest
from playwright.sync_api import Page

@pytest.mark.skip
def test_handle_alerts(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # breakpoint()
    time.sleep(5)
    button = page.locator("#confirmbtn")
    button.highlight()
    button.scroll_into_view_if_needed()
    button.click(force=True)
    # breakpoint()
    time.sleep(5)

def test_handle_alerts(page:Page):
    page.goto("https://selectorshub.com/xpath-practice-page/")
    # breakpoint()

    # page.get_by_text("Consider a small Donation and support this page.").click()

    page.on("dialog",lambda dialog:dialog.accept())

    page.locator("//*[@id='content']/div/div[1]/section[2]/div/div[2]/div/div[1]/div/button[1]").click(force=True)
    # page.get_by_text("Click To Open Window Alert").click()
    # page.locator("#myBtn").click()
    # button.highlight()
    # button.scroll_into_view_if_needed()
    # button.click()
    # breakpoint()
    page.wait_for_timeout(5000)

