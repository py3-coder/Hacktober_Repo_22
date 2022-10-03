# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 18:20:12 2021

@author: ankit
"""

import streamlit as st
import pickle
import numpy as np
model=pickle.load(open("model.pkl","rb"))

def predict_price(Manufacturer,IntelCore,Ram,HDD,SSD):
    prediction=model.predict([[Manufacturer,IntelCore,Ram,HDD,SSD]])
    print(prediction.round())
    return prediction

def main():
    st.title("Streamlit Tutorial")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Laptop Price Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    Manufacturer = st.text_input("Company { HP : 0 , Lenovo : 1 , ASUS : 2 , Dell : 3 } ","")
    IntelCore = st.text_input("IntelCore","")
    Ram = st.text_input("Ram(gb)","")
    HDD = st.text_input("HDD(gb)","")
    SSD = st.text_input("SSD(gb)","")
    
    if st.button("Predict"):
        output=predict_price(Manufacturer,IntelCore,Ram,HDD,SSD)
        st.success('Laptop Price is {}'.format(output.round()))

        

if __name__=='__main__':
    main()