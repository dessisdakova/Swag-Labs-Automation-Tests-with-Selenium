# Swag Labs Automation UI Tests


This project contains automated UI tests for the [Swag Labs](https://www.saucedemo.com/) website using Selenium WebDriver and Python. It follows the Page Object Model (POM) design pattern for better organization and maintainability of test code.

### Running Tests with Specific Users

You can run the tests with specific user roles using the --user command-line option. Default is "standard" Available users are: 
- standard
- locked-out
- problem
- performance
- error
- visual

**Example**:

```pytest --user=standard```

```pytest --user=locked-out```