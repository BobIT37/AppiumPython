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

print("Check if device locked or not: ", driver.is_locked())
print("Current Package: ", driver.current_package)
print("Current Activity: ", driver.current_activity)
print("Current Context: ", driver.current_context)
print("Current orientation: ", driver.orientation)