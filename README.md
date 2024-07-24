#### Type of Testing: Functional and Regression Testing

#### To run tests: behave -f allure_behave.formatter:AllureFormatter -o "reports" features/contactlist.feature ####

These test cases cover a range of functionalities in the contact list web app, including user management, contact management, search and sorting features, and error handling. 
They are designed to ensure the application's functionality, usability, and reliability. 

**Test Case 1: Verify User Registration**  ===> COMPLETED <br>
    Input: New user registration details, including a unique username, email, and strong password
    Expected Outcome: Successful registration

**Test Case 2: Verify Login Functionality** ===> COMPLETED <br>
    Input: Valid username and password
    Expected Outcome: Successful login and redirection to the user dashboard

**Test Case 3: Verify Invalid Login Attempt** ===> COMPLETED <br>
    Input: Invalid username and/or password, and incorrect multi-factor authentication code (if enabled)
    Expected Outcome: Proper error message displayed

**Test Case 4: Verify Adding a New Contact** ===> COMPLETED <br>
    Input: Valid contact details, including name, email, phone number, and address
    Expected Outcome: Contact added successfully

**Test Case 5: Verify Editing a Contact** ===> COMPLETED <br>
    Input: Existing contact details with modifications, including changes to contact information or adding additional notes
    Expected Outcome: Contact details updated successfully

**Test Case 6: Verify Deleting a Contact** ===> COMPLETED <br>
    Input: Select a contact to delete, with confirmation prompt for deletion
    Expected Outcome: Contact deleted and removed from the user's contact list