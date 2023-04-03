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

class MessagePopup(ButtonBehavior,Label):
    def on_release(self):
         parent=self.parent.parent.ids
         parent.floatlay.remove_widget(parent.floatlay.children[0])
         parent.remarks.hint_text='Remarks'
         parent.remarks.disabled=False
         parent.amount_input.disabled=False

class Main(GridLayout):
    db=DbOperation()
    categories=ListProperty(db.fetch_categories())
    
    def submit(self):

        if self.ids.amount_input.text=='':
            self.amount_validation_msg()

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
            self.record_success_msg()

    def reset_values(self):
        self.ids.amount_input.text=''
        self.ids.payment_mode.text='UPI'
        self.ids.remarks.text=''
        self.ids.category_dropdown.text='Category'

    def record_success_msg(self):
        self.ids.remarks.hint_text=''
        self.ids.remarks.disabled=True
        self.ids.amount_input.disabled=False
        self.ids.floatlay.add_widget(MessagePopup(
            text='Success!',
            color=[0,1,0,1],))
        self.ids.floatlay.children[0].id='this'
    
    def amount_validation_msg(self):
        self.ids.remarks.hint_text=''
        self.ids.remarks.disabled=True
        self.ids.floatlay.add_widget(MessagePopup(
            text='Must Enter Amount!',
            color=[1,0,0,1],))
    
class Fibonnacci(App): #CODE NAME - FIBONNACI.    
    def build(self):
        return Main()

if __name__=="__main__":
    Fibonnacci().run()