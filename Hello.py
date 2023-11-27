import streamlit as st
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["college_critic"]
collection = db["student_feedback"]

def main():
    st.title("College Critic App")
    st.write("Welcome to the College Critic App! Please login to continue.")
    
    st.write("To give ratings on facilities provided by SVECW follow the link:")
    
    # Create a Streamlit form
    with st.form("data_entry_form"):
        st.title("Data Entry Form")

        # Add form fields
        Classrooms = st.text_input("Classrooms:")
        Labs = st.text_input("Labs:")
        Network = st.text_input("Network:")
        Faculty = st.text_input("Faculty:")
        Hostels = st.text_input("Hostels:")
        Culturals = st.text_input("Culturals:")
        Sports = st.text_input("Sports:")
        Food = st.text_input("Food:")
        lib = st.text_input("Library:")
        clubs = st.text_input("Clubs:")

        # Create a submit button
        submit_button = st.form_submit_button(label="Submit")

        # Check if the form is submitted
        if submit_button:
            # Create a dictionary with the form data
            form_data = {
                "Classrooms": int(Classrooms),
                "Labs": int(Labs),
                "Network(wi-fi)": int(Network),
                "Faculty": int(Faculty),
                "Hostels": int(Hostels),
                "Culturals and Events": int(Culturals),
                "Food": int(Food),
                "Sports and Games": int(Sports),
                "Library": int(lib),
                "Clubs and Events": int(clubs)
            }

            # Insert the data into the MongoDB collection
            collection.insert_one(form_data)

            st.success("Data submitted successfully!")

if __name__ == "__main__":
    main()
