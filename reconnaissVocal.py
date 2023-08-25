#1. Import Required Libraries
import streamlit as st
import speech_recognition as sr

# 2. Define the Speech Recognition Function
def transcribe_speech(api,lang,r):
    ## Initialize recognizer class
    #r = sr.Recognizer()
    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info("Speak now...")
        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        st.info("Transcribing...")
        if api == "Google Web":
            try:
                text = r.recognize_google(audio_text,language=lang)
                return text
            except sr.UnknownValueError:
                return "Google Speech Recognition could not understand audio"
            except sr.RequestError:
                return "Could not request results; check your network connection"
        elif api == "Google Cloud":
            try:
                text = r.recognize_google_cloud(audio_text,language=lang)
                return text
            except sr.UnknownValueError:
                return "Google Cloud Recognition could not understand audio"
            except sr.RequestError:
                return "Could not request results; check your network connection"
            
        elif api == "Microsoft Bing":
            try:
                text = r.recognize_bing(audio_text,language=lang)
                return text
            except sr.UnknownValueError:
                return "Microsoft Bing Recognition could not understand audio"
            except sr.RequestError:
                return "Could not request results; check your network connection"
        
        elif api == "IBM":
            try:
                text = r.recognize_ibm(audio_text,language=lang)
                return text
            except sr.UnknownValueError:
                return "IBM Recognition could not understand audio"
            except sr.RequestError:
                return "Could not request results; check your network connection"  
        
        #elif api == "Sphinx":
        #    try:
        #        text = r.recognize_sphinx(audio_text,language=lang)
        #        return text
        #    except sr.UnknownValueError:
        #        return " CMU Sphinx Recognition could not understand audio"
        #    except sr.RequestError:
        #        return "Could not request results; check your network connection"
        
        else:
            text = "Invalid API selection"
            
        return text
    
def save_to_file(transcription):
    with open("transcription.txt", "w") as file:
        file.write(transcription)
    st.success("Transcription saved to 'transcription.txt'")

# 3. Define the Main Function

def main():
    st.title("Speech Recognition App")
    st.write("Press 'Start Recording' to begin speech recognition.")
    st.sidebar.header("Settings")
    api_option = st.sidebar.selectbox("Select Speech Recognition API", ["Google Web", "Google Cloud", "Microsoft Bing","IBM"])
    # Language selection
    language = st.sidebar.selectbox("Select Language", ["en-US", "es-ES", "fr-FR"])
    # Initialize recognizer class
    r = sr.Recognizer()
    # add a button to trigger speech recognition
    if st.button("Start Recording"):
        text = transcribe_speech(api_option,language,r)
        st.write("Transcription: ", text)
        
        save_button = st.button("Save Transcription")
        if save_button:
            save_to_file(text)
            
    st.write("Press 'Pause' to pause speech recognition.")

    pause_button = st.button("Pause")

    if pause_button:
        st.write("Speech recognition paused.")
        r.pause_threshold = float("inf")  # Pause the recognizer

    st.write("Resume 'Pause' to Resume speech recognition.")
    resume_button = st.button("Resume")

    if resume_button:
        st.write("Resuming speech recognition.")
        r.pause_threshold = 0.8  # Adjust as needed

            
if __name__ == "__main__":
    main()