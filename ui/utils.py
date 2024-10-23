import streamlit as st

def navigate_to(screen):
    st.session_state.current_screen = screen
    st.rerun()

def download_as_csv_button(grid_response):
    # Option to download the filtered data as CSV
    filtered_df = grid_response['data']
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download filtered data as CSV",
        data=csv,
        file_name='filtered_data.csv',
        mime='text/csv',
    )