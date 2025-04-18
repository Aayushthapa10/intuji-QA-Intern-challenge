from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class PracticeFormPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.XPATH, "//label[text()='Male']")
    GENDER_FEMALE = (By.XPATH, "//label[text()='Female']")
    GENDER_OTHER = (By.XPATH, "//label[text()='Other']")
    MOBILE = (By.ID, "userNumber")
    DATE_INPUT = (By.ID, "dateOfBirthInput")
    SUBJECTS = (By.ID, "subjectsInput")
    HOBBY_SPORTS = (By.XPATH, "//label[text()='Sports']")
    HOBBY_READING = (By.XPATH, "//label[text()='Reading']")
    PICTURE_UPLOAD = (By.ID, "uploadPicture")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    SUBMIT = (By.ID, "submit")

    def open(self):
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.execute_script("document.getElementById('fixedban').style.display='none'")
        self.driver.execute_script("document.getElementById('adplus-anchor').style.display='none'")

    def enter_first_name(self, name):
        self.driver.find_element(*self.FIRST_NAME).send_keys(name)

    def enter_last_name(self, name):
        self.driver.find_element(*self.LAST_NAME).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def select_gender(self, gender="Male"):
        if gender == "Male":
            self.driver.find_element(*self.GENDER_MALE).click()
        elif gender == "Female":
            self.driver.find_element(*self.GENDER_FEMALE).click()
        elif gender == "Other":
            self.driver.find_element(*self.GENDER_OTHER).click()

    def enter_mobile(self, mobile):
        self.driver.find_element(*self.MOBILE).send_keys(mobile)

    def enter_subjects(self, subject):
        input_field = self.driver.find_element(*self.SUBJECTS)
        input_field.send_keys(subject)
        input_field.send_keys(Keys.ENTER)

    def select_hobby(self):
        self.driver.find_element(*self.HOBBY_SPORTS).click()

    def upload_picture(self, file_path):
        self.driver.find_element(*self.PICTURE_UPLOAD).send_keys(file_path)

    def enter_address(self, address):
        self.driver.find_element(*self.CURRENT_ADDRESS).send_keys(address)

    def submit_form(self):
        submit_btn = self.driver.find_element(*self.SUBMIT)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        time.sleep(1)
        submit_btn.click()
