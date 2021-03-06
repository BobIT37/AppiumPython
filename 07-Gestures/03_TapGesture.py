from appium import webdriver
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}

desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "9.0"
desired_caps["deviceName"] =  "Pixel_2"
desired_caps["app"] = "/Users/bobit/Desktop/Android_Demo_App.apk"
desired_caps["appPackage"] = "com.code2lead.kwad"
desired_caps["appActivity"] = "com.code2lead.kwad.MainActivity"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,
                                                                       ElementNotSelectableException,
                                                                       NoSuchElementException])


ele = wait.until(lambda  x: x.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(text("LOGIN"))'))

actions = TouchAction(driver)
#actions.tap(None, 530, 1430, 1)
actions.tap(ele, 538, 1680, 1)
actions.perform()

sleep(2)
driver.quit()
