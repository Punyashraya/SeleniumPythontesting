Feature: To validate the functionality of product catalog
  Scenario: User should be able to view the products
    Given I can open the URL
    Then I can view entire collection of products

  Scenario: User should be able to select a product
    Given I can open the URL
    When I select any product
    Then I am taken to result page of that product

  Scenario: User should be able to see product details
    Given I can open the URL
    When I hover on the product
    Then I should be able to see product details

  Scenario: User should be able to product reviews
    Given I can open the URL
    When I view the product
    Then I can see it's reviews

  Scenario: User should be able to interact as required on other pages
    Given I can open the URL
    When I go to next page
    Then products should be visible
