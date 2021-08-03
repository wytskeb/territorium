import os

from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout


class StackLayoutPuzzles(StackLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        start_path = './volgorde'  # current directory
        for path, dirs, files in os.walk(start_path):
            for filename in files:
                gamename = filename.split(".")
                size = dp(50)
                b = Button(text=gamename[0], size_hint=(None, None), size=(size * 4, size),
                           background_color=(1, .3, .4, 1), background_normal="", font_size=(dp(30)),
                           font_name='fonts/Eurostile.ttf')
                b.bind(on_release=self.schuifpuzzel_button)
                # b.bind(on_release=self.manager.transition.direction("left"))
                self.add_widget(b)

    @staticmethod
    def schuifpuzzel_button(bestand):
        f = open("volgorde/" + bestand.text + ".lat", "r")
        screen.manager.transition.direction = "left"
        sm.current = "schuifpuzzle"
        SchuifPuzzlesWindow.tekst = f.read()


class SchuifPuzzlesWindow(Screen):

    tekst = ""

    def on_enter(self, *args):
        self.ids.opdrachttekst.text = self.tekst

    @staticmethod
    def verbum_page_button():
        sm.current = "verbum"


class VerbumPuzzlesWindow(Screen):

    @staticmethod
    def ludere_page_button():
        sm.current = "ludere"


class LudereMenuWindow(Screen):

    @staticmethod
    def verbum_puzzles_button():
        sm.current = "verbum"

    @staticmethod
    def domo_page_button():
        sm.current = "domo"


class DomoWindow(Screen):

    @staticmethod
    def ludere_page_button():
        sm.current = "ludere"

    @staticmethod
    def habitat_page_button():
        sm.current = "habitat"


class HabitatMenuWindow(Screen):

    @staticmethod
    def domo_page_button():
        sm.current = "domo"


class MiddleWindowManager(ScreenManager):
    pass


sm = MiddleWindowManager()
# db = DataBase("users.txt")

# de windows van deze app
screens = [DomoWindow(name="domo"), HabitatMenuWindow(name="habitat"), LudereMenuWindow(name="ludere"),
           VerbumPuzzlesWindow(name="verbum"), SchuifPuzzlesWindow(name="schuifpuzzle")]
for screen in screens:
    sm.add_widget(screen)

# Naam eerste window
sm.current = "domo"
