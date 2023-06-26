# Testing_wingify
# Testing_wingify

# Testing Project

This project contains automation scripts for testing the Login Page and Home Page of an application using Selenium and Python.

## Installation

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command:
 pip install requirements.txt
   
3. Download the appropriate WebDriver for your browser and ensure it is available in your system's PATH.

## Usage

1. Navigate to the project directory.

2. Run the test script using the following command:

python test_script.py


3. The test script will launch the browser, perform functional testing on the Login Page, and then navigate to the Home Page to check if the transaction amounts are sorted.

4. After the test execution, the test results will be displayed in the console, and an HTML report named `report.html` will be generated in the project directory.

## Test Scenarios

### Login Page

Covered functional testing scenarios for the Login Page include:

- Valid username and password
- Invalid username and valid password
- Valid username and invalid password
- Empty username and password fields

### Home Page

After successfully logging in, the test script performs the following actions on the Home Page:

- Clicks on the AMOUNT header in the transaction table to sort the values.
- Verifies if the transaction amounts are sorted in ascending order.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).



