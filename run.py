from model import Model
from view import View
from controller import Controller


class App:
    def __init__(self):
        self.controller = Controller()
        self.model = Model(controller=self.controller)
        self.view = View(controller=self.controller)

    def start(self):
        self.controller.start(model=self.model, view=self.view)


if __name__ == "__main__":
    app = App()
    app.start()
