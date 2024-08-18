import json
from abc import ABC, abstractmethod


class FileWork(ABC):

    @abstractmethod
    def read_file(self):
        """чтение файла"""
        pass

    @abstractmethod
    def save_file(self, data):
        """сохранения файла"""
        pass

    @abstractmethod
    def del_file(self):
        """удаление"""
        pass


class WorkWithJson(FileWork):
    def __init__(self, file_name):
        self.__file_name = self.__validation_name_file(file_name)

    @staticmethod
    def __validation_name_file(file_name):
        if file_name == ".json":
            return "vacancy.json"
        return file_name

    def read_file(self):
        with open(f"data/{self.__file_name}", "r", encoding="utf-8") as file:
            return json.load(file)

    def save_file(self, data):
        """Добавляет новые данные в JSON файл."""
        vacancy = []
        try:
            vacancy.extend(self.read_file())
        except FileNotFoundError as err:
            pass
        except json.decoder.JSONDecodeError as err:
            pass
        vacancy.extend(data)
        with open(f"data/{self.__file_name}", 'w', encoding='utf-8') as file:
            json.dump(vacancy, file, ensure_ascii=False, indent=4)

    def del_file(self):
        with open(f"data/{self.__file_name}", "w") as file:
            pass
