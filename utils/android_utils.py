from appium.options.common import AppiumOptions


def android_get_desired_capabilities():
    options = {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '8',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': '91a936f4',
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity',
        # 'appium': 'noReset'
    }
    capability_options = AppiumOptions().load_capabilities(options)
    return capability_options


def login_password():
    return {
        'login': 'qa.ajax.app.automation@gmail.com',
        'password': 'qa_automation_password'
    }

