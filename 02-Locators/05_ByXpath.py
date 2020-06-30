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

sleep(2)
#ele_xpath = driver.find_element_by_xpath('//android.widget.Button[@content-desc="Btn1"]') #Using xpath description
#ele_xpath = driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]') #using resource id
#ele_xpath = driver.find_element_by_xpath('//android.widget.Button[1]')
#ele_xpath = driver.find_element_by_xpath('//android.widget.Button[@text="ScrollView"]')
ele_xpath = driver.find_element_by_xpath('//android.widget.Button[@content-desc="Btn1"]')
ele_xpath.click()
sleep(2)
driver.find_element_by_xpath('//android.widget.EditText').send_keys("Code2Lead")
sleep(2)
driver.quit()