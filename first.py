import streamlit as st

st.set_page_config(page_title='Hello streamlit', layout="centered")

st.title("Welcome to streamlit 👌")
st.header("This is header")
st.subheader("This is subheader")

st.text("This is st.text")
st.write("This is st.write")
st.markdown("This is `st.markdown`")

code='''
def add(a,b):
    return a+b
print(add(5,6))

'''

st.code(code,language='python')

####### Sidebar, columns and expanders

st.sidebar.header("profile setting")
name=st.sidebar.text_input("Faculty name")
dep=st.sidebar.selectbox("Department",['CE','CST','IT'])

col1,col2=st.columns([1,2])

with col1:
    st.write("Basic info")
    st.write(name,dep)

with col2:
    st.subheader("About")

with st.expander("subjects taught"):
    st.write("python,FSD,DE")



##### forms and inputs
name=st.text_input("Enter name")
age=st.number_input("Age",0,80,18)
rating=st.slider("Rating",1,10,5)

if name:
    st.write(f'Hello {name}')


##### Section widgets

course=st.selectbox("Course",['Python','FSD','DE'])
days=st.multiselect('Preferred Days',['Mon','Tue','Thur'])
lec=st.radio('lecture no',[1,2,3])

#### Date time and file upload

from datetime import date,time

examdate=st.date_input("Exam Date",date.today())
starttime=st.time_input("Start time",time(14,0))
file=st.file_uploader("upload CSV",type=["CSV"])


###### Media display

st.subheader("Image display")
st.image(
    "ss.jpg",
    caption='Random image',
    # use_container_width=True
)


###### Audio file

# st.subheader("Audio example")
# st.audio(myaudio.mp3)

st.subheader("Video example")
st.video("E:\Pictures\Isha\CC54EEB9-805C-4CA6-BCC3-C46F138DF89B.MP4")


###### Creating and displaying data

import pandas as pd
data={
    "Student":['A','B','C','D'],
    "Marks": [85,90,76,24],
    "Passed": [True,True,True,False]
}

df=pd.DataFrame(data)

## display dataframe
st.header('st.dataframe')
st.dataframe(df)

## display table
st.header("static table")
st.table(df)

## json-javascript object notation data
st.header("json data")
st.json(data)

##### status and running tasks
st.info("Useful information")
import time

if st.button("start long run"):
    progress=st.progress(0)
    with st.spinner("Proccessing"):
        for i in range(100):
            time.sleep(0.03)
            progress.progress(i+1)

    st.success("Task completed")


##### Matplotlib charts

import matplotlib.pyplot as plt
import numpy as np

st.subheader("matplotlib based line chart")
x=np.arange(1,11)
y=np.random.randint(50,100,size=10)

plt.plot(x,y,'o')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("A line chart based on matplotlib")

st.pyplot(plt)

############ STREAMLIT BASED LINE CHART #####################

df1=pd.DataFrame({
    "Student":x,
    "Marks":y
})
st.line_chart(df1)
