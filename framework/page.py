from appium.webdriver.common.appiumby import AppiumBy


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element_path, by_text=None):
        if by_text == 'by_text':
            return self.driver.find_element(by=AppiumBy.XPATH, value=element_path).text
        else:
            return self.driver.find_element(by=AppiumBy.XPATH, value=element_path)

    def click_element(self, element):
        return element.click()

    def clear_string_field(self, element):
        return element.clear()

    def send_text_to_string_field(self, element, text_to_string):
        return element.send_keys(text_to_string)

