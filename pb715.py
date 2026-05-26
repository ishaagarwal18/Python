import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

n=st.number_input("Enter number of random points : ",min_value=1,step=1)
if st.button("Generate graph"):
    x=[random.random() for _ in range(n)]
    y=[random.random() for _ in range(n)]

    plt.scatter(x,y)

    plt.show()
