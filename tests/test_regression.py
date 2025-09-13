from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_functionality():
    driver = webdriver.Chrome()  # Make sure chromedriver is in PATH
    driver.get("https://example.com/login")

    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.ID, "loginBtn").click()

    assert "Welcome" in driver.page_source
    driver.quit()
