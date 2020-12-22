#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import sys
import os
from time import sleep

TIMEOUT = 15
NAME = "App Team"
NAVER_EMAIL = "email"

class CommandLine:

    def gift_price(self):
        os.system('clear')
        price = int(input("Enter the price of gift card (ex. '5): "))
        return price

    def email_list(self):
        emails_len = int(input("Enter the number of emails (ex. '3'): "))
        print("Paste emails from excel sheet cells/column (the newlines will be included and auto hit enter for the command line).")
        email_arr = []
        args_check = ""
        for i in range(emails_len):
            commandline_arg = input("\n") # '\n' TO 'ENTER' ON COMMANDLINE EACH EMAIL
            print(f"\nemails: {commandline_arg}")
            email_arr.append(commandline_arg)
        print(f"\n\n{email_arr}")
        return email_arr

def navigate_page_1(driver):
    driver.get("https://www.starbucks.com/shop/card/egift/workplace")
    return driver

def keep_Shopping(driver):
    try:
        button = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="keepShoppingButton"]' ) ))
        button.click() 
    except TimeoutError:
        print("Timed out trying to find keep_Shopping 'button'.")
    return driver

def form_filling(page_1, email, count, arr_len, price):
    congrats = "Congrats on winning!! Thanks for using the BAND App!"
    message_area = WebDriverWait(page_1, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="message"]' ) ))
    message_area.send_keys(congrats)
    price_button = WebDriverWait(page_1, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="pre_range"]/p' ) ))
    price_button.click()
    price_area = WebDriverWait(page_1, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="amount"]' ) ))
    price_area.clear()
    price_area.send_keys(price)
    name_area = WebDriverWait(page_1, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="sender_name"]' ) ))
    name_area.send_keys(NAME)
    my_email_area = WebDriverWait(page_1, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="sender_email"]' ) ))
    my_email_area.send_keys(NAVER_EMAIL)
    user_email_area = WebDriverWait(page_1, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="recipient_email"]' ) ))
    user_email_area.send_keys(email)
    sleep(1)

    # PUT A CONDITIONS HERE BASED ON ARRAY LENGTH
    add_cart_button = WebDriverWait(page_1, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="ecardform"]/div[3]/span/button' ) ))
    add_cart_button.click()
    if count != (arr_len - 1):
        keep_Shopping(page_1)
        # USING 'CSS_SELECTOR' BELOW BECAUSE XPATH WAS CHANGING WHEN WEBSITE ADDED AND DELETED CERTAIN GIFT CARD OPTIONS
        workplace_button = WebDriverWait(page_1, TIMEOUT).until(EC.visibility_of_element_located( ( By.CSS_SELECTOR, "a[href='/shop/card/egift/workplace']" ) ))        
        workplace_button.click()

def gift_card(price, email, driver, count, arr_len):
    page_1 = driver
    try:
        form_filling(page_1, email, count, arr_len, price)
    except TimeoutError:
        print("Timed out on gift_card function")
    return driver

def cards_loop(price, email_arr, arr_len, driver):
    email = ""
    for i in range(arr_len):
        email = email_arr.pop()
        gift_card(price, email, driver, i, arr_len)
    return driver

def checkout_guest(driver):
    checkout_button = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="checkoutButton"]' ) ))
    checkout_button.click()
    guest_button = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '    //*[@id="content"]/div[2]/div/div/div/div/div[1]/form[2]/button' ) ))
    guest_button.click()

def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = navigate_page_1(driver)
    flag = True
    while flag == True:
        emails = CommandLine()
        price = emails.gift_price()
        email_arr = emails.email_list()
        #driver = webdriver.Chrome(options=options)
        arr_len = len(email_arr)
        driver = cards_loop(price, email_arr, arr_len, driver)
        flag_check = input("More giftcards? (y or n): ")
        if flag_check == 'n':
            flag = False
            break
        driver = navigate_page_1(driver)
    print("Ready for review...")
    input("If correct, hit 'Enter' to continue to fill in cc info (Guest Checkout)")
    checkout_guest(driver)
    input("Hit 'Enter' to close the program...")

if __name__== "__main__":
  main()
