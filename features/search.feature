 Feature: Search functionality
   Scenario: I can view the search box
     Given I can open the URL
     Then I can see the search box

     Scenario: I can click the search box
       Given I can open the URL
       When I see the search box
       Then I can click the search box

       Scenario: I can search "paypal" in the search box
         Given I can open the URL
         And I can click the search box
         When I enter paypal
         Then I can see paypal in results



