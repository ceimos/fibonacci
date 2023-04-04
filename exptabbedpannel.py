from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

Builder.load_string("""

<Test>:
    size_hint: .5, .5
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False
    tab_pos:'top_mid'
    tab_width:root.size[0]/3

    TabbedPanelItem:
        background_color: [0,0,0,1]
        background_down:''
        background_normal:''
        border_color:1,0,0,1
        color: [1,1,1,1] if self.state=='down' else [0.5,0.5,0.5,1]
        text: 'first tab'
        Label:
            text: 'First tab content area'
    
    TabbedPanelItem:
        text: 'tab2'
        BoxLayout:
            Label:
                text: 'Second tab content area'
            Button:
                text: 'Button that does nothing'
    TabbedPanelItem:
        text: 'tab3'
        RstDocument:
            text:
                '\\n'.join(("Hello world", "-----------",
                "You are in the third tab."))
<TabbedPanelItem>:
    background_color: 0,0,0,1
    background_down:''
    background_normal:''
    border_color:1,0,0,1
    color: [1,1,1,1] if self.state=='down' else [0.5,0.5,0.5,1]
""")

class Test(TabbedPanel):
    pass


class TabbedPanelApp(App):
    def build(self):
        return Test()


if __name__ == '__main__':
    TabbedPanelApp().run()