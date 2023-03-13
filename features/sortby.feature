 Feature: Sort by functionality
   Scenario: I can view the sort by box
     Given I can open the URL
     Then I can view the sort by box

   Scenario: I can select the sort by box
       Given I can open the URL
       When I can view the sort by box
       Then I can click the sort by box

   Scenario: I can select Rating in the sort by box
         Given I can open the URL
         When I can click the sort by box
          And I select rating
         Then Rating is selected

   Scenario: I can select Rating in the sort by box and search paypal
         Given I can open the URL
         And I click the sort by box
         When I select rating
         And I search paypal
          Then I can see the sorted results

   Scenario: I can select Rating in the sort by box, search paypal and move to page 2
         Given I can open the URL
         And I select rating
         When I search paypal
         And I click on page  number 2
          Then page 2 results are shown
