from gtts import gTTS
from gtts.lang import tts_langs
from deep_translator import GoogleTranslator
import streamlit as st

st.set_page_config(page_title="Multilingual TTS", page_icon="🎙️")

st.title("🌍 Multilingual Translator & Text-to-Speech")

#user_input
text = st.text_area("Enter Text")

# Get all supported languages
languages = tts_langs()

# Language dropdown
selected_language = st.selectbox(
    "Choose Output Language",
    sorted(languages.values())
)

if st.button("Generate Speech"):

    if text:

        # Get language code from language name
        lang_code = next(
            code for code, name in languages.items()
            if name == selected_language
        )

        # Translate text
        translated_text = GoogleTranslator(
            source='auto',
            target=lang_code
        ).translate(text)

        # Show translated output
        st.subheader("Translated Text")
        st.success(translated_text)

        # Generate speech
        tts = gTTS(
            text=translated_text,
            lang=lang_code
        )

        filename = "audio.mp3"
        tts.save(filename)

        # Play audio
        with open(filename, "rb") as file:
            st.audio(file.read(), format="audio/mp3")

    else:
        st.warning("Please enter some text.")