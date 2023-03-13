Feature: To validate the developed by functionality
  Scenario: User can view the developed by functionality
    Given I can open the URL
    Then I can see the developed by box

  Scenario: User can select from developed by functionality
    Given I can open the URL
    Then I can select an option

  Scenario: User can select from developed by functionality after search
    Given I can open the URL
    And I can select an option
    When I enter paypal
    Then results 4 are shown

  Scenario: User can select developed by functionality with other filters
    Given I can open the URL
    And I can select an option
    When I enter paypal
    And I select rating
    Then results 5 are shown