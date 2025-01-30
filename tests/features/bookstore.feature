Feature: Test the DemoQA Bookstore
  As a user of the DemoQA website
  I want to test the bookstore
  So that I can verify the functionality

  Scenario: Create a user in the bookstore
    Given I navigate to the DemoQA website bookstore
     When I create a new user
     Then the user is created successfully