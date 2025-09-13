<<<<<<< HEAD
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def chrome_options():
    opts = Options()
    opts.add_argument("--headless=new")  # for headless CI run; remove if you want visible browser
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    return opts

@pytest.fixture(scope="function")
def driver(chrome_options):
    service = ChromeService()  # will auto-find chromedriver in PATH
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
=======
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def chrome_options():
    opts = Options()
    opts.add_argument("--headless=new")  # for headless CI run; remove if you want visible browser
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    return opts

@pytest.fixture(scope="function")
def driver(chrome_options):
    service = ChromeService()  # will auto-find chromedriver in PATH
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
>>>>>>> 57f9d72 (Initial commit : pytest + selenium sample)
    driver.quit()