import requests
import pytube
import pandas as pd 
import base64
from io import BytesIO
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
def main():
	path = st.text_input('Enter URL of any youtube video')
	option = st.selectbox(
     'Select type of download',
     ('audio', 'highest_resolution', 'lowest_resolution'))
	
	matches = ['audio', 'highest_resolution', 'lowest_resolution']
	if st.button("download"): 
		video_object =  YouTube(path)
		st.write("Title of Video: " + str(video_object.title))
		st.write("Number of Views: " + str(video_object.views))
		if option=='audio':
			video_object.streams.get_audio_only().download() 			
		elif option=='highest_resolution':
			video_object.streams.get_highest_resolution().download()
		elif option=='lowest_resolution':
			video_object.streams.get_lowest_resolution().download()
	if st.button("view"): 
		st.video(path) 
if _name_ == '_main_':
	main()
