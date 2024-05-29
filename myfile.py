import pickle
import streamlit as st

model1=pickle.load(open("area.pkl","rb"))

def myf1():
    st.title("Area Price Prediction")
    area=st.number_input("Enter the area value...")
    pred=st.button("Predict")
    
    if pred:
      op=model1.predict([[area]])
      st.write("price of the area is:",op[0])
    
myf1()
    