#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

"""
NO LONGER USING CC LOG-IN FORM -- CC.PY AND PASSWD.PY REMOVED FROM LOCAL 
(RE-CREATE BOTH IF GOING TO USE CODE BELOW, NAME THEM cc.py AND passwd.py)
USE VARIABLE NAMES BELOW FOR cc.py
"""

TIMEOUT = 15
NAVER_EMAIL = "email"


def cc_form(driver):
    # CC INFO
    input("Press 'Enter' once FLASH plug-in has been approved")
    driver.refresh()
    email = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="Address_EmailAddress"]' ) ))
    email.send_keys(NAVER_EMAIL)
    name_on_card = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="PaymentMethod_FullName"]' ) ))
    name_on_card.send_keys(cc.NAMEONCARD)
    card_number = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="PaymentMethod_AccountNumber"]' ) ))
    card_number.send_keys(cc.CC)
    cvn = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="PaymentMethod_CVN"]' ) ))
    cvn.send_keys(cc.CVN)
    exp_month = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="keepShoppingButton"]' ) ))
    exp_year = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="keepShoppingButton"]' ) ))
    # BILLING ADDRESS
    first_name = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="Address_FirstName"]' ) ))
    first_name.send_keys(cc.FIRSTNAME)
    last_name = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="Address_LastName"]' ) ))
    last_name.send_keys(cc.LASTNAME)
    street_addr = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="Address_AddressLine1"]' ) ))
    street_addr.send_keys(cc.STADDR)
    zipcode = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="Address_PostalCode"]' ) ))
    zipcode.send_keys(cc.ZIPCODE)
