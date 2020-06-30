from appium import webdriver
from time import sleep

desired_caps = {}

desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "9.0"
desired_caps["deviceName"] =  "Pixel_2"
desired_caps["app"] = "/Users/bobit/Desktop/Android_Demo_App.apk"
desired_caps["appPackage"] = "com.code2lead.kwad"
desired_caps["appActivity"] = "com.code2lead.kwad.MainActivity"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

#https://stackoverflow.com/questions/7789826/adb-shell-input-events

ele_id = driver.find_element_by_id("com.code2lead.kwad:id/EnterValue")
print("is Displayed : ",ele_id.is_displayed())
print("is Enabled : ",ele_id.is_enabled())
print("is Selected : ",ele_id.is_selected())
print("Size : ",ele_id.size)
print("Location : ",ele_id.location)