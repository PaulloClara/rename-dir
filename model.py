import os as OS


class Model:
    def __init__(self, controller):
        self.__controller = controller

        self.__file_names = []
        self.__new_file_names = {}

        self.__remove_chars = []
        self.__replace_chars = {}

    def run_rename(self, configs):
        pass

    def run_preview(self, **opts):
        self.__new_file_names = {}

        self.__remove_chars = []
        self.__replace_chars = {}

        if 'remove' in opts:
            self.__remove_chars = opts['remove']

        if 'replace' in opts:
            self.__replace_chars = opts['replace']

        for file_name in self.__file_names:
            self.__new_file_names[file_name] =\
                self._process_file_name(file_name=file_name)

        return self.__new_file_names

    def _process_file_name(self, file_name):
        for char in self.__remove_chars:
            file_name = file_name.replace(char, '')

        for char in self.__replace_chars:
            file_name = file_name.replace(char, self.__replace_chars[char])

        return file_name

    def get_file_names(self, path):
        try:
            self.__file_names = OS.listdir(path=path)
        except FileNotFoundError:
            return 'Directory not found'

        return 'OK'
