"""Simple service to load .ini files and extract values in code"""
from os import path
import configparser

from definitions import ROOT_DIR


class ConfigParser:
    # Docs - https://docs.python.org/3/library/configparser.html

    def __init__(self, filename=path.join(ROOT_DIR, "config.ini")):
        self.file = filename
        self.config = configparser.ConfigParser()

    def read(self):
        self.config.read(self.file)

        return self.config

    def get_section(self, key: str):
        for index, item in enumerate(self.config.sections()):
            if key == item:
                return self.config.sections()[index]
            else:
                raise AttributeError(f"[{key}] is not found in sections")

    def get_value(self, section, key):
        return self.config[section].get(key)
