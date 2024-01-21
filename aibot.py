import speech_recognition as sr
import pyttsx3

def get_voice_input():
    try:
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=6)

        print("Processing...")

        # Recognize speech using Google Speech Recognition
        command = recognizer.recognize_google(audio).lower()
        return command

    except sr.UnknownValueError:
        error_message = "Could not understand audio. Please say again."
        print(error_message)
        return None
    except sr.RequestError as e:
        error_message = f"Could not request results from Google Speech Recognition service; {e}"
        print(error_message)
        return None
    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        return None

def respond_to_query(query, user_name=None):
    # Simple rule-based responses
    if "hello" in query:
        return "Hello! How can I assist you today?"
    elif "what is your name?" in query:
        return "My name is anondgr AI assistant."  
    elif "how are you" in query:
        return "I'm just a computer program, but thanks for asking!"
    elif "bye" in query:
        return "Goodbye! Have a great day."
    elif "who created you" in query or "who developed you" in query or "who is your developer" in query:
        return "My developer is Mr. Rajan Kumar."
    elif "what can you do" in query:
        return "I can chat with you."
    elif "let's chat" in query:
        return "Thanks for chatting with me. What is your name?"
    elif "what is your name" in query:
        return "My name is anondgr AI assistant. What's your name?"
    elif "hello" in query.lower() and "my name is" in query.lower():
        # Extracting the user's name from the query
        user_name = query.split("my name is")[-1].strip()
        return f"Hello, {user_name}!"
    elif user_name is not None:
        return f"Hello, {user_name}! How can I assist you?"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def voice_chat():
    while True:
        query = get_voice_input()

        if query:
            response = respond_to_query(query)
            print("Bot:", response)
            speak(response)

# Start the voice chat
voice_chat()
