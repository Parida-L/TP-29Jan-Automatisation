# TP-29Jan-Automatisation

Partie 1 - DemoQA 

L'énoncé du TP est dans le fichier [enonce.md](./enonce.md). Chaque partie de l'énoncé a été transformée en Feature Gherkin avec ses scénarios associés. Le découpage permet de structurer clairement les interactions avec les différentes fonctionnalités de DemoQA.

J'ai décidé de séparer les features par catégories.  Les différents scénarios sont les différents éléments des catégories. Ainsi, la feature "Elements" va regrouper les scénarios des appel API (links), boutons radio et des propriétés dynamiques. Ainsi si plus tard, je veux rajouter d'autres scénarios comme text box, je peux le faire facilement sur la feature "Elements".

Features et Scénarios

1. Feature: Elements Page -> API calls ✅, radio button ✅, dynamic properties ✅
   
```Gherkin
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
	  
  Scenario: Test The Dynamic Properties 
      Given I am on the Dynamic Properties Elements page
      When I wait 5 seconds 
      Then the text color of the color change button changes
```

2. Feature: Form Page ✅
```Gherkin
Feature: DemoQA Forms Page
	As a user of DemoQA website
	I want to interact with the Forms page
    So that I can verify the functionnality of the form  
  
  Scenario: Test the Practise Form
	  Given I am on the Practise Form Page
	  When I fill the form 
	  Then I have confirmation of registration 
```

3. Feature: Widgets
```Gherkin
Feature: DemoQA Widgets Page
    As a user of DemoQA website
	I want to interact with the Widget page
    So that I can verify the functionnality of the widgets 

    Scenario: Test the Tool Tips on the Widgets Page
        Given I am on the Tool Tips Page
        When I hover over the Tool Tips
        Then I should see the Tool Tips message
	  
    Scenario: Verify Select menu
        Given I navigate to the select menu widget 
        When I select "Option 1" in the "Select value" dropdown
        And I select "Option 2" in the "Select one" dropdown
        And I select "Option 3" in "Old Style Select Menu" dropdown
        And I select "Option 4" and "Option 5" in "Multi Select Drop Down" dropdown
        Then the selected values should be displayed
```

4. Feature: Bookstore
```Gherkin
Feature: Search in the DemoQA Bookstore
  As a user of the DemoQA website
  I want to test the bookstore
  So that I can verify the functionality

  Scenario: Create a user in the bookstore
    Given I navigate to the DemoQA website bookstore
    When I create a new user
    Then I should see the user created
```

Commande pour lancer seulement un test précis
```
pytest tests/test_elements.py --gherkin-terminal-reporter --html=report.html -k "Test_The_Radio_Button"
```