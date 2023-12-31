# -*- coding:utf-8 -*-
from json import load, dump
from enum import Enum
from os.path import exists
from os import mkdir

class Config:
    def __init__(self, file_path = r'config\\config.json'):
        self.file_path = file_path
        self.data = self.load_config()
        if not exists(file_path):
            mkdir('config')
            with open(file_path, 'w', encoding='utf-8') as f:
                json = {
                    "QFluentWidgets":{
                        "ThemeColor": "#ff009faa",
                        "ThemeMode": "Auto"
                    }
                }
                dump(json, f, ensure_ascii=False, indent=4)

    def load_config(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return load(f)
        except FileNotFoundError:
            return {}

    def save_config(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            dump(self.data, f, ensure_ascii=False, indent=4)

    def getConfig(self, target):
        target = str(target)
        return self.data.get(target)

    def setConfig(self, target, value):
        target = str(target)
        value = str(value)
        self.data[target] = value
        self.save_config()

class Constants(Enum):
    YEAR = 2023
    AUTHOR = 'LingyunAwA'
    PACKAGE_VERSION = 'SnapShot 23w50a'
    HELP_URL = 'https://github.com/Yuns-Lab/YunSchedule/'
    FEEDBACK_URL = 'https://github.com/Yuns-Lab/YunSchedule/issues'
    RELEASE_URL = 'https://github.com/Yuns-Lab/YunSchedule/releases'