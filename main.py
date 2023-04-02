from kivy import __version__
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.metrics import dp,inch
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.properties import ListProperty

import regex as re #USED for floatInput filter.

from record import * #DATABASE OPERATIONS - DbOperations()

Builder.load_file('style.kv')

class FloatInput(TextInput): 

    # I DID NOT WRITE THIS CLASS. 
    # SOURCE - "https://kivy.org/doc/stable/api-kivy.uix.textinput.html?highlight=text%20input#module-kivy.uix.textinput"

    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join(
                re.sub(pat, '', s)
                for s in substring.split('.', 1)
            )
        return super().insert_text(s, from_undo=from_undo)
    
class DbInitiate(): 
    def __init__(self) -> None:
        self.db=DbOperation()

class Main(GridLayout):
    db=DbInitiate();db=db.db
    categories=ListProperty(db.fetch_categories())

    def submit(self):
        print(self.categories)

class Fibonnacci(App): #CODE NAME - FIBONNACI.
    def build(self):
        DbInitiate() #SETS up database and tables - if not exists.
        return Main()

if __name__=="__main__":
    Fibonnacci().run()