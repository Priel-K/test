from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

my_first_name = ""
my_last_name = "kasookar nisimi"


class Test_collectors:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_controllers.html")

    def teardown_class(cls):
        driver.quit()



