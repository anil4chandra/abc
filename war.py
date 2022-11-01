import streamlit as st
import pandas as pd
st.title("csv display")
x=pd.read_csv("styles.csv")
spectra = pd.DataFrame(x)
st.write(spectra)
