import logging
import pytest
from framework.login_page import LoginPage


@pytest.fixture(scope='package')
def user_login_fixture_negative(driver):
    yield LoginPage(driver, '1@ukr.net', '123')


@pytest.fixture(scope='function')
def setup_logging():
    loger = logging.getLogger()
    loger.info('CHECKING....all the info in "pytest.log" file!')
