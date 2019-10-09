from tkinter import *


class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self.title('Auto Rename Archives')
        self.geometry('400x500')
        self.resizable(0, 0)

        self.__controller = controller

        self.navbar = self._create_navbar()
        self.field_input = self._create_field_input()

    def _create_navbar(self):
        navbar = Navbar(master=self)

        command = self.__controller.navbar.click_button_home
        navbar.config_button_home(command=command)

        command = self.__controller.navbar.click_button_config
        navbar.config_button_config(command=command)

    def _create_field_input(self):
        field_input = FieldInput(master=self)

        field_input.config_button(
            command=self.__controller.click_button_send
        )

        return field_input

    def create_window_error(self, msg):
        self.window_error = ErrorBox(msg=msg)

    def start(self):
        self.mainloop()


class Navbar(Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.grid()

        self.__button_home = self._create_button_home()
        self.__button_config = self._create_button_config()

    def _create_button_home(self):
        button = Button(
            master=self,
            text='Home',
            bg='green',
            width=12,
            font=('arial', 14, 'bold')
        )

        button.grid(row=0, column=0)

        return button

    def _create_button_config(self):
        button = Button(
            master=self,
            text='Config',
            bg='blue',
            width=12,
            font=('arial', 14, 'bold')
        )

        button.grid(row=0, column=1)

        return button

    def config_button_home(self, command):
        self.__button_home.configure(command=command)

    def config_button_config(self, command):
        self.__button_config.configure(command=command)


class FieldInput(Frame):
    def __init__(self, master):
        super().__init__(master=master, bd=10)
        self.grid()

        self.__input = self._create_input()
        self.__button = self._create_button()
        self.__label = self._create_label()

    def _create_label(self):
        label = Label(
            master=self,
            text='Enter the file path',
            font=('arial', 12, 'bold')
        )

        label.grid(row=1, column=0, sticky='W')

        return label

    def _create_input(self):
        _input = Entry(
            master=self,
            width=28,
            bd=2,
            bg='white',
            fg='black',
            font=('arial', 14, 'italic')
        )

        _input.grid(row=0, column=0, pady=6)
        _input.focus()

        return _input

    def _create_button(self):
        button = Button(
            master=self,
            text='Send',
            width=6,
            bg='green',
            font=('arial', 14, 'bold')
        )

        button.grid(row=0, column=1, padx=6)

        return button

    def config_button(self, command):
        self.__button.configure(command=command)

    def get_path(self):
        return self.__input.get()


class ErrorBox(Tk):
    def __init__(self, msg):
        super().__init__()

        self.title('MSG ERROR')
        self.geometry('300x160')
        self.resizable(0, 0)

        label = Label(
            master=self,
            text=msg,
            fg='red',
            font=('arial', 16, 'bold')
        )
        label.pack(side='top', padx=10)

        button = Button(
            master=self,
            text='OK',
            bg='green',
            width=16,
            command=self.destroy
        )
        button.pack(side='bottom', pady=10)

        self.mainloop()
