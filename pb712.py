import streamlit as st
import numpy as np

st.title("Streamlit Vaccination app")
st.header("Pb 712 Program")

with st.sidebar:
    country=st.selectbox("Select country",['India','USA','UK','Canada'])
totalpopulation=st.number_input("Total population",min_value=1)
vaccinated=st.number_input("Total Vaccinated",min_value=0)

if st.button("calculate percentage"):
    percentage=(vaccinated/totalpopulation)*100
    st.write(f"Vaccination Rate for{country} is {percentage:2f}")

    st.progress(min(int(percentage),100))

    if percentage>=70:
        st.success("Good Vaccination coverage")
    else:
        st.warning("poor Vaccination")
