import streamlit as st
import gettext


_ = gettext.gettext
localizor_DE = gettext.translation('base',localedir='https://github.com/yaozheng600/Test/blob/fe45434aa985780e3ba09d7b336992dcc0df6c44/locale',languages=['DE'])
localizor_DE.install()
localizor_EN = gettext.translation('base',localedir='https://github.com/yaozheng600/Test/blob/fe45434aa985780e3ba09d7b336992dcc0df6c44/locale',languages=['EN'])
localizor_EN.install()
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
