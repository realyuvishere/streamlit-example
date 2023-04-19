import streamlit as st

n1 = st.number_input('Enter first number')
n2 = st.number_input('Enter second number')
n3 = st.number_input('Enter third number')

the_max = max(n1, max(n2, n3))
st.write(f'The max of the given three numbers is {the_max}')