import streamlit as st
import numpy as np

st.title("Streamlit marks Calculator app")
st.header("Pb 713 Program")

c1,c2,c3,c4,c5=st.columns(5)

m1=c1.number_input("FCSP: ",0,100,0)
m2=c2.number_input("FSD: ",0,100,0)
m3=c3.number_input("DE: ",0,100,0)
m4=c4.number_input("PS: ",0,100,0)
m5=c5.number_input("ETC: ",0,100,0)

if st.button("Calculate marks"):
    total=m1+m2+m3+m4+m5
    average=total/5

    if average>=60:
        division="First division"
    elif average>=40:
        division="Second division"
    else:
        division="Fail"
    with st.expander("Result"):
        st.write("Total marks" ,total)
        st.write("Average",average)
        st.write("Obtained grade",division)
