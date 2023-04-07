from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Graph(BoxLayout):
    def __init__(self,fig,**kwargs):
        super().__init__(**kwargs)
        figure_widget=FigureCanvasKivyAgg(fig)
        self.add_widget(figure_widget)

class GraphScrollView(RecycleView):
    def __init__(self, **kwargs):
        super(GraphScrollView, self).__init__(**kwargs)
        self.data = self.rowdata()

    def rowdata(self):
        apple = plt.figure()
        ax = apple.add_subplot(111)
        ax.plot([1, 2, 3], [4, 5, 6])
        return [{'fig_data':apple},{'fig_data':apple}]
    
    
if __name__ == '__main__':
    pass