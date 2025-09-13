
# pages/home_page.py
class HomePage:
    def _init_(self, driver):
        self.driver = driver
        self.url = "https://example.com"

    def open(self):
        self.driver.get(self.url)

    def title(self):
        return self.driver.title