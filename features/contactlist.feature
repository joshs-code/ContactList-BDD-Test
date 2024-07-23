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