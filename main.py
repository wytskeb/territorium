from kivy import Config
from kivy.app import App
from kivy.lang import Builder

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '900')

kv = Builder.load_file("middle_window.kv")

from middle_window import *

class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
