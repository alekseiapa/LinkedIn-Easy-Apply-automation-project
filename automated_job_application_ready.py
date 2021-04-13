
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time

path = "/path"

driver = webdriver.Chrome(path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2438155721&f_AL=true&f_L=Australia&geoId=101452733&keywords=junior%20developer&location=Australia")

try:
    sign_in_link = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
    )
    sign_in_link.click()
    time.sleep(2)
    try:
        email_entry = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_entry = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        email_entry.send_keys("email")

        password_entry.send_keys("password")

        sign_in_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn__primary--large.from__button--floating"))
        )
        sign_in_button.click()

    except TimeoutException:
        email_entry = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-email"))
        )
        password_entry = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-password"))
        )
        email_entry.send_keys("email")

        password_entry.send_keys("password")

        sign_in_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-submit"))
        )
        sign_in_button.click()

    time.sleep(15)
    print("Timer 1 finished")
    part_jobs_list = driver.find_elements_by_css_selector(".full-width.artdeco-entity-lockup__title.ember-view a")
    first_job = part_jobs_list[3]
    first_job.click()
    time.sleep(3)
    print("Timer 2 finished")
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    time.sleep(3)
    print("Timer 3 finished")
    all_jobs_list = driver.find_elements_by_css_selector(".full-width.artdeco-entity-lockup__title.ember-view a")
    print("List created")
    for job in all_jobs_list:

        print(job.text)
        job.click()
        time.sleep(2)
        try:
            apply_button = driver.find_element_by_css_selector(".jobs-apply-button--top-card button")
            apply_button.click()
            time.sleep(1)
            submit_button = driver.find_element_by_css_selector("footer button")
            time.sleep(1)
            if submit_button.text == "Submit application":
                submit_button.click()
                time.sleep(1)
                close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss.artdeco-button.artdeco-button--circle.artdeco-button--muted.artdeco-button--2.artdeco-button--tertiary.ember-view")
                close_button.click()
                print("Clicked")

            else:
                close_button = driver.find_element_by_class_name("artdeco-button__icon")
                close_button.click()
                time.sleep(1)

                discard_button = driver.find_element_by_css_selector(".artdeco-modal__confirm-dialog-btn.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
                discard_button.click()
                print("Passed")
        except NoSuchElementException:
            print("No application button, skipped.")
            continue

finally:
    time.sleep(2)
