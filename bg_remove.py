import streamlit as st


import numpy as np
from io import BytesIO
import base64
import os
import traceback
import time

st.set_page_config(layout="wide", page_title="Video Summarizer Tool")

st.write("## Summarize a video from YouTube URLs, MP3, M4A, WAV file")
st.write(
    ":dog: Try uploading a file to get a concise summary reoprt. Full text report can be downloaded from the sidebar.:grin:"
)
st.sidebar.write("## Upload and download :gear:")

# Increased file size limit
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

# Max dimensions for processing
MAX_VIDEO_SIZE = 2000  # pixels





def Sum(upload):
    try:
        start_time = time.time()
        progress_bar = st.sidebar.progress(0)
        status_text = st.sidebar.empty()

        status_text.text("Loading image...")
        progress_bar.progress(10)


        
        # Prepare download button
        st.sidebar.markdown("\n")
        st.sidebar.download_button(
            "Download fixed image", 
            convert_image(fixed), 
            "fixed.png", 
            "image/png"
        )

        

# UI Layout
col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an file or link", type=["png", "jpg", "jpeg"])

# Information about limitations
with st.sidebar.expander("ℹ️ Video Guidelines"):
    st.write("""
    - Maximum file size: xxxx MB
    - Large video will be automatically resized
    - Supported formats: URLs, MP3, M4A, MAV
    - Processing time depends on video size
    """)

# Process the image
if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error(f"The uploaded file is too large. Please upload an image smaller than {MAX_FILE_SIZE/1024/1024:.1f}MB.")
    else:
        fix_image(upload=my_upload)
else:
    # Try default images in order of preference
    default_images = ["./zebra.jpg", "./wallaby.png"]
    for img_path in default_images:
        if os.path.exists(img_path):
            fix_image(img_path)
            break
    else:
        st.info("Please upload an image to get started!")
