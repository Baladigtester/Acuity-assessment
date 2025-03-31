from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
import time

# Set up WebDriver (Change to the browser of your choice)
driver = webdriver.Chrome()  # Ensure chromedriver is installed and in PATH

# Open the login page
driver.get("https://qa.d3skkfzjfy3kf2.amplifyapp.com/")  # Replace with actual login URL

# Maximize the browser window
driver.maximize_window()

# Find username and password fields and enter credentials
username_field = driver.find_element(By.XPATH, "//input[@class='MuiInputBase-input MuiOutlinedInput-input css-7vs0oh']")  # Update selector if needed
password_field = driver.find_element(By.XPATH, "//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1gfwilh']")  # Update selector if needed

username_field.send_keys("admin@acuity.com")
password_field.send_keys("test@111")

#Remember me (checkbox)
remember_me = driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-gg4vpm']")
remember_me.click()
print("suessess",remember_me)

# Submit the form (Click login button or press Enter)
login_button = driver.find_element(By.XPATH, "//button[text()='Login']")  # Update selector
login_button.click()


# Wait for the page to load
time.sleep(5)

# Optional: Print current URL and Title to confirm login success
print("Current URL:", driver.current_url)
print("Title:",driver.title)

mange= driver.find_element(By.XPATH,"//span[normalize-space()='Manage']")
mange.click()

search_box= driver.find_element(By.CSS_SELECTOR,"[placeholder='Search']")
search_box.send_keys("Digiryte")

# Wait for the page to load
time.sleep(5)

view_details=driver.find_element(By.XPATH,"//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedSecondary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiButton-contained MuiButton-containedSecondary MuiButton-sizeMedium MuiButton-containedSizeMedium css-3st95z']")
view_details.click()

#Print the currentpage
driver.save_screenshot("Searchfunction.png")

# Loading the image
image = Image.open("Searchfunction.png")

# Showing the image
image.show()

# Wait for the page to load
time.sleep(5)

#Browser close
driver.close()