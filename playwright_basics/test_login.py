import time
from os import times

from playwright.sync_api import Page

def test_login_to_rahul_shetty_site(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.set_viewport_size({"width":1366,"height":768})
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("stud")
    page.get_by_role("button",name="Sign In").click()
    time.sleep(3)