import streamlit as st
from utils.stt import transcribe_offline
from utils.diarization import diarize  # your LLM diarization logic here

def conversation_analysis_page():
    st.header("Conversation Analysis")
    audio_file = st.file_uploader("Upload Audio (wav ONly)", type=["wav"])
    
    if audio_file:
        with st.spinner("Transcribing audio..."):
            transcript_data = transcribe_offline(audio_file)
        transcript_text = transcript_data.get('text', transcript_data) if isinstance(transcript_data, dict) else transcript_data
        
        st.subheader("Transcript")
        st.text_area("", transcript_text, height=200)

        with st.spinner("Performing LLM-based diarization..."):
            diarized_text = diarize(transcript_text)
        
        st.subheader("Diarization")
        st.text_area("", diarized_text, height=200)
