import streamlit as st
import pandas as pd
import pytube #pip install pytube
lista=st.text_input('Ingresá la playlist de YouTube:') 

if lista:
   videos = pytube.Playlist(lista)
   ctos=len(videos)
   todos={'Link':videos}
   df = pd.DataFrame(todos)

   st.table(df)
   
from pytube import Playlist
play_list = Playlist("https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Oj3ndXmNS1FFOUyQP-gEa")
print(len(play_list))

for link in play_list:
    print(link)
for video in play_list.videos:
    name = video.title
    print(name)
