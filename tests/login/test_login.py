import pytest
from time import sleep


for_positive = [
    ('//android.widget.TextView[@resource-id="com.ajaxsystems:id/text"]', 'Add Hub'),
    ('//android.widget.TextView[@resource-id="com.ajaxsystems:id/addFirstHub"]', 'Add your first hub to start managing '
                                                                                 'the security system')
]


@pytest.mark.parametrize('xpath, expected', for_positive)
def test_positive_user_login(setup_logging, user_login_fixture_positive, xpath, expected):
    assert user_login_fixture_positive.find_element(xpath, by_text='by_text') == expected
    sleep(1)
