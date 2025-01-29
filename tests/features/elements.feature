Feature: DemoQA Elements Page
  As a user of DemoQA website
  I want to interact with the Elements items 
  So that I can verify different functionality of Elements 
  
  Scenario: Test all API calls links 
	  Given I am on the Links Elements page
	  When I test all API calls links 
	  Then I should receive the corresponding status code

  Scenario: Test The Radio Button 
    Given I am on the Radio Button Elements page
    When I select each Radio Button 
    Then I should see the corresponding message except for No
	  
#   Scenario: Test The Dynamic Properties 
#       Given I am on the Dynamic Properties Elements page
#       When I click on the button 
#       Then I should see the button change color



