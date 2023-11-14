import pytest
from time import sleep


for_negative = [
    ('//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Forgot password?"]',
     'Forgot password?'),
    ('//android.widget.TextView[@resource-id="com.ajaxsystems:id/agreement"]', 'By tapping Log In, you agree to our '
                                                                               'Terms of Services: End User '
                                                                               'Agreement, Privacy Policy'),
    ('//android.widget.TextView[@resource-id="label" and @text="Email"]', 'Email'),
    ('//android.widget.TextView[@resource-id="label" and @text="Password"]', 'Password'),
    ('//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]', 'Log In')

]


@pytest.mark.parametrize('xpath, expected', for_negative)
def test_negative_user_login(setup_logging, user_login_fixture_negative, xpath, expected):
    assert user_login_fixture_negative.find_element(xpath, by_text='by_text') == expected
    sleep(1)
