import streamlit as st

tab1, tab2, tab3 = st.tabs(["Course Objectives", "Course", "Assignment"])

with tab1:
   st.header("Course Objectives")

with tab2:
   st.header("Course")

with tab3:
   st.header("Assignment")
