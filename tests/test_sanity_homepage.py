# tests/test_sanity_homepage.py
from pages.home_page import HomePage
#mid sem test commit 

def test_homepage_title(driver):
    home = HomePage(driver)
    home.open()
    assert "Example Domain" in home.title()
