import streamlit as st
from deep_translator import GoogleTranslator
import speech_recognition as sr
from Microphone import mic
from Translation import translate_text
from speak_file import speak
from Speak_2 import speak_text

st.title("Real Time Two Person Translator")

# Session state for microphone control
if "listening" not in st.session_state:
    st.session_state.listening = False
    st.session_state.speaker = None


# Language Options
languages = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Russian": "ru",
    "Arabic": "ar",
    "Portuguese": "pt"
}

# ---------------- Sidebar ----------------

st.sidebar.title("Language Settings")

person1_language = st.sidebar.selectbox(
    "Person 1 Language",
    list(languages.keys()),
    key="p1"
)

person2_language = st.sidebar.selectbox(
    "Person 2 Language",
    list(languages.keys()),
    key="p2"
)


st.sidebar.markdown("---")

# Listening Status Indicator
st.sidebar.subheader("Microphone Status")

if st.session_state.listening:
    st.sidebar.error("🔴 Listening...")
else:
    st.sidebar.success("🟢 Microphone Idle")

# -----------------------------------------


# -----------------------------------------

st.subheader("Conversation")

# Buttons layout
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Person 1 Speak"):
        if not st.session_state.listening:
            st.session_state.listening = True
            st.session_state.speaker = "p1"

with col2:
    if st.button("Person 2 Speak"):
        if not st.session_state.listening:
            st.session_state.listening = True
            st.session_state.speaker = "p2"

with col3:
    if st.button("Stop Microphone"):
        st.session_state.listening = False
        st.session_state.speaker = None
        st.warning("Microphone Stopped")


# Listening Logic
if st.session_state.listening:

    st.write("Listening...")
    text = mic()

    st.write("Recognition...")

    # Person 1 speaking
    if st.session_state.speaker == "p1":

        st.write("Person 1 said:", text)

        source = languages[person1_language]
        target = languages[person2_language]

        translated_text = translate_text(source, target, text)

        st.write("Translated text:", translated_text)

        speak_text(translated_text, target)

    # Person 2 speaking
    elif st.session_state.speaker == "p2":

        st.write("Person 2 said:", text)

        source = languages[person2_language]
        target = languages[person1_language]

        translated_text = translate_text(source, target, text)

        st.write("Translated text:", translated_text)

        speak_text(translated_text, target)

    st.session_state.listening = False
