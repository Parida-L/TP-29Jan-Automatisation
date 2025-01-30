# TP-29Jan-Automatisation

## 📌 Introduction
Ce TP vise à automatiser les tests des fonctionnalités du site **DemoQA** en utilisant **Selenium**. L'énoncé du TP se trouve dans le fichier [enonce.md](./enonce.md).

Chaque partie de l'énoncé a été transformée en **feature Gherkin** avec ses scénarios associés, organisés par catégorie. Ce découpage facilite l'ajout de nouveaux tests sans complexifier la structure existante.

---

## 📂 Organisation du projet

📁 **tests/** *(Dossier contenant les implémentations des tests Python avec Selenium)*
- `test_elements.py`
- `test_forms.py`
- `test_widgets.py`
- `test_bookstore.py`

📁 **tests/features/** *(Dossier contenant les tests Gherkin)*
- `elements.feature` → Tests des éléments interactifs (API calls, radio buttons, propriétés dynamiques)
- `forms.feature` → Test du formulaire
- `widgets.feature` → Tests des widgets (Tool Tips, Select Menu)
- `bookstore.feature` → Test de la création d’un utilisateur dans la bookstore

📁 **utils/** *(Dossier contenant les fonctions utilitaires)*
- `username_generator.py` → Génération de noms d’utilisateurs uniques
- `password_generator.py` → Génération de mots de passe

- 📄 **installation.md** *(Instructions pour l'installation et configuration du projet)*
- 📄 **README.md** *(Ce fichier !)*
- 📄 **report.html** *(Rapport généré après exécution des tests)*

---

## 🎯 Fonctionnalités testées

### **1️⃣ Feature: Test the DemoQA Bookstore** ✅
```gherkin
Feature: Test the DemoQA Bookstore
  As a user of the DemoQA website
  I want to test the bookstore
  So that I can verify the functionality

  Scenario: Create a user in the bookstore
    Given I navigate to the DemoQA website bookstore
    When I create a new user
    Then the user is created successfully
```

### **2️⃣ Feature: DemoQA Elements Page** ✅
```gherkin
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

### **3️⃣ Feature: DemoQA Forms Page** ✅
```gherkin
Feature: DemoQA Forms Page
  As a user of DemoQA website
  I want to interact with the Forms page
  So that I can verify the functionnality of the form

  Scenario: Test the Practice Form
    Given I am on the Practice Form Page
    When I fill in the form
    Then I have confirmation of registration
```

### **4️⃣ Feature: DemoQA Widgets Page** ✅
```gherkin
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
    And I select "Option 4" in "Standard multi select"
    Then the selected values should be displayed
```

---

## ⚙️ Installation et Configuration

Avant d'exécuter les tests, suivez les instructions du fichier [installation.md](./installation.md)


1. **Exécuter les tests**
   ```sh
   pytest tests/test_elements.py --html=report.html
   ```

---

## 🎯 Exécuter un test spécifique
Si vous souhaitez exécuter uniquement un test précis, utilisez :
```sh
pytest tests/test_elements.py --gherkin-terminal-reporter --html=report.html -k "Test_The_Radio_Button"
```

---

## 📊 Génération du Rapport de Tests
Après l'exécution des tests, un fichier `report.html` est généré contenant les résultats détaillés.

---

## 💡 Améliorations futures
- Ajouter de nouveaux scénarios pour d'autres fonctionnalités de DemoQA

