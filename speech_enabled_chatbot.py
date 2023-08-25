# 1. First, import the necessary packages in your code. This includes nltk, streamlit, and speech_recognition.
import streamlit as st
import speech_recognition as sr
import nltk # for natural language processing tasks such as tokenization, lemmatization, and stopword removal.
# The ‘nltk.download()’ function is used to download additional resources needed for the nltk library. 
# In this case, we are downloading the punkt and averaged_perceptron_tagger resources. 
# These resources are needed for tokenization and part-of-speech tagging tasks.
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string # used for string operations

# Initialize recognizer class
r = sr.Recognizer()

# 2. Load the text file and preprocess the data using the chatbot algorithm.
with open('Climatic_Changes_Their_Nature_and_Causes2.txt', 'r', encoding='utf-8') as f:
    data = f.read().replace('\n', ' ')
# Tokenize the text into sentences
sentences = sent_tokenize(data)
# Define a function to preprocess each sentence
def preprocess(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    # Remove stopwords and punctuation
    words = [word.lower() for word in words if word.lower() not in stopwords.words('english') and word not in string.punctuation]
    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return words
# Preprocess each sentence in the text
corpus = [preprocess(sentence) for sentence in sentences]
# Define a function to find the most relevant sentence given a query
def get_most_relevant_sentence(query):
    # Preprocess the query
    query = preprocess(query)
    # Compute the similarity between the query and each sentence in the text
    max_similarity = 0
    most_relevant_sentence = ""
    for sentence in corpus:
        try:
            similarity = len(set(query).intersection(sentence)) / float(len(set(query).union(sentence)))
        except ZeroDivisionError:
            similarity = 0
        
        if similarity > max_similarity:
            max_similarity = similarity
            most_relevant_sentence = " ".join(sentence)
    return most_relevant_sentence

#3. Define a function to transcribe speech into text using the speech recognition algorithm.
def transcribe_speech(audio_text):
    st.info("Transcribing...")
    try:
        # using Google Speech Recognition
        text = r.recognize_google(audio_text)
        return text
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio."
    except sr.RequestError:
        return "Could not request results; check your network connection."

# 4. Modify the chatbot function to take both text and speech input from the user. 
# If the user provides text input, the chatbot should function as before.
# If the user provides speech input, the speech recognition algorithm should transcribe the speech into text, which is then passed to the chatbot.

def chatbot(user_input):
    if isinstance(user_input, str):
        # Si l'entrée est du texte
        # Find the most relevant sentence
        response  = get_most_relevant_sentence(user_input)
    elif isinstance(user_input, bytes):
        # Si l'entrée est un enregistrement audio (en bytes)
        text=transcribe_speech(user_input)
        response  = get_most_relevant_sentence(text)
    else:
        response = "Entrée non prise en charge."

    return response

# Fonction principale de l'application Streamlit
def main():
    st.title("Chatbot avec Entrée Textuelle et Vocale")
    st.write("Bienvenue dans notre application chatbot !")
    
    st.sidebar.header("Settings")
    option = st.sidebar.selectbox("Sélectionnez le mode d'entrée:", ["Texte", "Voix"])

    # add a button to start
    if st.button("Start "):

        if option == "Texte":
            user_entree = st.text_input("Vous pouvez taper votre question ici:")
        else:
            st.write("Cliquez sur le bouton et parlez pour poser votre question.")
            record = st.button("Enregistrez votre question")

            if record:
                # Reading Microphone as source
                with sr.Microphone() as source:
                    st.info("Speak now...")
                    # listen for speech and store in audio_text variable
                    user_entree = r.listen(source)
                st.success("Enregistrement terminé!")
                    
        response=chatbot(user_entree)
        st.write("Réponse du Chatbot:" + response)
    # st.write(response)

if __name__ == "__main__":
    main()






    
