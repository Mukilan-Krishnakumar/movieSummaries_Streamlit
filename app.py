import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def n_largest_dict_maker(final_df,n_value):
  '''
  This function takes two inputs : a dataframe and n_value. It return top n_value of 
  labels and their frequencies
  '''
  labels = []
  sizes = []
  labels = final_df['Genres'][:n_value]
  sizes = final_df['Frequency'][:n_value]
  return labels, sizes

def n_smallest_dict_maker(final_df,n_value):
  '''
  This function takes two inputs : a dataframe and n_value. It return bottom n_value of 
  labels and their frequencies
  '''
  labels = []
  sizes = []
  labels = final_df['Genres'][-1*n_value:]
  sizes = final_df['Frequency'][-1*n_value:]
  return labels, sizes

def pieChartMaker(labels,sizes,typeOfChart,n_type):
  '''
  This function creates a pie chart from labels(genres) and their sizes(frequencies)
  '''
  statement = f"Pie Plot of {n_type} {typeOfChart}"
  st.title(statement)
  colors = sns.color_palette('pastel')[0:5]
  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, labels=labels, colors = colors)
  ax1.axis('equal')
  st.pyplot(fig1)

def barPlotMaker(labels,sizes,typeOfChart,n_type):
  '''
  This function creates a bar plot from labels(genres) and their sizes(frequencies)
  '''
  statement = f"Bar Plot of {n_type} {typeOfChart}"
  st.title(statement)
  n_df = pd.DataFrame({"Labels" : labels,"Sizes" : sizes})
  fig = plt.figure(figsize=(12,15))
  ax = sns.barplot(data=n_df, x= "Sizes", y = "Labels")
  ax.set(ylabel = 'Genres')
  ax.set(xlabel = 'Frequency')
  st.pyplot(fig)
    
def functionExecutor(funType,typeOfChart,fianl_df,values):
    '''
    This function executes the given function and produces pie chart and bar plot
    '''
    labels,sizes = funType(final_df,values)
    barPlotMaker(labels,sizes,typeOfChart,values)
    pieChartMaker(labels,sizes,typeOfChart,values)

st.title('Movie Summaries Explorer')
st.markdown('''
This application allows user to perform Exploratory Data Analysis on MovieSummaries DataSet
**Python Libraries:** streamlit, pandas, numpy, matplotlib and seaborn

The dataset can be downloaded from the following [link](http://www.cs.cmu.edu/~ark/personas/).

This dataset contains 42,306 movie plot summaries extracted from Wikipedia along with metadata extracted from FreeBase.

The blog post for creating these visualizations can be found [here](https://medium.com/@mukilankrishnakumar2002/multilabel-classification-on-moviesummaries-dataset-part-1-c5a05b0debdc)
''')
df = pd.read_csv('https://gist.githubusercontent.com/Mukilan-Krishnakumar/e9e5f23ee6293c817fccb411a266636e/raw/ca7e98c8730dcf0ba87cc1a11f01e4b73e343f0b/Frequency.csv')
df.drop(df.columns[0], axis=1, inplace=True)
final_df = df.sort_values(by=['Frequency'], ascending=False)
st.dataframe(df)
st.markdown('''
## Instructions:##
You can select the range in which you want to plot from the **Range Slider** in the sidebar.

You can select the type of plot : N-Largest or N-Smallest from the **Plot Type** in the sidebar.
''')
st.sidebar.header('User Input Features')
st.sidebar.header('Range Slider') 
values = st.sidebar.slider(
     'Select a range of values',0,50,value=25)
st.sidebar.header('Plot Type') 
largest = st.sidebar.checkbox("Largest")
if largest:
    functionExecutor(n_largest_dict_maker,"Largest",final_df,values)
smallest = st.sidebar.checkbox("Smallest")
if smallest:
    functionExecutor(n_smallest_dict_maker,"Smallest",final_df,values)
st.markdown('''
## Plug:
 Thanks for going through this simple EDA application.
 
 You can follow me at [twitter](https://twitter.com/Mukilan_Krish) and [medium](https://medium.com/@mukilankrishnakumar2002)
 ''')
