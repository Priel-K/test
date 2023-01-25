import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class TestSemple1:

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://www.google.com")
        yield
        driver.quit()



    def test_demo1(self,test_setup):
        print("the driver is:", driver.title)
        print("the url is:", driver.current_url)


