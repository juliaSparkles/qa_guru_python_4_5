import pytest
from selene import browser


@pytest.fixture()
def browser_setting():
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    return browser
