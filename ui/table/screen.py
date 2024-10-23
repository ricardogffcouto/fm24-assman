import uuid

import streamlit as st
from ui.constants import ScreenName
from ui.table.filters import get_saved_filters, load_filter, save_filter
from ui.table.utils import display_dataframe
from ui.utils import navigate_to, download_as_csv_button


def save_filter_component(columns_state):
    filter_name = st.sidebar.text_input("Filter Name")
    if st.sidebar.button("Save Current Filter"):
        if filter_name:
            st.session_state.agGridKey = str(uuid.uuid4())
            save_filter(filter_name, columns_state)
            st.sidebar.success(f"Filter '{filter_name}' saved successfully!")
        else:
            st.sidebar.error("Please enter a filter name.")

def load_filter_component():
    saved_filters = get_saved_filters()
    selected_filter = st.sidebar.selectbox("Select a filter to load", [""] + saved_filters)
    if selected_filter and st.sidebar.button("Load Selected Filter"):
        loaded_filter = load_filter(selected_filter)
        if loaded_filter:
            st.session_state.columns_state = loaded_filter
            st.rerun()

def reset_filter_component():
    if st.sidebar.button("Reset Filter"):
        st.session_state.pop('columns_state', None)
        st.session_state.agGridKey = str(uuid.uuid4())

def show_table_screen(df):
    st.title("Search")

    # Initialize the grid key if it doesn't exist
    if "agGridKey" not in st.session_state:
        st.session_state.agGridKey = str(uuid.uuid4())

    # Initialize columns_state if not available in session_state
    if "columns_state" not in st.session_state:
        st.session_state["columns_state"] = None

    columns_state = st.session_state["columns_state"]

    # Display the data with AgGrid, capturing the columns state
    grid_response = display_dataframe(df, columns_state)

    # Ensure columns_state is not None
    if grid_response and grid_response['columns_state'] is not None:
        st.session_state["columns_state"] = grid_response['columns_state']

    save_filter_component(grid_response.get('columns_state', None))

    load_filter_component()

    download_as_csv_button(grid_response)

    # Add a button to go back to the main screen
    if st.button("Back to Main Screen"):
        navigate_to(ScreenName.MAIN)