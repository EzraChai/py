from msedge.selenium_tools import options
from msedge.selenium_tools import Edge,EdgeOptions
from time import sleep

options = EdgeOptions()
options.use_chromium = True 
driver = Edge(options=options)

usr = "juanzhe2@gmail.com"
pwd = "D9806f2a2b"

driver.get("https://www.facebook.com/")
print("Opened Facebook")
sleep(0.5)

username_box = driver.find_element_by_id("email")
username_box.send_keys(usr)
print("Email ID entered")
sleep(0.1)

password_box = driver.find_element_by_id("pass")
password_box.send_keys(pwd)
print("Password entered")
sleep(0.5)

enter_box = driver.find_element_by_id("u_0_b").click()
print("Login pressed") 