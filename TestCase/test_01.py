import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

class TestHomework01:

    @pytest.fixture()
    def setup_class(cls):
       global driver
       driver = webdriver.Chrome(ChromeDriverManager().install())
       driver.maximize_window()
       driver.get("https://www.imdb.com/")
       yield

    def teardown_class(cls):
       driver.quit()


    def test_001(self, setup_class):
      driver.refresh()
      title= driver.title
      url= driver.current_url
      if title == "IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows":
          print("title pass")
      else:
          print("title false")

      if url == "https://www.pmdb.com/":
          print("ok")
      else:
          print("no")





