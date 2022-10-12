# Importing required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Local chrome driver path which is installed in you PC, .exe must for win users
chrome_driver_path = "C:\Development\chromedriver.exe"

# Creating a new driver from the module, we can now instantiate any browser we want..
# After choosing Chrome as our browser the only argument required to give is- executable path.. above mentioned the path
# Chrome driver is a bridge which is to establish a communication between chrome browser and selenium script
# There are different drivers for different browsers
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Using our driver to open up a webpage... passing the URL of the site to which we look to open.
driver.get("http://secure-retreat-92358.herokuapp.com/")

# Finding the element by it's name on the web by inspecting
f_name = driver.find_element_by_name("fName")
# Sending the data on-to the input which we want to input as to signup, using the send_keys method
f_name.send_keys("Prabhakar")
# Taking control of the keyboard as to navigate through the input boxes and shifting to other i/p box
f_name.send_keys(Keys.TAB)

# Follow the same for second field data
l_name = driver.find_element_by_name("lName")
l_name.send_keys("Kulkarni")
l_name.send_keys(Keys.TAB)

# Final script to press enter and sign up success!
email = driver.find_element_by_name("email")
email.send_keys("kulkarniprabhakar2000@gmail.com")
email.send_keys(Keys.ENTER)
