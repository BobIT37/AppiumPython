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

ele_id = driver.find_element_by_id("com.code2lead.kwad:id/EnterValue")
ele_id.click()

sleep(2)
ele_classname = driver.find_element_by_class_name("android.widget.EditText").send_keys("Code2Lead")




#UiSelector is a method to inspect element. Check appium for detailed info