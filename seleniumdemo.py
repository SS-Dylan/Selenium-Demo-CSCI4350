# Dylan Shaffer, CSCI 4350-001
# A simple application to demonstrate Selenium using Python.

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By # Import all necessary libraries

driver = webdriver.Chrome() # Create a new instance of the Chrome driver
driver.get("http://www.youtube.com") # Navigate to YouTube
assert "YouTube" in driver.title # Verify that the title of the page is "YouTube"
elem = driver.find_element(By.NAME, "search_query") # Find the search bar
elem.clear() # Clear the search bar
elem.send_keys("geico ringtone") # Enter the search term
elem.send_keys(Keys.ENTER) # Press the return key
assert "No results found." not in driver.page_source # Verify that the search returned results
time.sleep(5) # Wait for the page to load
video = driver.find_element(By.XPATH, '//a[@href="/watch?v=E-PmJYxusHI&pp=ygUOZ2VpY28gcmluZ3RvbmU%3D"]') # Clicks on a certain video...
video.click() # Click the result
time.sleep(60) # Wait for the video to play
driver.close() # Close the browser