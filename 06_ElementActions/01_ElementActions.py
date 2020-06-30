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
print("Text on the button: ", ele_id.get_attribute("content-desc"))
print("Text on the button: ", ele_id.text)
print("Text: ",ele_id.get_attribute("text"))

ele_id.click()

sleep(2)
ele_classname = driver.find_element_by_class_name("android.widget.EditText")
ele_classname.send_keys("Robert")
sleep(2)
ele_classname.clear()

