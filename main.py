from kivy import __version__
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.metrics import dp,inch
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.properties import ListProperty,StringProperty
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.recycleview import RecycleView

import regex as re #USED for floatInput filter.
from datetime import date,datetime

from record import * #DATABASE OPERATIONS - DbOperations()
from dataview import * #Table View of all Transactions
from analyse import * #Data Analysis Function and Graphs.


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

    def on_touch_move(self, touch): #Two Swipe(and switch) tabbed panels.
        tabs=self.ids.Tabs
        index_current_tab=tabs.tab_list.index(tabs.current_tab)

        if touch.dx > 60 and index_current_tab < len(tabs.tab_list)-1:
            tabs.switch_to(tabs.tab_list[index_current_tab+1])

        if touch.dx < -60 and index_current_tab > 0:
            tabs.switch_to(tabs.tab_list[index_current_tab-1])

        #return super().on_touch_move(touch)
    
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
            self.ids.ActiveTableView.update_data()
            popup.open()

    def reset_values(self):
        self.ids.amount_input.text=''
        self.ids.payment_mode.text='UPI'
        self.ids.remarks.text=''
        self.ids.category_dropdown.text='Category'

    def refresh_graphs(self):
        self.ids.GraphScrollView.refresh_graphs_n_data()
    
class Fibonacci(App): #CODE NAME - FIBONNACI.
    def build(self):
        return Main()

if __name__=="__main__":
    Fibonacci().run()