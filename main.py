import requests
import pytube
from pytube import YouTube
import streamlit as st
from streamlit_lottie import st_lottie


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


puka = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_7ie89w61.json")
st.set_page_config(page_title="yt_downloader", page_icon=":sparkling_heart:", layout="wide")
st.subheader("this is youtube video downloader :wave:")
st.title("Download what you want from youtube for free")
st.write("##")
left_column, right_column = st.columns(2)
with left_column:
    st.subheader("what do we provide:")
    st.write("->zero ads")
    st.write("->high speeds")
    st.write("->unlimited downloads")
    st.write("##")
    st.write("##")
st.write("##")
st.write("##")
with right_column:
    st_lottie(puka, height=300)

url=st.text_input("enter the url")
st.button("download")
if(st.button("downlaod")):
    yt = YouTube(url)
    ys=yt.streams.get_lowest_resolution()
    ys.download()
