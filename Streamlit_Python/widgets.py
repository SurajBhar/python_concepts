import streamlit as st
import pandas as pd
import numpy as np

st.title("Text Input to Streamlit")

name = st.text_input("Enter your name:")

# Create a slider
age = st.slider("How old are you?", 0, 100, 25)
st.write(f"Your age is: {age}")

# Create a Selectbox
options = ["Python", "C++", "JAVA"]
choices = st.selectbox("Choose your facourite programming language", options)
st.write(f"Your favourite programming language is: {choices}")

if name:
    st.write(f"Hello, {name}!")

# Create a simple dataframe
df = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column' : [10,20,30,40]
})

# Display the dataframe
st.write("Here is the dataframe")
df.to_csv("sample_data.csv")
st.write(df)

# Create a Line Chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns = ['a', 'b', 'c']
)
st.line_chart(chart_data)

# Create an Upload Button for the file upload
uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt"])
if uploaded_file is not None:
    # Read the uploaded file
    data = pd.read_csv(uploaded_file)
    st.write(data)