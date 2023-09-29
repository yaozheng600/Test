import streamlit as st
import pandas as pd
import gettext
import os


# 获取所有环境变量
env_vars = os.environ

# 打印所有环境变量及其值
for key, value in env_vars.items():
    st.write(f"{key}: {value}")



_ = gettext.gettext

localizor_DE = gettext.translation('base',localedir='locale',languages=['de'])
localizor_DE.install()
localizor_EN = gettext.translation('base',localedir='locale',languages=['en'])
localizor_EN.install()

st.dataframe(pd.read_csv('Sleep_health_and_lifestyle_dataset.csv'))
if st.button("de"):
    _ = localizor_DE.gettext
if st.button("en"):
    _ = localizor_EN.gettext
if st.button("Original"):
    _ = lambda s:s
st.title(_("标题"))
x="引用"
st.button(_("f函数里的button{x}"))
st.header(_("副标题"))
st.markdown(_("写在write里的文字。"))
st.markdown(_("markdown里的文字"))
