import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'I can view entire collection of products')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@id='extension-list']")
    assert context.driver.find_element(By.XPATH,"//div[@id='extension-list']").is_displayed()


@when(u'I select any product')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT,'PayPal Checkout Integration').click()


@then(u'I am taken to result page of that product')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,'PayPal Checkout Integration').is_displayed()


@when(u'I hover on the product')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//img[@class='img-responsive']")


@then(u'I should be able to see product details')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//div[@class='extension-description']").is_displayed()


@when(u'I view the product')
def step_impl(context):
    pass


@then(u'I can see it\'s reviews')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//div[@class='text-right']").is_displayed()


@when(u'I go to next page')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[text()='2']").click()


@then(u'products should be visible')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,"Dashboard Sales without Shipping Costs").is_displayed()
