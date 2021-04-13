
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

path = "/path"
driver = webdriver.Chrome(path)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=101452733&keywords=python%20engineer&location=Australia")

time.sleep(20)
sign_in_link = driver.find_element_by_link_text("Sign in")
sign_in_link.click()
try:
    email_entry = driver.find_element_by_id("username")
    password_entry = driver.find_element_by_id("password")
    email_entry.send_keys("email_entry")
    password_entry.send_keys("password")
    sign_in_button = driver.find_element_by_css_selector(".btn__primary--large.from__button--floating")
    sign_in_button.click()
except:
    email_entry = driver.find_element_by_id("login-email")
    password_entry = driver.find_element_by_id("login-password")
    email_entry.send_keys("email_entry")
    password_entry.send_keys("password")
    sign_in_button = driver.find_element_by_id("login-submit")
    sign_in_button.click()

easy_apply_button = driver.find_element_by_id()


easy_apply_button = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, "ember204"))
    )
easy_apply_button.click()
phone_number_entry = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2446122843,20781683,phoneNumber~nationalNumber)"))
)
phone_number_entry.clear()
phone_number_entry.send_keys("phone_number_entry")
next_button1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view"))
)
next_button1.click()
next_button2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view"))
)
next_button2.click()
