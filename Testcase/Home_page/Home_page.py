from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image

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

# Submit the form (Click login button or press Enter)
login_button = driver.find_element(By.XPATH, "//button[text()='Login']")  # Update selector
login_button.click()


# Wait for the page to load
time.sleep(5)

# Optional: Print current URL and Title to confirm login success
print("Current URL:", driver.current_url)
print("Title:",driver.title)

#User setting page navigation
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/div[1]/div/header/div/div/div[2]/button[2]/div/img"))).click()

my_profile=driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/ul/li[1]")
my_profile.click()

#User save button click
user_save_proceed= driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div/div/div[2]/div/form/div[4]/button[2]")
user_save_proceed.click()

try:
   # Wait until the element is present
     field_values_update = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.ID, ":r2m:"))  # Update locator as needed
     )

     # Clear the field before entering new data

except Exception as e:

    print(f"Error: {e}")

#User save and proceedbutton
user_save_proceed1= driver.find_element(By.XPATH,"//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-4 css-1tz8m30']")
user_save_proceed1.click()

driver.save_screenshot("image.png")

# Loading the image
image = Image.open("image.png")

# Showing the image
image.show()

#Browser close
driver.close()