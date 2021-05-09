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
