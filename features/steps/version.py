import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'I can see the version box')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@class='input-group']//select[@class='form-control']")
    assert context.driver.find_element(By.XPATH,
                                    "//div[@class='input-group']//select[@class='form-control']").is_displayed()


@when(u'I click on the version box')
def step_impl(context):
    a = context.driver.find_element(By.XPATH, "//div[@class='input-group']//select[@class='form-control']")
    a.click()


@then(u'dropdown list appears')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,
                                    "//div[@class='input-group']//select[@class='form-control']").is_displayed()


@then(u'I select a version')
def step_impl(context):
    a = context.driver.find_element(By.XPATH, "//div[@class='input-group']//select[@class='form-control']")
    context.s = Select(a)
    context.s.select_by_visible_text("4.0.1.1")


@when(u'I select a version')
def step_impl(context):
    a = context.driver.find_element(By.XPATH, "//div[@class='input-group']//select[@class='form-control']")
    context.s = Select(a)
    context.s.select_by_visible_text("4.0.1.1")


@then(u'results are shown')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//div[@class='form-group']//div[@class='input-group']").is_displayed()


@then(u'results 2 are shown')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//div[@class='form-group']//div[@class='input-group']").is_displayed()
