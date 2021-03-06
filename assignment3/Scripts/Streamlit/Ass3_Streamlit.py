#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:05:50 2021

@author: rishab
"""


#Importing required libraries
from multiapp import MultiApp
import streamlit as st
import pandas as pd
import os

#Reading the required data
root_path = "C:\\Users\\prana\\Downloads\\img\\input_Images"
def asearch():
    st.title("Images using Artistic Style Similarity Search Method")
    st.write("-------------------------------------------------------------------------------------------------")

    def get_data():
        return pd.read_csv(r'C:\Users\prana\Downloads\img\Faiss_n.csv')

    n = 1
    df = get_data()
    images = df['0'].unique()
    # print("images == assearch ==",images)
    st.subheader("Choose an image from the dropdown : ")
    pic =  st.selectbox('Choices : ', images)
    print("os.path.join(root_path,pic)==",os.path.join(root_path,pic))
    st.image(os.path.join(root_path,pic), width=None)
    st.subheader('How Many Images do you want to see?')
    z = st.slider('How many images do you want to see?', 1, 10, 1)
    st.subheader("Similar Products you may want to buy")
    for index, row in df.iterrows():
        if row['0'] == pic:
            while n < z + 1:
                st.image(os.path.join(root_path,row[n]), width=100, caption=row[n])
                n += 1

def fbfa():
    st.title("Images using Facebook FAISS")
    st.write("-------------------------------------------------------------------------------------------------")

    def get_data():
        return pd.read_csv(r'C:\Users\prana\Downloads\img\Faiss_n.csv')

    n = 1
    df = get_data()
    images = df['0'].unique()
    st.subheader("Choose an image from the below menu: ")
    pic = st.selectbox('Choices : ', images)
    st.image(os.path.join(root_path,pic), width=None)
    st.subheader('Similar images to be shown?')
    z = st.slider('Similar images to be shown?', 1, 10, 1)
    st.subheader("Similar Products")
    for index, row in df.iterrows():
        if row['0'] == pic:
            while n < z + 1:
                st.image(os.path.join(root_path,row[n]), width=100, caption=row[n])
                n += 1

app = MultiApp()
app.add_app("Artistic Style Similarity Search", asearch)
app.add_app("Facebook FAISS", fbfa)
app.run()


# In[ ]:




