import streamlit as st
import pandas as pd
import gettext
import os

# 设置 LC_MESSAGES 环境变量
os.environ['LC_MESSAGES'] = 'de_DE.UTF-8'


_ = gettext.gettext

localizor_DE = gettext.translation('base',localedir='locale',languages=['DE'])
localizor_DE.install()
localizor_EN = gettext.translation('base',localedir='locale',languages=['EN'])
localizor_EN.install()

st.dataframe(pd.read_csv('Sleep_health_and_lifestyle_dataset.csv'))
if st.button("DE"):
    _ = localizor_DE.gettext
if st.button("EN"):
    _ = localizor_EN.gettext
if st.button("Original"):
    _ = lambda s:s
st.title(_("标题"))
x="引用"
st.button(_("f函数里的button{x}"))
st.header(_("副标题"))
st.markdown(_("写在write里的文字。"))
st.markdown(_("markdown里的文字"))
