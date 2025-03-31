from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait

# Set up WebDriver (Change to the browser of your choice)
driver = webdriver.Chrome()  # Ensure chromedriver is installed and in PATH

# Open the login page
driver.get("https://qa.d3skkfzjfy3kf2.amplifyapp.com/")  # Replace with actual login URL

# Maximize the browser window
driver.maximize_window()

# Find username and password fields and enter credentials
username_field = driver.find_element(By.XPATH, "//input[@class='MuiInputBase-input MuiOutlinedInput-input css-7vs0oh']")  # Update selector if needed
password_field = driver.find_element(By.XPATH, "//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1gfwilh']")  # Update selector if needed

username_field.send_keys("sky@acuity.com")
password_field.send_keys("test@111")

# Submit the form (Click login button or press Enter)
login_button = driver.find_element(By.XPATH, "//button[text()='Login']")  # Update selector
login_button.click()

#Print the currentpage
driver.save_screenshot("Invalid-user.png")

# Loading the image
image = Image.open("Invalid-user.png")

# Showing the image
image.show()

#pop up close
try:
    # Wait for pop-up close button to appear
    popup_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Close')]"))
    )
    print(popup_close.text)
    print("Popup closed successfully!")
except Exception as e:
    print("Popup close button not found:", e)

# Wait for the page to load
time.sleep(5)

# Optional: Print current URL and Title to confirm login success
print("Current URL:", driver.current_url)
print("Title:",driver.title)

# Close the browser
driver.quit()
