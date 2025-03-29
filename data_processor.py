from typing import Self, Dict


class IterateOverData:
    def __init__(self: Self, file_path:str, file_handler, open_mode: str):
        self.file_path = file_path
        self.file_handler = file_handler
        self.__count = 0
        self.data = self.file_handler().load(file_path, mode= open_mode)

    def __iter__(self: Self):
        return self
    
    def __next__(self: Self) -> Dict:
        if self.__count < len(self.data):
            current_count = self.__count
            self.__count += 1
            return self.data[current_count]
        else:
            raise StopIteration