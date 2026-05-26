import streamlit as st
import numpy as np

st.title("Streamlit profile app")
st.header("PB 711 Program")

name=st.text_input("Enter name : ")
age=st.slider("Select age",10,100)
gender=st.radio("Choose Gender",["Male","Female","Other"])
hobbies=st.multiselect("Select hobboies",["Reading","sports","travel"])
photo=st.file_uploader("Upload pic",type=["jpg","png","jpeg"])

if st.button("Submit profile : "):
    st.subheader("Profile deatils")
    st.write("Name : ",name)
    st.write("Age : ",age)
    st.write("Gender : ",gender)
    st.write("Hobbies : ",",".join(hobbies))
    if photo:
        st.image(photo,caption="profile pic",width=200)
