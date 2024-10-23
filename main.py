import streamlit as st

from ui.constants import ScreenName
from ui.upload_screen import show_upload_screen
from ui.load_screen import show_load_screen
from ui.table_screen import show_table_screen
from ui.utils import navigate_to

st.set_page_config(layout="wide")

def initialize_session_state():
    if 'current_screen' not in st.session_state:
        st.session_state.current_screen = ScreenName.MAIN
    if 'df' not in st.session_state:
        st.session_state.df = None

def show_main_screen():
    st.title('Football Manager 24 - Assistant Manager')
    tab1, tab2 = st.tabs(["Upload File", "Load File"])
    with tab1:
        show_upload_screen()
    with tab2:
        show_load_screen()

def screen_handler():
    initialize_session_state()

    if st.session_state.current_screen == ScreenName.MAIN:
        show_main_screen()
    elif st.session_state.current_screen == ScreenName.TABLE:
        if st.session_state.df is not None:
            show_table_screen(st.session_state.df)
        else:
            st.error("No data to display. Please upload or load a file first.")
            if st.button("Back to Main Screen"):
                navigate_to(ScreenName.TABLE)
    else:
        st.error(f"Unknown screen: {st.session_state.current_screen}")
        if st.button("Back to Main Screen"):
            navigate_to(ScreenName.TABLE)

def main():
    screen_handler()

if __name__ == "__main__":
    main()
