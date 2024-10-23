import streamlit as st
import os
from parser import read_file
from ui.constants import ScreenName
from ui.utils import navigate_to  # Assuming your parsing logic is in a separate file

def show_upload_screen():
    st.header("Upload New File")
    uploaded_file = st.file_uploader("Choose an HTML file", type="html")

    if uploaded_file is not None:
        # Save the uploaded file
        file_path = os.path.join('data', uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"File saved: {file_path}")

        # Parse the file
        file_name = uploaded_file.name.split('.')[0]
        df = read_file(file_name)

        # Store the DataFrame in session state
        st.session_state.df = df
        navigate_to(ScreenName.TABLE)
