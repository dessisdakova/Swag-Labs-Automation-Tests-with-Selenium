# Swag Labs Automation Tests with Selenium

## Project Overview
This project contains automated tests for the [Swag Labs](https://www.saucedemo.com/) website using Selenium WebDriver with Python. The tests focus on login functionality, error handling, and product sorting.

## Project Structure
- `login_tests.py` - Contains tests related to the login functionality of Swag Labs.<br />
- `products_sorting_tests.py` - Contains tests to verify the sorting of products on the Swag Labs site.<br />

## Tech Stack
*Language:* Python 3.11.3<br />
*IDE:* PyCharm Community Edition 2021<br />
*Testing Framework:*  Selenium<br />

## Dependencies
`selenium`<br/>
`webdriver-manager`<br/>
`unittest`<br/>

## Test Cases
### Login Tests
- **Correct Login:** Verifies that users can log in with valid credentials.</br>
- **Incorrect Password:** Checks that an error message is displayed for incorrect passwords.</br>
- **Locked Out User:** Confirms that a locked-out user receives an appropriate error message</br>
- **Performance Glitch:** Measures the login time for the `performance_glitch_user` to ensure it's slower than the standard user.

### Product Sorting Tests
- **Price (Low to High):** Verifies that products are sorted by price in ascending order.</br>
- **Price (High to Low):** Confirms that products are sorted by price in descending order.</br>
- **Name (A to Z):** Ensures that products are sorted alphabetically from A to Z.</br>
- **Name (Z to A):** Checks that products are sorted alphabetically from Z to A.