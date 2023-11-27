import streamlit as st
from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data():
    client = MongoClient("mongodb://localhost:27017/")  
    db = client["college_critic"] 
    collection = db["student_feedback"]  

    # Retrieve data from MongoDB collection
    cursor = collection.find({})
    data = pd.DataFrame(list(cursor))
    
    return data

def display():
    image1_path = "hostel1.jpg"
    image2_path = "hostel2.jpg"

# Display images side by side using columns
    col1, col2 = st.columns(2)

    with col1:
        st.image(image1_path, caption='Image 1', use_column_width=True)

    with col2:
        st.image(image2_path, caption='Image 2', use_column_width=True)
    df = load_data()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(df['Hostels'], bins=np.arange(1, 7), edgecolor='black', linewidth=1.2)


# Show the histogram using Streamlit's st.pyplot
    st.pyplot(fig)
    
if __name__ == "__main__":
    display()