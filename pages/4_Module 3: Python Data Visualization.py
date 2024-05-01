import streamlit as st

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.header("Module 3: Python Data Visualization")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("Objective")
    with col2:
        st.markdown("Section 01")
    with col3:
        st.markdown("Section 02")
    st.progress(33)
    st.markdown('''      
    ## Course Objective
    In this module, we will learn about data analysis and visualization using the libraries of pandas and seaborn. Pandas allows reading and processing CSVs, a spreadsheet file with columns separated by commas and rows by line breaks. Seaborn is a Python library that allows you to create plots effortlessly. An alternative is matplotlib, but matplotlib often requires more code to create simple plots.
    
    ## Course Sections
    Section 01: Pandas Library

    Section 02: Plotting''')

    st.button('Begin Module', type='primary', on_click=set_state, args=[1])

if st.session_state.stage == 1:
    st.header("Module 3: Python Data Visualization")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("Objective")
    with col2:
        st.markdown("Section 01")
    with col3:
        st.markdown("Section 02")
    st.progress(66)
    st.markdown('''
## Section 01: Pandas Library
To get started, download the [file](https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv) containing a dataset focused around survivors of the Titanic. I suggest using a jupyter notebook to write and run the code along with this module. Today, we will analyze the survival rate within the Titanic. First, some basic information about Pandas functions.

In order to utilize the library, we will need to import Pandas. To do so, simply type in''')
                
    st.image('assets/m3/01.jpg')   
    st.markdown('''
This line imports the pandas library and aliases it as “pd” allowing for faster usage. To load into the data, we simply use the function pd.read_csv. We also want to know what the data looks like, so we can use the function df.head() to display the first five rows of the data. Let's try it out. By default, it displays 5 rows, but you can also have it display more.
''')
    st.image('assets/m3/02.jpg')
    st.image('assets/m3/03.jpg')
    st.markdown('''
As you can see, this displays the first 5 rows of the data.The column we are most concerned with is “Survived”. To index into a column, we simply use the syntax of df[Name]. To index into a row, we use df.iloc[index]. Lets try it.
''')                
    st.image('assets/m3/04.jpg')
    st.image('assets/m3/05.jpg')
    st.markdown('''            
We can also index into rows with a condition. For example, if we want to find the first 5 rows where the passenger survived, we can use the following code.
''')
    st.image('assets/m3/06.jpg')
    st.image('assets/m3/07.jpg')
    st.markdown('''          
You can chain the indexing as well. For example, all rows within the first 10 rows where the passenger survives.
''')
    st.image('assets/m3/08.jpg')
    st.markdown('''

You can also display the number of rows and columns in the data by using the shape attribute.
''')
    st.image('assets/m3/09.jpg')

    
    q1 = st.radio(
        "Which of the followingf function should I use if I wish to see the Overview of the data",
        ["df.head()", "df.iloc[0]", "df.shape"],
        index=None,
    )
    st.subheader("You must correctly answer the above quizz(es) to unlock the rest masterials")
    if q1 == 'df.head()':
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("Objective")
        with col2:
            st.markdown("Section 01")
        with col3:
            st.markdown("Section 02")
        st.progress(100)
        st.markdown('''
## Section 02: Plotting

Now, let's do some plotting! To get started, import the seaborn library:
''')
        st.image('assets/m3/10.jpg')
        st.markdown('''     

The first thing that we might look at is the distribution of age among the inhabitants of the titanic.

Seaborn has a really cool function called histplot that allows us to generate a histogram:
''')               
        st.image('assets/m3/11.jpg')
        st.markdown('''     
We can also look at the distribution of age among the survivors and non-survivors. Let's try this by using the indexing method we learned earlier.
''')
        st.image('assets/m3/12.jpg')
        st.image('assets/m3/13.jpg')
        st.markdown('''     
We can also look at the distribution of sex among the survivors and non-survivors. Let's try this by using the indexing method we learned earlier.
''')
        st.image('assets/m3/14.jpg')
        st.markdown('''     

Looks like there were more men on the ship!.

Another interesting thing that we might want to look at is the correlation of fare and age. We can use the scatterplot function to do this.
''')
        st.image('assets/m3/15.jpg')
        st.image('assets/m3/16.jpg')

        st.markdown('''                         

Hmm, that wasn't very clear. Let's try to see if there is a correlation by using the regplot function.
''')
        st.image('assets/m3/17.jpg')
        st.markdown('''     

Looks like older people generally paid higher prices to be on the ship!

Maybe we can find more interesting things by coloring the points by the survival status of the passenger.
                    
''')
        st.image('assets/m3/18.jpg')
        st.markdown('''     

It appears that we lived in less equal times! Those who paid higher fares tended to survive more. Finally, let's learn one last important graph: the box plot.

Let's take a look at how the age is distributed among the passengers. Just for fun. Recall that a boxplot shows the minimum, first quartile, median, third quartile, and maximum of a dataset.
''')                  
        st.image('assets/m3/19.jpg')

        st.subheader('Congraduation! You have successfully Complete the Entire Course')
        rate = st.slider('Please Rate this module', 0, 3, 5)

    
    st.button('Back to Objective', on_click=set_state, args=[0])

