Feature: DemoQA Forms Page
  As a user of DemoQA website
  I want to interact with the Forms page
  So that I can verify the functionnality of the form  
  
  Scenario: Test the Practice Form
    Given I am on the Practice Form Page
    When I fill in the form 
    Then I have confirmation of registration 
	  