class Controller:
    def __init__(self):
        self.__model = None
        self.__view = None

    def click_button_send(self):
        path = self.__view.field_input.get_path()

        if not path:
            return

        self.__model.get_file_names(path=path)

        new_file_names = self.__model.run_preview(
            remove=['P', '[', ']'],
            replace={'+': ' ', '_': ' '}
        )

        print(new_file_names)

    def start(self, model, view):
        self.__model = model
        self.__view = view

        self.__view.start()
