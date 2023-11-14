import logging
import pytest
from framework.login_page import LoginPage
from utils.android_utils import login_password

@pytest.fixture(scope='package')
def user_login_fixture_positive(driver):
    yield LoginPage(driver, login_password()['login'], login_password()['password'])


@pytest.fixture(scope='function')
def setup_logging():
    loger = logging.getLogger()
    loger.info('CHECKING....all the info in "pytest.log" file!')
