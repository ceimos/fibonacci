from kivy import __version__
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('style.kv')

class Main(BoxLayout):
    pass

class Fibonnacci(App): #CODE NAMED FIBONNACI.
    def build(self):
        return Main()
    
if __name__=="__main__":
    Fibonnacci().run()