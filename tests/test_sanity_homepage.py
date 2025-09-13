# tests/test_sanity_homepage.py
# testing for pushing changes
from pages.home_page import HomePage

def test_homepage_title(driver):
    home = HomePage(driver)
    home.open()
    assert "Example Domain" in home.title()