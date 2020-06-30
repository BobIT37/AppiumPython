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

element = driver.find_elements_by_class_name('android.widget.Button')

for x in element:
    print(x.text)

for x in element:
    button = x.text
    if button == "ScrollView":
        x.click()
        break

sleep(3)
driver.quit()