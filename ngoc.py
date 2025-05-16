import streamlit as st

st.title("NGOC - test")
st.write("This is a test for the NGOC app.")
st.write("this is a new test")

a = st.button("Click me!")
if a:
    st.write("you clicked the button!")
st.text_input("Enter some text:")
st.text_area("Enter some text:")
st.selectbox("Select an option:", ["Option 1", "Option 2", "Option 3"])
st.multiselect("Select multiple options:", ["Option 1", "Option 2", "Option 3"])
st.slider("Select a range:", 0, 100, (25, 75))
st.checkbox("Check this box")
st.radio("Select one option:", ["Option 1", "Option 2", "Option 3"])

st.write("This is a new test for the NGOC app.")

st.write("This is a new test for the NGOC app.")