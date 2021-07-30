from kivy import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
# from kivy.properties import ObjectProperty
# from kivy.uix.popup import Popup
# from kivy.uix.label import Label
# from database import DataBase
from kivy.uix.stacklayout import StackLayout
# from kivy.uix.listview import ListView

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '900')

class StackLayoutPuzzles(StackLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        for i in range(0, 20):
            # size = dp(100) + i*10
            size = dp(50)
            b = Button(text="Knop " + str(i+1), size_hint=(None, None), size=(size * 4, size))

            b.bind(on_press=self.on_event)
            b.bind(state=self.on_property)
            b.bind(on_press=lambda x: self.on_event(None))
            b.bind(on_press=self.on_anything)
            b.bind(on_press=self.on_anything)
            b.bind(on_release=self.boe)
            b.fbind('on_press', self.on_event)
            b.fbind('state', self.on_property)
            print("knop = ", i)
            b.fbind('on_press', self.on_event_with_args, 'right',
                       tree='birch', food='text')
            b.fbind('on_press', self.on_anything)


            self.add_widget(b)


    def boe(self, obj):
        print("6 Boe", str(obj))
        print("_____")

    def on_event(self, obj):
        print("1 en 3 Typical event from", obj)

    def on_property(self, obj, value):
        print("2 Typical property change from", obj, "to", value)

    def on_anything(self, *args, **kwargs):
        print('4 en 5 The flexible function has *args of', str(args),
              "and **kwargs of", str(kwargs))

    def on_event(self, obj):
        print("Typical event from", obj)

    def on_event_with_args(self, side, obj, tree=None, food=None):
        print("Event with args", obj, side, tree, food)

    def on_property(self, obj, value):
        print("Typical property change from", obj, "to", value)

    def on_anything(self, *args, **kwargs):
        print('The flexible function has *args of', str(args),
              "and **kwargs of", str(kwargs))
        return True


class VolgordePuzzlesWindow(Screen):

    @staticmethod
    def puzzle_page_button():
        sm.current = "puzzles"

class WereldMenuWindow(Screen):

    @staticmethod
    def first_page_button():
        sm.current = "first"


class PuzzleMenuWindow(Screen):

    @staticmethod
    def volgorde_puzzles_button():
        sm.current = "volgorde"

    @staticmethod
    def first_page_button():
        sm.current = "first"


class FirstWindow(Screen):

    @staticmethod
    def puzzle_page_button():
        sm.current = "puzzles"

    @staticmethod
    def wereld_page_button():
        sm.current = "wereld"


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("territorium.kv")

sm = WindowManager()
# db = DataBase("users.txt")

# de windows van deze app
screens = [FirstWindow(name="first"), PuzzleMenuWindow(name="puzzles"),  WereldMenuWindow(name="wereld"),
           VolgordePuzzlesWindow(name="volgorde")]
for screen in screens:
    sm.add_widget(screen)

# Naam eerste window
sm.current = "first"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
