import streamlit as st
from streamlit.logger import get_logger
from streamlit_extras.switch_page_button import switch_page


LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Python E-learning",
        page_icon="",
    )

    st.write("# Welcome to Python e-Learning! 👋")

    st.markdown(
        """
        ## Overview

Are you ready to unlock the power of data analysis and visualization with Python through hands-on programming experience? Whether you’re a complete beginner or have limited programming experience, this Python eLearning course is here to guide you through the essentials of Python programming tailored for beginners to improve their working and learning efficiency.

## Why Python?
Python is a high-level programming language that become one of the most popular programming languages due to its simplicity, readability, and versatility. Python is used in a wide range of fielding including web development, data analysis, AI, machine learning, and etc. This course chose Python as the programming language because it is beginner-friendly, versatile, has a strong community and resources, and is FREE. 

## What You'll Learn?
1. Python Syntax: Get comfortable with Python syntax and write your first code
2. Python Data Structures: Learn how you could store data in Python and how to manipulate them
3. Python Data Analysis Visualization: Learn how to utilize various different Python libraries to analyze and visualize your data 

## Who Is This For?
1. Complete Beginners: If you have zero programming experience but want to learn Python, this is the perfect place to start
2. Non-Technical Professionals: Whether you're a marketer, business analyst, or researcher, learning Python through this course would supercharge your data skills and career prospects
3. Students: If you're a student looking to add valuable programming skills to your toolkit, this course provides a solid foundation in Python programming for data work.

## How to Use This Learning Platform
Firstly, please follow the Python Installation instructions to ensure all required toolkits are correctly installed on your machine. Then you could click the first module to begin your programming journey

For each module, there are three sections “Objectives”, “Course”, and “Assignment”. You can find the corresponding tab on the top of the screen, and you can click each tab to jump between them. Under the “Objectives” section, you will find what you will learn after accomplishing this module. The “Course” section contains the main course material for this section. Note that there may be pop quizzes in the material, you have to correctly answer the quiz to proceed. Finally, the “Assignment” section gives you the opportunity to test yourself through hands-on coding experience. Upload your code and our Autograder will grade your assignment and provide you feedback.

    """
    )
    if st.button("**Start Your Journey NOW.**", type="primary"):
        switch_page('Python Installation')

if __name__ == "__main__":
    run()