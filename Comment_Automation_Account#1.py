from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# replace with your Instagram login details
my_username = "daily__tech.news"
my_password = "MyinstaB.com"

# replace with the Instagram post URL you want to comment on
post_url = "https://www.instagram.com/p/Crh1ypTsmCs/"

# initialize the webdriver
browser = webdriver.Chrome("/chromedriver")

# Authorization:
def auth(username, password):
    try:
        browser.get("https://instagram.com")
        time.sleep(random.randrange(2, 4))

        input_username = browser.find_element_by_name("username")
        input_password = browser.find_element_by_name("password")

        input_username.send_keys(username)
        time.sleep(random.randrange(1, 2))
        input_password.send_keys(password)
        time.sleep(random.randrange(1, 2))
        input_password.send_keys(Keys.ENTER)
        time.sleep(random.randrange(3, 5))

        # Check if 2-step verification is enabled
        try:
            input_two_factor_code = browser.find_element_by_name("verificationCode")
            two_factor_code = input("Please enter your 2-step verification code: ")
            input_two_factor_code.send_keys(two_factor_code)
            input_two_factor_code.send_keys(Keys.ENTER)
            time.sleep(random.randrange(3, 5))
        except:
            pass

    except Exception as err:
        print(err)
        browser.quit()

# function to comment on a post
def comment_on_post(post_url, comment_text):
    try:
        browser.get(post_url)
        time.sleep(5)

        comment_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[aria-label='Add a comment…']"))
        )

        comment_input.send_keys(random.choice(comment_text))
        time.sleep(random.randrange(3, 5))

        for i in range(10):
            comment_input = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[aria-label='Add a comment…']"))
            )

            comment_input.click()
            comment_input.clear()
            comment_input.send_keys(comment_text)
            comment_input.send_keys(Keys.ENTER)
            time.sleep(5)
    except Exception as e:
        print(e)
        browser.quit()

# login to Instagram
def login(username, password):
    pass

auth(my_username, my_password)
time.sleep(random.randrange(2, 4))

# comment on the post ten times with a delay of 5 seconds between each comment
comment_text = "Great post!"
comment_on_post(post_url, comment_text)

# close the browser window
browser.quit()
