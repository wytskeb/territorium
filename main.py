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
            b = Button(text="Knop " + str(i+1), size_hint=(None, None), size=(size * 4, size), on_press=self.boe())
            self.add_widget(b)


    def boe(self):
        print("Boe")


    #def on_event(self, obj):
    #    print("Typical event from", obj)

    #def on_property(self, obj, value):
    #    print("Typical property change from", obj, "to", value)

    #def on_anything(self, *args, **kwargs):
    #    print('The flexible function has *args of', str(args),
    #          "and **kwargs of", str(kwargs))



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
