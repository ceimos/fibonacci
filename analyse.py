from kivy.app import App
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from kivy.uix.recycleview import RecycleView,RecycleDataAdapter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.properties import StringProperty,ListProperty,ObjectProperty
import numpy as np
from record import *
plt.style.use('dark_background')

class PlotGraph():

    def save_graph(self, graph, name : str):
        file_name='.\\resources\\'+name+'.png'
        graph.savefig(file_name,
                      dpi=720,
                      bbox_inches='tight',
                      pad_inches=0.2)

    def test_graph(self):
        fig, ax= plt.subplots(figsize=plt.figaspect(5/7))
        ax.bar([1,2,3,4], [12,34,56,23],0.5,align='center')
        self.save_graph(fig,'test_graph')

    def bar_graph(self, x_data, height_data, graph_name : str, time_period : str):
        time_period=time_period
        fig, ax= plt.subplots(figsize=plt.figaspect(5/7))
        ax.bar(x_data, height_data,0.5,align='center')
        ax.set_xlabel(time_period)
        ax.set_ylabel('Volume')
        self.save_graph(fig,'bar_'+graph_name)

    def pie_chart(self,categories,volume):
        fig,ax=plt.subplots(figsize=plt.figaspect(5/7))
        colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(categories)))
        ax.pie(volume,
               labels=categories,
               colors=colors)
        self.save_graph(fig,'pie')

class Graph(Image):
    pass

class GraphScrollView(RecycleView):

    PlotGraph=PlotGraph()
    db=DbOperation()

    def __init__(self, **kwargs):
        super(GraphScrollView,self).__init__(**kwargs)
        
        self.PlotGraph.bar_graph([1,2,3,4],[10,21,12,18],'month','month')
        self.PlotGraph.bar_graph([5,8,9,10],[10,21,12,18],'year','year')
        self.PlotGraph.bar_graph([87,67,78,74],[10,21,12,18],'week','week')
        self.PlotGraph.pie_chart(self.db.fetch_categories(),[x for x in range(len(self.db.fetch_categories()))])

        self.data=[{'source':'.\\resources\\bar_month.png'},
                   {'source':'.\\resources\\bar_week.png'},
                   {'source':'.\\resources\\bar_year.png'},
                   {'source':'.\\resources\\pie.png'},
                   {'source':'.\\resources\\cat.jpg'}]
    
if __name__ == '__main__':
    PlotGraph().bar_graph([1,2,3,4],[10,20,12,18],'monthly',time_period='month')