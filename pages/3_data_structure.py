import streamlit as st

tab1, tab2, tab3 = st.tabs(["Objectives", "Course", "Assignment"])

with tab1:
    st.header("Module 2: Python Data Structure")
    st.markdown('''
    ## Course Objective:
    Diving deeper into Python, "Data Structures" is your next stop on this programming adventure. Python's data structures are like the compartments of a toolbox, each holding its own set of tools in an organized manner. With them, you can store, structure, and manipulate data efficiently—vital skills for any aspiring programmer.
    You'll explore lists, which are like arrays in other languages but with superpowers—being dynamic and able to hold different types of data. Tuples will introduce you to the concept of immutability, which is crucial for data that you want to remain unchanged. Then, there's dictionaries, Python’s approach to key-value storage, allowing you to create a mesh of related data that's quick to access and easy to understand. We’ll also cover sets, the go-to for unique collection needs, where duplication is a no-go. Throughout this module, we’ll highlight when and why you'd want to choose one structure over another, and how to use them to handle data effectively.
    By the end of this module, not only will you know how to use these structures, but you'll also understand how to pick the right one for your tasks, optimize data handling, and keep your code both efficient and elegant. Let's jump in and learn to organize our data with finesse!
    ## Course Sections
    Section 01: Lists and List Operations
    
    Section 02: Dictionaries and Key-Value Pairing
    ''')
with tab2:
    st.header("Module 2: Python Data Structure")
    st.markdown('''
    ## Section 01: Lists and List Operations
    In this section, "Lists and List Operations," you'll discover the versatility of Python lists. Lists in Python are ordered collections that are changeable and allow duplicate members. You'll learn how to create a list, access list items, change their values, loop through a list, and understand list comprehensions.
    
    ## Table of Content           
    - Creating a List
    - Accessing and Modifying Items
    - List Operations
    - Practice
    ## Creating a List
    - Below is an example of creating a list with square brackets and filling it with items of any data type. 1, 2, 3 are integers, whereas 'Python' is a string.''')
    
    st.image('assets/m2/01.jpg')
    st.markdown('''            
    ## Accessing and Modifying Items
    - You can use indices to access list items and modify them. Here is an example:
    ''')
    st.image('assets/m2/02.jpg')
    st.markdown('''
    
    ## List Operations
    - Python has methods of appending, extending, and removing items, as well as other list methods that are essential for list manipulation. Here is an example of appending to a list:
    ''')
    st.image('assets/m2/03.jpg')
    q1 = st.radio(
        "Which of the following is the correct way to make a LIST in python?",
        ["my_list = [1, 2, 3]", "my_list = (1, 2, 3)", "my_list = {1, 2, 3}", "my_list = 1, 2, 3"],
        index=None,
    )
    st.subheader("You must correctly answer the above quizz(es) to unlock the rest masterials")
    if q1 == 'my_list = [1, 2, 3]':
        st.markdown('''
    ## Section 02: Dictionaries and Key-Value Pairing
    In this section, "Dictionaries and Key-Value Pairing," you'll explore the Python dictionary, a collection of key-value pairs that allows you to store and retrieve data efficiently. Unlike lists, dictionaries are unordered and cannot be indexed by a number. Instead, they use unique keys to access values. This makes dictionaries ideal for representing real-world data in a structured way.
    ## Table of Content
    - Creating a Dictionary
    - Accessing and Modifying Dictionary Items
    - Dictionary Methods
    - Practice
    
    ## Creating a Dictionary
    - Below is an example of creating a dictionary where data is stored in key-value pairs. Here, 'name' and 'age' are keys, and 'Alice' and 25 are their corresponding values.
        ''')
        st.image('assets/m2/04.jpg')
        st.markdown('''
    ## Accessing and Modifying Dictionary Items
    - You can access values in a dictionary using their keys and modify them accordingly. Here is an example:
        ''')
        st.image('assets/m2/05.jpg')
        st.markdown('''
    ## Dictionary Methods
    - Python provides a variety of methods to work with dictionaries. Here is how you can add a new key-value pair to a dictionary and retrieve all the keys as a list:
            ''')
        st.image('assets/m2/06.jpg')
        
    rate = st.slider('Please Rate this module', 0, 3, 5)

with tab3:
    st.header("Assignment")
    st.markdown('''
    ## Assignment Objective: 
    Construct a Python script that demonstrates your grasp of lists and dictionaries. The script should accurately use these data structures to store predefined data, apply specific operations, and print expected results.

    ## Assignment Details:
    1. Header Comment:
        - Start your script with a header comment that includes the title of the assignment, your name, and the current date in the format YYYY-MM-DD.
    2. Declare a Dictionary:
        - Create a dictionary named capitals with the following key-value pairs:
            - 'China': 'Beijing'
            - 'Germany': 'Berlin'
            - 'France': 'Lyon'
    3. List Operation:
        - Append the color 'yellow' to the list colors.
        - Change the color 'blue' into 'white'.
    4. Dictionary Operation:
        Add a new key-value pair to the dictionary capitals with 'Australia' as the key and 'Canberra' as the value.
        A country in the dictionary was matched to the wrong capital. Correct the mistake in the country-capital pair. 
    5. Print Variables:
        - Print the colors list.
        - Print the capitals dictionary.
    ''')
    st.subheader('Upload Your Work')
    file = st.file_uploader('please upload your work here',['py'])

    st.subheader("Grade & Feedback")
    
    if file:
        st.markdown("**Your Grade is:** 80/100")
