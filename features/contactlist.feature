Feature: ContactList Login
  Scenario: Register to Contactlist
    Given launch chrome browser
    When I open contact list homepage
    And click sign up button
    And enter first name and last name and email and password
    And click on submit button
    Then user must have successfully created account.
    Then close the browser

  Scenario: Login to ContactList
    Given launch chrome browser
    When i open contact list homepage
    And enter email and password
    And click on the submit button
    Then user must have successfully logged in.
    Then close the browser

  Scenario: Login with Invalid Credentials
    Given launch chrome browser
    When i open contact list homepage
    And enter invalid email and password
    And click on the submit button
    Then user must have received error message
    Then close the browser

  Scenario: Verify Adding a New Contact
    Given launch chrome browser
    When i open contact list homepage
    And enter email and password
    And click on the submit button
    And click add a new contact
    And fill out the contact details
    And click submit button
    Then contact must have successfully added to contact list
    Then close the browser