from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty,NumericProperty
from kivy.uix.recycleview import RecycleView

from record import *

class TableViewRow(BoxLayout):
    category = StringProperty()   
    remarks = StringProperty()
    date = StringProperty()
    time = StringProperty()
    mode = StringProperty()
    amount = NumericProperty()

class TableView(RecycleView):
    db=DbOperation()

    def __init__(self, **kwargs):
        super(TableView, self).__init__(**kwargs)
        self.data = self.rowdata()

    def rowdata(self):
        rows=self.db.fetch_rows_all()
        columns=['category','remarks','date','time','mode','amount']
        list_of_dict=[dict(zip(columns,row)) for row in rows]
        return list_of_dict
    
    def update_data(self):
        #called inside submit Button.
        #Updates TableView with new data everytime a new entry is made.
        self.data=self.rowdata()

if __name__=="__main__":
    TableView().rowdata()