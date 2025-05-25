import streamlit as st
from transcriber import transcribe_audio
from summarizer import summarize_text
import tempfile

st.set_page_config(page_title="Voice-to-Text Summarizer", layout="centered")

st.title(" Voice-to-Text Summarizer")
st.write("Upload an audio file or record voice, then get transcript + summary!")

# File uploader
uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a", "flac"])


if uploaded_file is not None:
    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    st.info("Transcribing audio with Whisper...")
    transcript = transcribe_audio(temp_path)
    
    st.subheader("Transcript")
    st.success(transcript)

    # Ask user if they want a summary
    if st.button("🔍 Summarize Transcript"):
        st.info("Summarizing...")
        summary = summarize_text(transcript)
        st.subheader("Summary")
        st.success(summary)
