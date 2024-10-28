import streamlit as st

def main():
    st.header("About Me")
    col1, col2 = st.columns(2)
    with col1:
        user_choice = st.selectbox("Enter what you want to view", ["Education Background", "Work Experience", "Skills", "Certifications"])
        if user_choice == "Education Background":
            st.write("1. Multimedia University of Kenya")
            st.write("Bachelor of Science in Computer Science")
            st.write("September 2020 - April 2024")
            st.divider()
            st.write("2. Nairobi School")
            st.write("Grade - A-")
            st.write("February 2016 - November 2019")
            st.divider()
            st.write("3. Nyeri Good Shepherd Academy")
            st.write("427 Marks")
            st.write("January 2014 - November 2015")
        elif user_choice == "Work Experience":
            st.write("1. eMobilis Technology Training Institute")
            st.write("Data Science Lecturer")
            st.write("September 2024 - Present")
            st.divider()
            st.write("2. Taka Earth")
            st.write("Data Scientist")
            st.write("June 2023 - August 2024")
            st.divider()
            st.write("3. Axum Enterprises")
            st.write("Python Developer")
            st.write("January 2023 - September 2023")
            st.divider()
            st.write("4. Calltronix")
            st.write("IT Support")
            st.write("May 2022 - July 2022")
        elif user_choice == "Skills":
            st.write("1. Python Programming")
            st.write("2. Machine Learning")
            st.write("3. Computer Vision")
            st.write("4. Natural Language Processing")
            st.write("5. Reinforcement Learning")
            st.write("6. Recommendation Systems")
        elif user_choice == "Certifications":
            st.write("1. IBM")
            st.write("Data Science Practitioner")
            st.write("May - October 2023")
            st.divider()
            st.write("2. Stanford University")
            st.write("Machine Learning Engineering")
            st.write("February - June 2023")
            st.divider()
            st.write("3. ALX")
            st.write("Data Analytics")
            st.write("May - December 2023")
    with col2:
        name = st.text_input("Enter your name")
        email = st.text_input("Enter your email address")
        remarks = st.text_area("Enter your remarks")
        if st.button("Submit"):
            st.toast(f'Thank you {name} for sharing your remarks!', icon='👊')

if __name__ == "__main__":
    st.set_page_config(
        page_title="Peter Gachuki Portfolio",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    main()