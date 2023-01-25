from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Test_LocatorsBasic:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("http://selenium.dev/")

    def teardown_class(cls):
        driver.quit()

    def test_verify_locators_basic(self):
        print(driver.find_element(By.CLASS_NAME, "navbar-brand"))
        print(driver.find_element(By.CLASS_NAME, "navbar-logo"))
        print(driver.find_element(By.ID, "selenium_logo"))
        print(driver.find_element(By.TAG_NAME, "svg"))
        print(driver.find_elements(By.TAG_NAME, "svg")[0])

        links = driver.find_elements(By.TAG_NAME, "a")
        Selenium_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Selenium")
        selenium_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "selenium")
        print("Number of total links in page: " + str(len(links)))
        print("Number of links in page with word: Selenium is: " + str(len(Selenium_links)))
        print("Number of links in page with word: selenium is: " + str(len(selenium_links)))


class Test_Wikipedia:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("http://wikipedia.org/")

    def teardown_class(cls):
        driver.quit()

    def test_verify_locators_basic(self):
        main_logo = driver.find_element(By.CLASS_NAME, "central-featured-logo")
        search_field = driver.find_element(By.ID, "searchInput")
        select_language = driver.find_element(By.ID, "searchLanguage")
        footer_sidebar = driver.find_element(By.CLASS_NAME, "footer-sidebar-content")
        wiki_elements = [main_logo, search_field, select_language, footer_sidebar]

        for wiki in reversed(wiki_elements):
            print(wiki)
