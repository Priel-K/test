import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import xml.etree.ElementTree as ET


def get_data(node_name):
    root = ET.parse('C:/AutomationPython/SeleniumPythonDigital/TestCase/config.xml').getroot()
    return root.find(".//" + node_name).text


class Test_ExternalFiles:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(get_data("Url"))

    def teardown_class(cls):
        driver.quit()

    def test_external_files(self):
        driver.find_element_by_id("weight").send_keys(get_data("Weight"))
        driver.find_element_by_name("height").send_keys(get_data("Height"))
        driver.find_element_by_id("calculate_data").click()
        expected_result = get_data("ExpectedResultBMI")
        actual_result = driver.find_element_by_id("bmi_result").get_attribute("value")
        assert expected_result == actual_result


