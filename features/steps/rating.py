import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'I can see the rating box')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//h4[contains(text(),'Rating')]")
    assert context.driver.find_element(By.XPATH, "//h4[contains(text(),'Rating')]").is_displayed()


@when(u'I click on the rating box')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//section[@id='extension-rating']//li[1]//a[1]").click()


@then(u'selected ratings result appear')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,
                                    "//div[@id='extension-list']//div[2]//div[1]//section[1]//div[3]").is_displayed()


@then(u'results 3 are shown')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//a[contains(text(),'Fix PayPal Standard unsupported currency')]")

