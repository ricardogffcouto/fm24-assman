import streamlit as st
from ui.constants import ScreenName
from ui.utils import display_dataframe, navigate_to

def show_table_screen(df):
    st.title("Search")
    
    # Display the data
    grid_response = display_dataframe(df)

    # Option to download the data as CSV
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='data.csv',
        mime='text/csv',
    )

    # Add a button to go back to the main screen
    if st.button("Back to Main Screen"):
        navigate_to(ScreenName.MAIN)
