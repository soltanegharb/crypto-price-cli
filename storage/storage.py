import pickle
import os

from typing import Self, Any
from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def dump(self):
        pass


class PickleFiles(FileHandler):
    def __init__(self: Self):
        self.file = None

    def __test_file_path(self:Self, file_path:str):
        if os.path.exists(file_path):
            return True
        else:
            raise FileExistsError("please send an available file path")

    def __open(self: Self, file_path: str, mode: str):
        self.file = open(file=file_path, mode=mode)
    
    def load(self: Self, file_path: str, mode: str):
        if self.__test_file_path(file_path=file_path):
            self.__open(file_path=file_path, mode=mode)
            return pickle.load(self.file)

    def dump(self: Self, to_be_written: Any, file_path: str, mode:str):
        self.__open(file_path=file_path, mode=mode)
        pickle.dump(to_be_written, self.file)

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
