class Controller:
    def __init__(self):
        self.__model = None
        self.__view = None

        self.navbar = Navbar(master=self)

    def click_button_send(self):
        path = self.__view.field_input.get_path()

        if not path:
            return

        response = self.__model.get_file_names(path=path)
        if response != 'OK':
            self.__view.create_window_error(msg=response)
            return

        new_file_names = self.__model.run_preview(
            remove=['P', '[', ']'],
            replace={'+': ' ', '_': ' '}
        )

        print(new_file_names)

    def start(self, model, view):
        self.__model = model
        self.__view = view

        self.__view.start()


class Navbar:
    def __init__(self, master):
        self.__master = master

    def click_button_home(self):
        pass

    def click_button_config(self):
        pass
