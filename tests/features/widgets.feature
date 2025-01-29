Feature: DemoQA Widgets Page
  As a user of DemoQA website
  I want to interact with the Widget page
  So that I can verify the functionnality of the widgets 
  
  Scenario: Test the Tool Tips on the Widgets Page
    Given I am on the Tool Tips Page
    When I hover over the Tool Tips
    Then I should see the corresponding Tool Tips message

  Scenario: Test Select Menu on the Widgets Page
    Given I navigate to the select menu widget
    When I select "Option 1" in the "Select value" dropdown
    And I select "Option 2" in the "Select one" dropdown
    And I select "Option 3" in "Old Style Select Menu" dropdown
    And I select all options in "Multi Select Drop Down" dropdown
    # And I select "Option 4" in "Standard multi select"
    # Then the selected values should be displayed
