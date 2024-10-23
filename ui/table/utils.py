import streamlit as st

from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode, DataReturnMode

def display_dataframe(df, columns_state=None):
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(paginationAutoPageSize=True)
    gb.configure_side_bar()
    gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children")
    gridOptions = gb.build()

    grid_response = AgGrid(
        df,
        gridOptions=gridOptions,
        data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
        update_mode=GridUpdateMode.MANUAL,
        fit_columns_on_grid_load=False,
        theme='streamlit',
        height=500,
        width='100%',
        reload_data=True,
        allow_unsafe_jscode=True,
        key=st.session_state.agGridKey,
        columns_state=columns_state,
    )

    return grid_response