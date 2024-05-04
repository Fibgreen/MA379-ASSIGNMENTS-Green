## Notes
# Almost done, make it look pretty
# Add some images

import streamlit as st

st.title('About Me')
st.divider()

st.header('Name')
st.write('Connor S. Green')

st.header('Birthday')
st.write("March 9th, 2000")

st.header('Hometown')
st.write('Norfolk, VA')

st.header('Hobbies')
st.write('Sailing')
st.image('sailing.JPG')
st.write('Racing')
st.image('racing.png')

st.header('Career Goals')
st.write('After graduation I will commission into the Navy and go '
         'to flight school')

st.header('ME!')
st.image('me.png')

