import streamlit as st
from streamlit_extras.switch_page_button import switch_page

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.header("Module 1: Python Syntax")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("Objective")
    with col2:
        st.markdown("Section 01")
    with col3:
        st.markdown("Section 02")
    with col4:
        st.markdown("Assignment")
    st.progress(25)
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
    st.button('Begin Module', type='primary', on_click=set_state, args=[1])

if st.session_state.stage == 1:
    st.header("Module 1: Python Syntax")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("Objective")
    with col2:
        st.markdown("Section 01")
    with col3:
        st.markdown("Section 02")
    with col4:
        st.markdown("Assignment")
    st.progress(50)
    st.markdown('''
    ## Section 01: Basic Syntax and Comments
    In this lesson, "Basic Syntax and Comments," you'll take your first steps into writing clean and readable code. Python is known for its straightforward syntax, often compared to the English language, which makes it an excellent language for beginners.

    You will learn about the structure of a Python program, which serves as the backbone of your coding journey. We’ll demystify how Python uses whitespace to organize code, a feature that makes Python unique. This concept, called indentation, is not just about making your code look pretty — it’s essential for your program to run correctly.

    In addition, you'll discover the art of commenting your code. Comments are the silent guides that talk to you and other programmers, explaining what the code does and why certain decisions were made. They are crucial for teamwork and maintaining code in the long run.

    By the end of this lesson, you'll be able to craft a simple Python program and understand the importance of comments in making your code understandable. Let’s get started and write some beautiful Python code!

    ## Table of Content
    - Structure of a Python program
    - Understanding indentation
    - Writing comments
    - Exercise -- Writing first Python Program
    - Quiz


    ## Structure of a Python Program        
    - Python programs are composed of lines of code and follow a specific syntax.
    - A simple Python script often starts with imports (if any), followed by definitions of functions and classes, and finally the main code body.
    - Example of a basic Python program structure:
''')
    st.image('assets/m1/01.jpg')

    st.markdown('''
    ## Understanding Indentation
    - Indentation refers to the spaces at the beginning of a code line.
    - In Python, indentation is crucial as it defines the scope of loops, functions, classes, and conditionals (like if statements).
    - Consistent indentation is key; Python does not allow mixing tabs and spaces.
    - Example of correct and incorrect indentation:
        - Correct:''')
    st.image('assets/m1/02.jpg')
    st.markdown('''
        - Incorrect:
    ''')
    st.image('assets/m1/03.jpg')       
    ## Writing Comment
    st.markdown('''
    - Comments are lines that are not executed and are used to explain the code.
    - Single-line comments: Start with a hash character (#) and extend to the end of the line.
        - Example:''')
    st.image('assets/m1/04.jpg')
    st.markdown('''
    - Multi-line comments: While Python does not have a direct way to create multi-line comments, you can use a multi-line string (triple quotes) that is not assigned to a variable.
        - Example:''')
    st.image('assets/m1/05.jpg')
    st.markdown('''
    ## Quiz
    ### Quiz 01: Section 01 -- Getting Started with Python Programming
    ''')
    q1 = st.radio(
        "What is the correct way to start a single-line comment in Python?",
        ["// This is a comment", "/* This is a comment */", "\# This is a comment", "<!-- This is a comment -->"],
        index=None,
    )
    st.subheader("You must correctly answer the above three quizzes to unlock the rest masterials")
    if q1 == "\# This is a comment":
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("Objective")
        with col2:
            st.markdown("Section 01")
        with col3:
            st.markdown("Section 02")
        with col4:
            st.markdown("Assignment")
        st.progress(75)
        st.markdown('''
    ## Section 02: Variables and Data Types
    In this section, we will dive into how you can declare variables and the simplicity behind Python’s dynamic typing. We’ll explore the core data types that are foundational to programming in Python: integers for whole numbers, floating-point numbers for decimals, strings for text, and booleans for truth values.

    Understanding these basics is like learning the alphabet before writing sentences. Once you grasp these concepts, you’ll be well on your way to creating more complex and powerful Python programs. Let's get started and discover the simplicity and power of Python's variables and data types!

    ## Table of Content
    - Declaring and Using Variable
    - Common Data Types
    - Dynamic Data Types
    -Quiz
    ## Declaring and Using Variables
    In Python, variables are like containers for storing data values. Unlike other programming languages, there is no need to declare the type of variable; it is inferred from the value it is assigned.

    To create a variable, you simply assign it a value using the equals sign (=).

    Example:''')
        st.image('assets/m1/06.jpg')
        st.markdown('''
    
                    
    Python has a set of built-in data types that define the type of value a variable can hold. Here are the most common ones:
                    
    Integers (int)
                    
    Whole numbers without a fractional part.
                    
    Example:
    
    > age = 21
                    
    Floating-Point Numbers (float)

    Numbers with a decimal point or in exponential form.

    Example:
    > temperature = 98.6

    Booleans (bool)
    
    Represents True or False values and is used to perform logical operations.

    Example:  

    >is_active = False     

    ## Dynamic Typing in Python
    - Python is dynamically typed, which means you don't have to explicitly declare the data type of a variable. The type can change as the assignment to the variable changes.
    - This feature allows for greater flexibility, but it also means that you need to be aware of the type of value your variables are holding.
    - Example of dynamic typing:
''')
        st.image('assets/m1/07.jpg')
        rate = st.slider('Please Rate this module', 0, 3, 5)

        st.button('Continue to Assignment', type='primary', on_click=set_state, args=[2])

    st.button('Back to Objective', on_click=set_state, args=[0])


if st.session_state.stage == 2:
    st.header("Module 1: Python Syntax")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("Objective")
    with col2:
        st.markdown("Section 01")
    with col3:
        st.markdown("Section 02")
    with col4:
        st.markdown("Assignment")
    st.progress(100)
    st.markdown('''         
    ## Assignment Objective: 
    Create a Python script that demonstrates the use of basic syntax, comments, variables, and data types. Your script will act as a journal entry for your first week of learning Python, summarizing what you have learned and storing various pieces of information as Python variables.
    
    ## Assignment Details:
                
    1. Create a Header Comment:
    At the beginning of your script, include a header comment with the title of the assignment, your name, and the date.
    2. Declare Variables:
    - Declare a string variable to store the title of the module.
    - Declare an integer variable to count the number of lessons completed.
    - Declare a float variable to estimate how much of the module you understand as a percentage.
    - Declare a boolean variable to state whether you have completed the assignment or not.
    3. Add Descriptive Comments:
    For each variable declaration, add a line comment that explains what the variable represents.
    4. Print Variables:
    Use the print function to output each variable on a separate line.
    Include a string literal before printing each variable to describe what is being printed.''')
    
    st.subheader('Upload Your Work')
    file = st.file_uploader('please upload your work here',['py'])

    st.subheader("Grade & Feedback")
    
    if file:
        st.markdown("**Your Grade is:** 100/100")
    st.button('Back to Module', on_click=set_state, args=[1])
    if st.button('Continue to Next Module', type='primary'):
        st.session_state.clear()
        switch_page('Module 2: Python Data Structure')
