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
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.popup import Popup

import regex as re #USED for floatInput filter.

from record import * #DATABASE OPERATIONS - DbOperations()

from datetime import date,datetime

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

class MessagePopUp(Popup):
    pass

class Main(GridLayout):
    db=DbOperation()
    categories=ListProperty(db.fetch_categories())
    
    def submit(self):

        if self.ids.amount_input.text=='':
            message=Label(text="Press Anywhere To dismiss.", color=[1,0,0,1],font_size=dp(15))
            popup=MessagePopUp(title='Must Enter Amount!',
                           content=message,
                           separator_color=[1,0,0,0.5],
                           title_size=dp(25))
            popup.open()


        else:
            input_list=[
                float(self.ids.amount_input.text),
                date.today().strftime(f'%Y-%m-%d'),
                datetime.now().time().strftime('%H:%M:%S'),
                self.ids.payment_mode.text,
                self.ids.remarks.text,
                self.ids.category_dropdown.text,
                ]
            #SEQUENCE in the list IS IMPORTANT
            self.db.record_expense(tuple(input_list))
            self.reset_values()
            message=Label(text="Press Anywhere To dismiss.", color=[0,1,0,1],font_size=dp(15))
            popup=MessagePopUp(title='Success!',
                           content=message,
                           separator_color=[0,1,0,0.5])
            popup.open()

    def reset_values(self):
        self.ids.amount_input.text=''
        self.ids.payment_mode.text='UPI'
        self.ids.remarks.text=''
        self.ids.category_dropdown.text='Category'
    
class Fibonnacci(App): #CODE NAME - FIBONNACI.    
    def build(self):
        return Main()

if __name__=="__main__":
    Fibonnacci().run()