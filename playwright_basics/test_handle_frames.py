from playwright.sync_api import Page, expect


def test_iframe_handling(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    frame = page.frame_locator("#courses-iframe")
    frame.locator("[href='https://courses.rahulshettyacademy.com/courses']").nth(0).click()
    expect(frame.get_by_role("heading",name="Browse products")).to_contain_text("Browse products")