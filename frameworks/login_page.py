from time import sleep
from .page import Page


class LoginPage(Page):
    def __init__(self, driver, login, password):
        super().__init__(driver)
        self.login = login
        self.password = password
        self.click_element(self.find_element('(//androidx.compose.ui.platform.ComposeView['
                                              '@resource-id="com.ajaxsystems:id/compose_view"])['
                                              '1]/android.view.View/android.view.View/android.widget.Button'))
        self.clear_string_field(self.find_element('(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]'))

        self.send_text_to_string_field(self.find_element('(//android.widget.EditText['
                                                         '@resource-id="defaultAutomationId"])[1]'), self.login)
        self.send_text_to_string_field(self.find_element('(//android.widget.EditText['
                                                         '@resource-id="defaultAutomationId"])[2]'), self.password)
        self.click_element(self.find_element(
            '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])['
            '4]/android.view.View/android.view.View/android.widget.Button'))
        sleep(10)


