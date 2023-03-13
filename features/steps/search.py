import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@given(u'I can open the URL')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.opencart.com/index.php?route=marketplace/extension")


@then(u'I can see the search box')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='filter_search']")
    time.sleep(5)


@when(u'I see the search box')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='filter_search']")
    time.sleep(5)


@then(u'I can click the search box')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='filter_search']").click()
    time.sleep(5)


@given(u'I can click the search box')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='filter_search']").click()
    time.sleep(5)


@when(u'I enter paypal')
def step_impl(context):
    a = context.driver.find_element(By.XPATH, "//input[@name='filter_search']")
    a.send_keys("Paypal")
    a.send_keys(Keys.ENTER)
    time.sleep(5)


@then(u'I can see paypal in results')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,"PayPal Checkout Integration").is_displayed()
    time.sleep(5)
