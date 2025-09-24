from selenium import webdriver
from selenium.webdriver.common.by import By

import requests

def test_login_functionality():
    driver = webdriver.Chrome()  # Make sure chromedriver is in PATH
    driver.get("https://example.com/login")

    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.ID, "loginBtn").click()

    assert "Welcome" in driver.page_source
    driver.quit()

# Test 1: User creation
def test_create_user():
    payload = {"username": "newuser", "email": "user@example.com"}
    response = requests.post("http://localhost:5000/users", json=payload)
    assert response.status_code == 201

# Test 2: Get user details
def test_get_user():
    response = requests.get("http://localhost:5000/users/newuser")
    assert response.status_code == 200
    assert response.json()["username"] == "newuser"

# Test 3: Update user details
def test_update_user():
    payload = {"email": "updated@example.com"}
    response = requests.put("http://localhost:5000/users/newuser", json=payload)
    assert response.status_code == 200

# Test 4: Delete user
def test_delete_user():
    response = requests.delete("http://localhost:5000/users/newuser")
    assert response.status_code == 200

# Test 5: Invalid API endpoint returns 404
def test_invalid_endpoint():
    response = requests.get("http://localhost:5000/invalid")
    assert response.status_code == 404



