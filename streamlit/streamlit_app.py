"""
Discussion Topics
=====================
* Adding Interactive Components to a Streamlit App
* button, selectbox, checkbox, radio, toggle, latex
* Adding an image

"""

# We need the following modules
import streamlit as st
# from PIL import Image, ImageEnhance
# Needed for some image stuff import random as rng

st.title('Adding Interactive Components')

st.header('st.button')

# Let's add a button here

st.divider()

st.header('st.selectbox')

# Let's add a selection box here

st.divider()

st.header('st.checkbox + st.button')

st.write('What would you like to order?')

# Let's add some checkboxes here

st.divider()

st.header('st.radio + st.latex')

# Let's add some radio buttons and latex here

st.divider()

st.header('st.toggle + st.slider + st.image')

# Let's add a toggle button, slider and some image stuff here