def read_text_with_gtts(text, language='en'):
    from gtts import gTTS
    import os
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the speech to a temporary file
    tts.save("output.mp3")
    
    # Play the audio file (works on most systems)
    os.system("afplay output.mp3")

    # Optionally remove the temporary file
    os.remove("output.mp3")