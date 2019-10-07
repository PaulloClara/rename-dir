from tkinter import *


class App(Frame):
    def __init__(self, master):
        super().__init__(master=master, bd=10)
        self.grid()

        self.field_input_path = None

    def start(self):
        self.create_field_input()

        self.mainloop()

    def start_rename(self):
        path = self.get_input_path()

        print(path)

    def create_field_input(self):
        self.field_input_path = {}

        self.field_input_path['label'] = Label(
            master=self,
            text='Enter the file path',
            font=('arial', 12, 'bold')
        )
        self.field_input_path['label'].grid(row=0, column=0, sticky='W')

        self.field_input_path['input'] = Entry(
            master=self,
            width=28,
            bd=2,
            bg='white',
            fg='black',
            font=('arial', 14, 'italic')
        )
        self.field_input_path['input'].grid(row=1, column=0, pady=10)
        self.field_input_path['input'].focus()

        self.field_input_path['button'] = Button(
            master=self,
            text='Send',
            width=6,
            bg='green',
            font=('arial', 14, 'bold'),
            command=self.start_rename
        )
        self.field_input_path['button'].grid(row=1, column=1, padx=6)

    def get_input_path(self):
        return self.field_input_path['input'].get()


if __name__ == "__main__":
    window = Tk()
    window.title('Auto Rename Archives')
    window.geometry('400x500')
    window.resizable(0, 0)

    app = App(master=window)
    app.start()
