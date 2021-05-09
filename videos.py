import streamlit as st
import pandas as pd
import pytube #pip install pytube
videos = pytube.Playlist("https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Oj3ndXmNS1FFOUyQP-gEa")
ctos=len(videos)
todos={'Link':videos}
df = pd.DataFrame(todos)

st.table(df)
