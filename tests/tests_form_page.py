import time
from utils.base_driver import BaseDriver
from pages.form_page import PracticeFormPage


def setup():
    driver = BaseDriver().start_browser()
    page = PracticeFormPage(driver)
    page.open()
    return driver, page


def test_tc_01_empty_fields():
    driver, page = setup()
    page.submit_form()
    time.sleep(2)
    driver.quit()


def test_tc_02_valid_data():
    driver, page = setup()
    page.enter_first_name("Aayush")
    page.enter_last_name("Thapa")
    page.enter_email("aayush@test.com")
    page.select_gender("Male")
    page.enter_mobile("9876543210")
    page.enter_subjects("Maths")
    page.select_hobby()
    page.upload_picture("C:/Users/User/Downloads/sample img.png")
    page.enter_address("Kathmandu")
    page.submit_form()
    time.sleep(2)
    driver.quit()
