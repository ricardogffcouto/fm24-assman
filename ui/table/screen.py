import uuid

import streamlit as st
from ui.constants import ScreenName
from ui.table.filters import save_filter, get_saved_filters, load_filter
from ui.table.utils import display_dataframe
from ui.utils import navigate_to, download_as_csv_button


def show_table_screen(df):
    st.title("Search")

    # Initialize the grid key if it doesn't exist
    if "agGridKey" not in st.session_state:
        st.session_state.agGridKey = str(uuid.uuid4())

    # Create buttons for saving, loading, and resetting
    col1, col2, col3 = st.columns(3)
    with col1:
        save_btn = st.button("Save columns state")
    with col2:
        load_btn = st.button("Load columns state")
    with col3:
        reset_btn = st.button("Reset Grid")

    # Handle button actions
    if reset_btn:
        st.session_state.agGridKey = str(uuid.uuid4())
        st.session_state.pop('columns_state', None)

    columns_state = st.session_state.get("columns_state") if load_btn else None

    # Display the data with AgGrid
    grid_response = display_dataframe(df, columns_state)

    # Save columns state if save button is clicked
    if save_btn:
        st.session_state.columns_state = grid_response['columns_state']

    download_as_csv_button(grid_response)

    # Add a button to go back to the main screen
    if st.button("Back to Main Screen"):
        navigate_to(ScreenName.MAIN)