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
    page.set_viewport_size({"width":1366,"height":768})
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("stud")
    page.get_by_role("button",name="Sign In").click()

    iphone_element = page.locator("app-card").filter(has_text="iphone X") # filter on the list of web elements
    iphone_element.get_by_role("button").click()

    samsung_element = page.locator("app-card").filter(has_text="Samsung Note 8")  # filter on the list of web elements
    samsung_element.get_by_role("button").click()

    page.get_by_text("checkout").click()

    expect(page.locator(".media-body")).to_have_count(2)

    time.sleep(5)

