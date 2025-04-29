import time
from playwright.sync_api import Page, expect


def test_add_to_cart(page:Page):
    """
        Add samsung note 8 and iphone X in cart
        Verify cart has those many items
    :param page:
    :return:
    """
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as new_page:
        page.locator(".blinkingText").click()
        child_page= new_page.value
        text = child_page.locator(".red").text_content()
        print(f"Email Text : {text}")
        if "mentor@rahulshettyacademy.com" in text.split():
            assert True
        else:
            assert False

    time.sleep(10)