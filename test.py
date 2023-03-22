from selenium import webdriver
import time

# Amazon Credentials

username = "naikprasad4242@gmail.com"
password = "Open@123"

# initialize the Chrome driver

driver = webdriver.Chrome()

# Headin to Amazon Login Page

driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

# Find username/email field and send the username itself to the input field
driver.find_element("id", "ap_email").send_keys(username)
driver.find_element("id", "continue").click()

# find password input field and insert password as well
driver.find_element("id", "ap_password").send_keys(password)

# click login button
driver.find_element("id", "signInSubmit").click()

time.sleep(5)

driver.close()