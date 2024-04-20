import streamlit as st
import subprocess

def main():
    st.title("Hey, What are you Looking For??")

    st.write("Please select the Model you want to run:")

    project = st.radio("Select Project", ("Resume Ranking System", "Job Recommendation Model"))

    if st.button("Run"):
        if project == "Resume Ranking System":
            st.write("Running Resume Ranking System...")
            subprocess.run(["streamlit", "run", "modified.py"])  # Replace with the filename of your resume ranking system file
        elif project == "Job Recommendation Model":
            st.write("Running Job Recommendation Model...")
            subprocess.run(["streamlit", "run", "Job.py"])  # Replace with the filename of your job recommendation model file

if __name__ == "__main__":
    main()
