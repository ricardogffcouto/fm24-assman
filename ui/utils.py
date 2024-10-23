import streamlit as st

def navigate_to(screen):
    st.session_state.current_screen = screen
    st.rerun()

def download_as_csv_button(grid_response):
    # Option to download the columned data as CSV
    columned_df = grid_response['data']
    csv = columned_df.to_csv(index=False)
    st.download_button(
        label="Download columned data as CSV",
        data=csv,
        file_name='columned_data.csv',
        mime='text/csv',
    )