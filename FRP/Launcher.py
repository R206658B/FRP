import streamlit as st
from datetime import datetime
import pandas as pd

st.set_page_config(
    page_title="Attendance System", page_icon="C:\\Users\\Charles\\Desktop\\FRP\\coh_logo.png", layout="wide"
)

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("C:\\Users\\Charles\\Desktop\\FRP\\coh_logo.png", width=155)

st.header(':rainbow[KANZURU ATTENDANCE SYSTEM!] :city_sunrise:', divider='rainbow')
st.image("C:\\Users\\Charles\\Desktop\\FRP\\rowan_martin.jpg")

