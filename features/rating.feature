Feature: To see the working for ratings functionality
  Scenario: To validate I can see the rating box
    Given I can open the URL
    Then I can see the rating box

  Scenario: To validate the user can select a rating
    Given I can open the URL
    When I click on the rating box
    Then selected ratings result appear

  Scenario: To validate the user can use the app after selecting a rating
    Given I can open the URL
    When I click on the rating box
    And I enter paypal
    Then results 3 are shown