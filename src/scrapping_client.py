import requests
from os import environ, devnull
from simplejson import JSONDecodeError
from os import kill
from signal import SIGKILL
from typing import Dict, List, Any, Tuple, Type
import copy
from urllib.parse import urljoin
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

from operance_api_base.custom_exceptions import (
    ClientException,
    ClientAuthenticationException,
    ClientConnectionException,
    ClientJSONException
)


class BaseScraperClient:
    """
        UI Client for data fetch using Firefox browser by default.
        Class for using Selenium tools guided by SeleniumClient.
    """
    def __init__(self, **kwargs):
        """
            Setup the Selenium settings and selenium webdriver
        """
        self.driver = self._get_default_driver()
        self.pid = self.driver.capabilities['moz:processID']

    @staticmethod
    def _get_default_driver():
        options = Options()
        if not environ.get('ENV_TYPE') == 'local':
            options.add_argument('--headless')
        return webdriver.Firefox(
            # service_log_path=devnull,
            firefox_options=options
        )

    @staticmethod
    def by_translation():
        return {
            "id": By.ID,
            "class_name": By.CLASS_NAME,
            "css_selector": By.CSS_SELECTOR,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "name": By.NAME,
            "xpath": By.XPATH,
            "tag_name": By.TAG_NAME,
        }

    @staticmethod
    def wait_translation():
        return {
            "element_present": EC.presence_of_element_located,
            "element_visible": EC.visibility_of_element_located,
            "all_elements_present": EC.presence_of_all_elements_located,
            "text_present_in_element": EC.text_to_be_present_in_element,
            "text_present_in_value_attr": EC.text_to_be_present_in_element_value,
            "frame_available": EC.frame_to_be_available_and_switch_to_it,
            "element_invisible": EC.invisibility_of_element_located,
            "element_clickable": EC.element_to_be_clickable,
            "element_selected": EC.element_located_to_be_selected,
        }

    def get_source(self, url):
        self.driver.get(url)

    def webdriver_wait(self, delay: int, until_condition: str, path_type: str, path: str) -> None:
        if until_condition not in self.wait_translation().keys():
            raise Exception('error_given_until_condition_is_not_allowed')
        try:
            WebDriverWait(self.driver, delay).until(
                self.wait_translation()[until_condition](
                    (self.by_translation()[path_type], path)
                )
            )
        except TimeoutException as err:
            raise ClientException(err)

    def find_element(self, path_type: str, path: str) -> WebElement:
        try:
            return self.driver.find_element(self.by_translation()[path_type], path)
        except Exception as err:
            raise ClientConnectionException(err)

    def find_elements(self, path_type: str, path: str) -> List[WebElement]:
        if path_type == 'id':
            raise IOError('error_cannot_find_elements_set_by_id')
        try:
            return self.driver.find_elements(self.by_translation()[path_type], path)
        except Exception as err:
            raise ClientConnectionException(err)

    def send_key(self, path_type: str, path: str, key: str) -> None:
        try:
            return self.find_element(path_type=path_type, path=path).send_keys(key)
        except Exception as err:
            raise ClientException(err)

    def click(self, path_type: str, path: str) -> None:
        try:
            return self.find_element(path_type=path_type, path=path).click()
        except Exception as err:
            raise ClientException(err)

    # noinspection PyMethodMayBeStatic
    def get_element_text(self, element: WebElement) -> str:
        return element.text

    # noinspection PyMethodMayBeStatic
    def get_element_attribute(self, element: WebElement, attribute_name: str) -> str:
        return element.get_attribute(attribute_name)

    def __del__(self):
        try:
            kill(self.pid, SIGKILL)
        except ProcessLookupError:
            raise Exception(f'error_browser_was_not_killed_{self.pid}')

