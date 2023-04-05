from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

Builder.load_string('''
#:kivy 1.10.0
#: import Popup kivy.uix.popup

<RecycleViewRow>:
    orientation: 'horizontal'
    Label:
        text: root.category
    Label:
        text: root.remarks
    BoxLayout:
        orientation:'vertical'
        Label:
            text:root.date
        Label:
            text:root.time
        Label:
            text:root.mode
    Label:
        text:root.amount

<MainScreen>:
    viewclass: 'RecycleViewRow'
    RecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        default_spacing:dp(30)
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'                    
                    ''')

class MessageBox(Popup):
    message = StringProperty()

class RecycleViewRow(BoxLayout):
    category = StringProperty()   
    remarks = StringProperty()
    date = StringProperty()
    time = StringProperty()
    mode = StringProperty()
    amount = StringProperty()

class MainScreen(RecycleView):    
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.data = [{'category': "Button " + str(x), 
                      'remarks': str(x),
                      'date': str(x),
                      'time': str(x),
                      'mode': str(x),
                      'amount': 'amount'} 
                      for x in range(3)]

    def message_box(self, message):
        p = MessageBox()
        p.message = message
        p.open() 
        print('test press: ', message)

class TestApp(App):
    title = "RecycleView Direct Test"

    def build(self):
        return MainScreen()

if __name__ == "__main__":
    TestApp().run()