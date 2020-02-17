import pytest
from selenium import webdriver
import json


CONFIG_FILE_PATH = 'tests/config.json'
SUPPORTED_BROWSERS = ['firefox', 'chrome']
DEFAULT_WAIT_TIME = 10


@pytest.fixture(scope="session")
def config():
    with open(CONFIG_FILE_PATH) as file:
        data = json.load(file)
    return data


@pytest.fixture(scope='session')
def config_browser(config):
    if "browser" not in config:
        raise Exception('Config file does not contain "browser"')  # ключ "browser" отсутствует в файле config.json
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not supported browser')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture
def browser(config_browser, config_wait_time):
    if config_browser == 'firefox':
        driver = webdriver.Firefox(executable_path='/home/hitruk/dir/geckodriver')
    elif config_browser == 'chrome':
        driver = webdriver.Chrome(executable_path='/home/hitruk/dir/chromedriver')
    else:
        raise Exception(f'"{config["browser"]}" is not supported browser')
    driver.implicitly_wait(config_wait_time)
    yield driver
    driver.quit()