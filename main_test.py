url = "https://sakshingp.github.io/assignment/login.html"

driver.get(url)

# Wait for the username input field to be visible
username_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "form-control"))
)

# Enter the username
username_input.send_keys(username)

password_input = driver.find_element_by_id("password")
password_input.send_keys(password)

login_button = driver.find_element_by_id("log-in")
login_button.click()

print("Logged in successfully")

# Wait for the amount header to be clickable
amount_header = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "amount"))
)

# Click on the amount header to sort the table
amount_header.click()

# Get the list of amounts from the transaction table
amounts = driver.find_elements_by_xpath("//table[@id='transaction-table']//tr[position() > 1]/td[5]")
amounts_text = [amount.text for amount in amounts]

# Check if the amounts are sorted in ascending order
sorted_amounts = sorted(amounts_text)
assert amounts_text == sorted_amounts, "Amounts in the transaction table are not sorted"

print("Amounts in the transaction table are sorted")


time.sleep(4)
# Close the browser
driver.quit()
