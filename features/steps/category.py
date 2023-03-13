import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'I can view the categories')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//h4[text()='Category']")
    assert context.driver.find_element(By.XPATH, "//h4[text()='Category']").is_displayed
    context.driver.quit()


@when(u'I click on an option')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[text()='All']").click()


@then(u'results 6 is shown')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,"PayPal Checkout Integration").is_displayed()
    context.driver.quit()


@when(u'I click on All option')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[text()='All']").click()


@then(u'All results are shown')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "PayPal Checkout Integration").is_displayed()
    context.driver.quit()


@when(u'I click on Marketplace option')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[text()='Marketplaces']").click()


@then(u'Marketplace results are shown')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "Google Shopping for OpenCart").is_displayed()
    time.sleep(2)
    context.driver.quit()


@when(u'I click on Themes option')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[text()='Themes']").click()


@then(u'Themes results are shown')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "Antropy Multipurpose Theme").is_displayed()
    time.sleep(2)
    context.driver.quit()


@when(u'I click on Languages option')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[text()='Languages']").click()


@then(u'Languages results are shown')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "Italian Translate").is_displayed()
    context.driver.quit()


@when(u'I click on Payment Gateways option')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[text()='Payment Gateways']").click()


@then(u'Payment Gateways results are shown')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "PayPal Checkout Integration").is_displayed()
    context.driver.quit()


@when(u'I click on Shipping methods option')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[text()='Shipping Methods']").click()


@then(u'Shipping methods results are shown')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "10 Clone Flat Rate").is_displayed()
    context.driver.quit()


@when(u'I click on Modules option')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[text()='Modules']").click()


@then(u'Modules results are shown')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,"Facebook for OpenCart").is_displayed()
    context.driver.quit()


@when(u'I click on Order totals option')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[text()='Order Totals']").click()


@then(u'Order totals results are shown')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,"Customer Group Discount").is_displayed()
    context.driver.quit()


@when(u'I click on Product feeds option')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[text()='Product Feeds']").click()


@then(u'Product feeds results are shown')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,"Advanced Sitemap Generator").is_displayed()
    context.driver.quit()


@when(u'I click on Report option')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[text()='Reports']").click()


@then(u'Report results are shown')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "Sales Extended Report").is_displayed()
    context.driver.quit()


@when(u'I click on Other option')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[text()='Other']").click()


@then(u'Other results are shown')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "Return request mail").is_displayed()
    context.driver.quit()

