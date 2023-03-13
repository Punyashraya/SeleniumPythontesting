import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'I can see the developed by box')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//h4[text()='Developed by']").click()
    assert context.driver.find_element(By.XPATH, "//h4[text()='Developed by']").is_displayed()
    time.sleep(2)

@then(u'I can select an option')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//h4[text()='Developed by']").click()
    assert context.driver.find_element(By.XPATH, "//h4[text()='Developed by']").is_displayed()
    time.sleep(2)

@given(u'I can select an option')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//h4[text()='Developed by']").click()
    assert context.driver.find_element(By.XPATH, "//h4[text()='Developed by']").is_displayed()
    time.sleep(2)

@then(u'results 4 are shown')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//label[normalize-space()='Developers']").click()
    assert context.driver.find_element(By.XPATH, "//label[normalize-space()='Developers']").is_displayed()
    time.sleep(2)

@then(u'results 5 are shown')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,
                                    "//select[@id='input-sort']//option[contains(text(),'Rating')]").is_displayed()

    time.sleep(2)