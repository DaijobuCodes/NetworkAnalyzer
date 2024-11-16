import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle
import os

COOKIES_FILE = "google_cookies.pkl"

def save_cookies(driver, cookies_file):
    """Save cookies to a file."""
    with open(cookies_file, 'wb') as f:
        pickle.dump(driver.get_cookies(), f)
    print("Cookies saved.")

def load_cookies(driver, cookies_file):
    """Load cookies from a file."""
    if os.path.exists(cookies_file):
        with open(cookies_file, 'rb') as f:
            cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        print("Cookies loaded.")
    else:
        print("No cookies file found. Manual login required.")

def login_to_google(driver):
    """Automates login to Google."""
    print("Automating Google login...")
    driver.get("https://accounts.google.com/signin")
    time.sleep(2)

    # Input email
    email_field = driver.find_element(By.ID, "identifierId")
    email_field.send_keys("yashshravu2005@gmail.com")  # Replace with your email
    email_field.send_keys(Keys.RETURN)
    time.sleep(3)

    # Input password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("f@mily2435")  # Replace with your password
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)

    print("Login completed.")

def upload_to_google_maps(kml_file_path):
    """Automates uploading the KML file to Google My Maps."""
    print("Starting Selenium automation for Google My Maps upload...")
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.google.com/maps/d/")
        time.sleep(3)  # Allow the page to load

        # Load cookies if available
        load_cookies(driver, COOKIES_FILE)

        # Refresh to apply cookies
        driver.refresh()
        time.sleep(3)

        # Check if logged in
        if "Sign in" in driver.page_source:
            print("Not logged in. Attempting automated login...")
            login_to_google(driver)
            save_cookies(driver, COOKIES_FILE)
            driver.refresh()
            time.sleep(3)

        # Create a new map
        create_map_button = driver.find_element(By.LINK_TEXT, "Create a new map")
        create_map_button.click()
        time.sleep(3)

        # Import the KML file
        import_button = driver.find_element(By.XPATH, '//div[contains(text(), "Import")]')
        import_button.click()
        time.sleep(2)

        # Upload the KML file
        file_input = driver.find_element(By.XPATH, '//input[@type="file"]')
        file_input.send_keys(kml_file_path)
        time.sleep(5)  # Wait for the upload to complete
        print("KML file successfully uploaded to Google My Maps.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()



