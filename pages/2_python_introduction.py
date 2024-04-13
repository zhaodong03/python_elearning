import streamlit as st

tab1, tab2, tab3 = st.tabs(["Objectives", "Course", "Assignment"])

with tab1:
   st.header("Module 1: Python Syntax")
   st.markdown('''
## Course Objectives
               
In this lesson, "Basic Syntax and Comments," you'll take your first steps into writing clean and readable code. Python is known for its straightforward syntax, often compared to the English language, which makes it an excellent language for beginners.

You will learn about the structure of a Python program, which serves as the backbone of your coding journey. We'll demystify how Python uses whitespace to organize code, a feature that makes Python unique. This concept, called indentation, is not just about making your code look pretty — it's essential for your program to run correctly.

In addition, you'll discover the art of commenting your code. Comments are the silent guides that talk to you and other programmers, explaining what the code does and why certain decisions were made. They are crucial for teamwork and maintaining code in the long run.

By the end of this lesson, you'll be able to craft a simple Python program and understand the importance of comments in making your code understandable. Let's get started and write some beautiful Python code!             

## Course Sections
Section 01:  Basic Syntax and Comments
Section 02: Variables and Data Types             
''')
with tab2:
   st.header("Course")

with tab3:
   st.header("Assignment")
