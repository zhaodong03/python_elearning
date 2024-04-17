import streamlit as st

tab1, tab2 = st.tabs(["Mac", "Windows"])

with tab1:
    st.header("Mac Python Installation")
    st.markdown('''
## Pre-Installed Check
Mac laptops usually come with Python pre-installed, to check if your MacBook has Python pre-installed:
Open terminal (you can search for terminal by clicking and command and space at the same time)
Type python --version and click return
If there is “python xx.xx.xx” like “Python 3.9.12” shown on the screen, this means you have Python already installed on your laptop, and you can jump to Install “Visual Studio Code” part

## Install Python
If you find Python is not installed on your machine, you can download Python from the official website: https://www.python.org/downloads/

You can choose any version of this course, but you need to make sure the operating system is macOS. Once downloaded, open the installer and follow the on-screen instructions to install Python. After the installation is complete, you can verify that Python is installed correctly by opening the Terminal and typing python --version, which could display the version of Python installed on your system

## Install Visual Studio Code
Visual Studio Code is a free, open-source code editor that supports many programming languages, including Python.
You can download it through the office website https://code.visualstudio.com/Download, make sure you are downloading for the macOS.Once the download is complete, open the downloaded file (.dmg) and drag the Visual Studio Code icon to the Applications folder to install it.

## Config Visual Studio Code
Open Visual Studio Code
Click the extension on the left bar (or press shift+command+x)
Search 'Python' in the search extensions
Download the first Python extension

## The first line of code
Create a file named 'HelloWorld' on your desktop
Drag this file to the Visual Studio Code
You will see the HelloWorld on the top left, move your mouse to the HelloWorld, you will see 4 icons, click the leftmost one to create a new file, named “helloworld.py”''')
    st.image('assets/installation/01.png')
    st.markdown('''
Type print("Hello World") in the helloworld.py, save the file by press command+S
Click the small triangle run button on the top right of the screen to run the code

You will see the Hello World be printed in the Output'''
)
    st.image('assets/installation/02.png')

with tab2:
    st.header("Windows Python Installation")
    st.markdown('''
## Install Python
You can download Python from the official website: https://www.python.org/downloads/, You can choose any version of this course, but you need to make sure the operating system is Windows. Once downloaded, open the installer and follow the on-screen instructions to install Python. Make sure you select the Install launcher for all users checkbox and the Add python.exe to PATH checkbox. After the installation is complete, you can verify that Python is installed correctly by opening the Terminal and typing python --version, which could display the version of Python installed on your system

## Install Visual Studio Code
Visual Studio Code is a free, open-source code editor that supports many programming languages, including Python.
You can download it through the office website https://code.visualstudio.com/Download, make sure you are downloading for Windows. Once the download is complete, open the downloaded file (.exe) and follow the onscreen instructions to install it.

## Config Visual Studio Code
Open Visual Studio Code
Click the extension on the left bar (or press Ctrl+Shift+X)
Search ‘Python’ in the search extensions
Download the first Python extension

## The first line of code
Create a file named ‘HelloWorld’ on your desktop
Drag this file to the Visual Studio Code
You will see the HelloWorld on the top left, move your mouse to the HelloWorld, you will see 4 icons, click the leftmost one to create a new file, named “helloworld.py”''')
    st.image('assets/installation/01.png')
    st.markdown('''
Type print("Hello World") in the helloworld.py, save the file by press command+S
Click the small triangle run button on the top right of the screen to run the code

You will see the Hello World be printed in the Output'''
)
    st.image('assets/installation/02.png')
    st.markdown('''
## Reference 
https://www.digitalocean.com/community/tutorials/install-python-windows-10
''')

