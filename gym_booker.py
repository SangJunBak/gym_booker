import time
import warnings
import os
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

warnings.filterwarnings("ignore", category=DeprecationWarning)

# Choose which gym you want
GYM = "PAC Fitness Centre"  # GYM = "CIF Fitness Centre"

# Duo 2FA Credentials
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

# Get this by requesting codes to your phone
DUO_CODES = [
    "1749063",
      "2661741",
        "3417386",
          "4729370",
            "5999896",
              "6655660",
                "7996593",
                  "8117851",
                    "9825361",
                      "0363351",
]

POLL_TIME_MINUTES = 10

WEBDRIVER_PATH = '/usr/local/bin/chromedriver'

# Formatting matters so keep it consistent with 
WANTED_TIMES = [
    {
        "day": "Mon",
        "times": [],
    },
    {
        "day": "Tue",
        "times": [],
    },
    {
        "day": "Wed",
        "times": [],
    },
    {
        "day": "Thu",
        "times": ["1 - 1:50 PM", "2 - 2:50 PM", "3 - 3:50 PM", "4 - 4:50 PM"],
    },
    {
        "day": "Fri",
        "times": ["1 - 1:50 PM", "2 - 2:50 PM", "3 - 3:50 PM", "4 - 4:50 PM"],
    },
    {
        "day": "Sat",
        "times": ["1 - 1:50 PM", "2 - 2:50 PM", "3 - 3:50 PM", "4 - 4:50 PM"],
    },
    {
        "day": "Sun",
        "times": ["1 - 1:50 PM", "2 - 2:50 PM", "3 - 3:50 PM", "4 - 4:50 PM"],
    },
]


driver = webdriver.Chrome(WEBDRIVER_PATH)

driver.get('https://warrior.uwaterloo.ca/booking')

time.sleep(1)  # Let the user actually see something!


pac_booking_button = driver.find_element_by_link_text('PAC Fitness Centre')
pac_booking_button.click()

time.sleep(2) 

login_button = driver.find_element_by_css_selector(
    "button[title='WATIAM USERS']")

# Log in via Duo 2FA
if(login_button):
    login_button.click()
    time.sleep(2)
    user_name_field = driver.find_element_by_id("userNameInput")
    user_name_field.send_keys(USERNAME)
    user_name_field.submit()
    time.sleep(1)

    password_field = driver.find_element_by_id("passwordInput")
    password_field.send_keys(PASSWORD)
    password_field.submit()
    time.sleep(1)

    # Change focus to the duo mobile IFrame to access its DOM
    driver.switch_to.frame("duo_iframe")
    time.sleep(1)

    passcode_button = driver.find_element_by_id(
        "passcode")
    passcode_button.click()

    duo_code_message = driver.find_element_by_class_name(
        "next-passcode-msg").get_attribute("innerText")

    passcode_field = driver.find_element_by_class_name("passcode-input")

    valid_duo_code = None
    for code in DUO_CODES:
        if code[0] == duo_code_message[-1]:
            valid_duo_code = code

    passcode_field.send_keys(valid_duo_code)
    time.sleep(2)

    passcode_button.click()
    time.sleep(2)

    pac_booking_button = driver.find_element_by_link_text('PAC Fitness Centre')
    pac_booking_button.click()

time.sleep(2)

# Check every POLL_TIME_MINUTES for booking availability
while True:
    for event in WANTED_TIMES:
        times = event["times"]
        day = event["day"]

        if len(times) == 0:
            continue

        date_buttons = driver.find_elements_by_xpath(
            '//span[text()="'+day+'"]/..')

        if len(date_buttons) == 0:
            print(day + " not available / already booked")
            continue

        date_button = date_buttons[1]

        # Scroll to the date buttons
        driver.execute_script("window.scrollTo(0,0);")
        time.sleep(1)

        date_button.click()
        time.sleep(1)

        print("Looking for times on "+day+"...")

        for event_time in times:
            book_buttons = driver.find_elements_by_css_selector(
                "button[data-slot-text='"+event_time+"']")

            if len(book_buttons) == 0:
                print(event_time+" not available")
                continue

            print("Time is available. Booking now.")
            book_button = book_buttons[0]
            book_button.click()
            print(event_time+" for "+day+" booked")
            time.sleep(2)
            break

        driver.refresh()  # So that captcha resets

        time.sleep(1)

    time.sleep(POLL_TIME_MINUTES * 60)


# driver.quit()
