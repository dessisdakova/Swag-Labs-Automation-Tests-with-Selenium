# Swag Labs Automation Tests with Selenium

## Project Overview
This project contains automated tests for the [Swag Labs](https://www.saucedemo.com/) website using Selenium WebDriver with Python. It follows the Page Object Model (POM) design pattern for better organization and maintainability of test code.

## Project Structure
The project is organized using the Page Object Model (POM) pattern, with separate classes for each page of the application. This pattern helps in creating a clear structure for the test code and makes it more modular and reusable.<br />
/tests<br />
├── `base_test.py` - BaseTest class for common setup and teardown logic<br />
├── `login_page_tests.py` - Tests for the Login page<br />
├── `inventory_page_tests.py` - Tests for the Inventory page<br />
└── `cart_page_tests.py` - Tests for the Cart page<br />

/pages<br />
├── `login_page.py` - Page object for the Login page<br />
├── `inventory_page.py` - Page object for the Inventory page<br />
└── `cart_page.py` - Page object for the Cart page<br />

## Tech Stack
*Language:* Python 3.11.3<br />
*IDE:* PyCharm Community Edition 2021<br />
*Testing Framework:*  Selenium<br />

## Dependencies
`selenium`<br/>
`webdriver-manager`<br/>
`unittest`<br/>

## Test Cases
### Login page Tests
- **Correct Login:** Verifies that users can log in with valid credentials.</br>
- **Incorrect Password:** Checks that an error message is displayed for incorrect passwords.</br>
- **Locked Out User:** Confirms that a locked-out user receives an appropriate error message</br>
- **Performance Glitch:** Measures the login time for the `performance_glitch_user` to ensure it's slower than the standard user.

### Inventory page Tests
- **Price (Low to High):** Verifies that products are sorted by price in ascending order.</br>
- **Price (High to Low):** Confirms that products are sorted by price in descending order.</br>
- **Name (A to Z):** Ensures that products are sorted alphabetically from A to Z.</br>
- **Name (Z to A):** Checks that products are sorted alphabetically from Z to A.

### Product Sorting Tests
- **Adding items to cart:** Verifies that exactly the selected items are added to the cart, ensuring no extra or incorrect items are present.