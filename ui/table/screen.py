import uuid

import streamlit as st
from ui.constants import ScreenName
from ui.table.columns import get_saved_columns, load_column, save_column
from ui.table.utils import display_dataframe
from ui.utils import navigate_to, download_as_csv_button


def save_column_component(columns_state):
    column_name = st.sidebar.text_input("Column Schema Name")
    if st.sidebar.button("Save Current Column Schema"):
        if column_name:
            st.session_state.agGridKey = str(uuid.uuid4())
            save_column(column_name, columns_state)
            st.sidebar.success(f"Column Schema '{column_name}' saved successfully!")
        else:
            st.sidebar.error("Please enter a column schema name.")

def load_column_component():
    saved_columns = get_saved_columns()
    selected_column = st.sidebar.selectbox("Select a column schema to load", [""] + saved_columns)
    if selected_column and st.sidebar.button("Load Selected Column Schema"):
        loaded_column = load_column(selected_column)
        if loaded_column:
            st.session_state.columns_state = loaded_column
            st.rerun()

def reset_column_component():
    if st.sidebar.button("Reset Column Schema"):
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

    save_column_component(grid_response.get('columns_state', None))

    load_column_component()

    download_as_csv_button(grid_response)

    # Add a button to go back to the main screen
    if st.button("Back to Main Screen"):
        navigate_to(ScreenName.MAIN)