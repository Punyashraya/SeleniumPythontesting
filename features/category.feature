Feature: To validate the working of category functionality
  Scenario: User is able to view the categories
    Given I can open the URL
    Then I can view the categories

  Scenario: User is able to choose a category
    Given I can open the URL
    When I click on an option
    Then results 6 is shown

  Scenario: User can choose All from category
    Given I can open the URL
    When I click on All option
    Then All results are shown

  Scenario: User can choose Marketplace from category
    Given I can open the URL
    When I click on Marketplace option
    Then Marketplace results are shown

  Scenario: User can choose Themes from category
    Given I can open the URL
    When I click on Themes option
    Then Themes results are shown

  Scenario: User can choose Languages from category
    Given I can open the URL
    When I click on Languages option
    Then Languages results are shown

  Scenario: User can choose Payment Gateways from category
    Given I can open the URL
    When I click on Payment Gateways option
    Then Payment Gateways results are shown

  Scenario: User can choose Shipping methods from category
    Given I can open the URL
    When I click on Shipping methods option
    Then Shipping methods results are shown

  Scenario: User can choose Modules from category
    Given I can open the URL
    When I click on Modules option
    Then Modules results are shown

  Scenario: User can choose Order totals from category
    Given I can open the URL
    When I click on Order totals option
    Then Order totals results are shown

  Scenario: User can choose All Product feeds category
    Given I can open the URL
    When I click on Product feeds option
    Then Product feeds results are shown

  Scenario: User can choose Report from category
    Given I can open the URL
    When I click on Report option
    Then Report results are shown

  Scenario: User can choose Other from category
    Given I can open the URL
    When I click on Other option
    Then Other results are shown