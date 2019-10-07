class Controller:
    def __init__(self):
        self.__model = None
        self.__view = None

    def click_button_send(self):
        path = self.__view.field_input.get_path()

        if not path:
            return

        print(path)

    def start(self, model, view):
        self.__model = model
        self.__view = view

        self.__view.start()
