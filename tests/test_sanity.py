import requests

def test_homepage_up():
    response = requests.get("https://example.com")
    assert response.status_code == 200

def test_login_page_loads():
    response = requests.get("https://example.com/login")
    assert "Login" in response.text

# Test 1: Application/API is up
def test_app_running():
    response = requests.get("http://localhost:5000/health")  # sample health endpoint
    assert response.status_code == 200

# Test 2: Login works with valid credentials
def test_login_valid():
    payload = {"username": "admin", "password": "admin123"}
    response = requests.post("http://localhost:5000/login", json=payload)
    assert response.status_code == 200
    assert "token" in response.json()

# Test 3: Invalid login shows error
def test_login_invalid():
    payload = {"username": "fakeuser", "password": "wrongpass"}
    response = requests.post("http://localhost:5000/login", json=payload)
    assert response.status_code == 401
