import csv
import plotly.figure_factory as ff
import statistics
import pandas as pd
import random 
import plotly.graph_objects as go

data=[]
df=pd.read_csv("data.csv")
data=df["temp"].tolist()




def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_figure(list):
    df=list
    mean=statistics.mean(list)
    print(mean)
    fig=ff.create_distplot([df],["Temperature"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="Mean"))
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set=random_set_of_mean(10)
        mean_list.append(set)
    standard_deviation=statistics.stdev(mean_list)
    print(standard_deviation)
    show_figure(mean_list)
setup()

