Feature: To see the working for version functionality
  Scenario: To validate I can see the version box
    Given I can open the URL
    Then I can see the version box

  Scenario: To validate the version dropdown list is functional
    Given I can open the URL
    When I click on the version box
    Then dropdown list appears

  Scenario: To validate the user can use the version box
    Given I can open the URL
    When I click on the version box
    Then I select a version

  Scenario: To validate the use of search after version functionality is chosen
    Given I can open the URL
    When I select a version
    And I enter paypal
    Then results are shown

  Scenario: To validate the use of version functionality before search function
    Given I can open the URL
    When I enter paypal
    And I select a version
    Then results 2 are shown