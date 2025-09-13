import requests

def test_homepage_up():
    response = requests.get("https://example.com")
    assert response.status_code == 200

def test_login_page_loads():
    response = requests.get("https://example.com/login")
    assert "Login" in response.text
