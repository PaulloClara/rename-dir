from tkinter import *


class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self.title('Auto Rename Archives')
        self.geometry('400x500')
        self.resizable(0, 0)

        self.__controller = controller

        self.field_input = self._create_field_input()

    def _create_field_input(self):
        field_input = FieldInput(master=self)

        field_input.config_button(
            command=self.__controller.click_button_send
        )

        return field_input

    def start(self):
        self.mainloop()


class FieldInput(Frame):
    def __init__(self, master):
        super().__init__(master=master, bd=10)
        self.grid()

        self.__label = self._create_label()
        self.__input = self._create_input()
        self.__button = self._create_button()

    def _create_label(self):
        label = Label(
            master=self,
            text='Enter the file path',
            font=('arial', 12, 'bold')
        )

        label.grid(row=0, column=0, sticky='W')

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

        _input.grid(row=1, column=0, pady=6)
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

        button.grid(row=1, column=1, padx=6)

        return button

    def config_button(self, command):
        self.__button.configure(command=command)

    def get_path(self):
        return self.__input.get()
