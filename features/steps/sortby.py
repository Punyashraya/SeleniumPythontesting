import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'I can view the sort by box')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//label[contains(text(),'Sort by')]")
    assert context.driver.find_element(By.XPATH, "//label[contains(text(),'Sort by')]").is_displayed()


@when(u'I can view the sort by box')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//label[contains(text(),'Sort by')]")
    assert context.driver.find_element(By.XPATH, "//label[contains(text(),'Sort by')]").is_displayed()


@then(u'I can click the sort by box')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//label[contains(text(),'Sort by')]").click()
    assert context.driver.find_element(By.XPATH, "//label[contains(text(),'Sort by')]").is_displayed()


@when(u'I can click the sort by box')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//label[contains(text(),'Sort by')]").click()
    assert context.driver.find_element(By.XPATH, "//label[contains(text(),'Sort by')]").is_displayed()


@when(u'I select rating')
def step_impl(context):
    a = context.driver.find_element(By.XPATH, "//select[@id='input-sort']")
    obj = Select(a)
    obj.select_by_visible_text("Rating")
    assert context.driver.find_element(By.XPATH,
                                    "//select[@id='input-sort']//option[normalize-space()='Rating']").is_displayed()


@then(u'Rating is selected')
def step_impl(context):
    a = context.driver.find_element(By.XPATH, "//select[@id='input-sort']")
    obj = Select(a)
    obj.select_by_visible_text("Rating")
    assert context.driver.find_element(By.XPATH,
                                       "//select[@id='input-sort']//option[normalize-space()='Rating']").is_displayed()


@given(u'I click the sort by box')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//label[contains(text(),'Sort by')]").click()


@when(u'I search paypal')
def step_impl(context):
    a = context.driver.find_element(By.XPATH, "//input[@name='filter_search']")
    a.send_keys("Paypal")
    a.send_keys(Keys.ENTER)
    time.sleep(2)


@then(u'I can see the sorted results')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//a[contains(text(),'PayPal Checkout Integration')]")


@given(u'I select rating')
def step_impl(context):
    a = context.driver.find_element(By.XPATH, "//select[@id='input-sort']")
    obj = Select(a)
    obj.select_by_visible_text("Rating")


@when(u'I click on page  number 2')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//a[@class='page-link'])[1]").click()


@then(u'page 2 results are shown')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//a[normalize-space()='Multi Payment Fee']").is_displayed


