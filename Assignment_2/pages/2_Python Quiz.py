## Notes

import streamlit as st
st.session_state.count = 0
st.session_state.flag = False


st.title('Python Quiz')

Q1 = st.radio('Question 1: Python is a snake and nothing else',
              ["True","False"])

Q2 = st.radio("Question 2: What class is a whole number ex. 7?",["String","Float",
                "Integer","None (right?)"])

st.write("Question 3: How do you get an input from a user? (select all that apply)")
Q3_1 = st.checkbox("input()")
Q3_2 = st.checkbox("int(input())")
Q3_3 = st.checkbox("input_value()")
Q3_4 = st.checkbox("I don't know how to code")
# Q3 logic

Q4 = st.multiselect("Question 4: Which way is the correct way to iterate a For loop 9 times? (select all that apply)",
              ["for j in range(10):","for j in range(9):","for j in range(0,9):"
               ,"I have never typed a line of code before"])

Q5 = st.radio("Question 5: Why do we use While loops?",["They're easy",
            "We don't know how long the loop needs to run",
            "We know EXACTLY how long the loop needs to run",
            "I wish I paid more attention in class"])

st.radio("Question 6: Here's a freebie: what does print('Hello world') output?",
         ["Not this one","Nope","Hello world","Too far"])

st.divider()


if st.button("Submit"):
    st.session_state.flag = True
    st.write("Your score is " + str(st.session_state.count) + " out of 6")
    if st.session_state.count == 6:
        st.balloons()

