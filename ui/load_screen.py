import streamlit as st
import pandas as pd
import os

from ui.constants import ScreenName
from ui.utils import navigate_to

def show_load_screen():
    st.header("Load Existing File")
    # Get list of parquet files in the data directory
    parquet_files = [f for f in os.listdir('data') if f.endswith('.parquet')]
    
    if not parquet_files:
        st.warning("No parquet files found in the data directory.")
    else:
        selected_file = st.selectbox("Select a file to load", parquet_files)
        
        if st.button("Load Selected File"):
            # Load the selected parquet file
            df = pd.read_parquet(os.path.join('data', selected_file))
            
            # Store the DataFrame in session state
            st.session_state.df = df
            navigate_to(ScreenName.TABLE)
