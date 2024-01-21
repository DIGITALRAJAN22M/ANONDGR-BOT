import speech_recognition as sr
import os
import pyttsx3
import webbrowser

def open_application(command):
    if "open whatsapp" in command:
        # Replace with the actual path to your WhatsApp executable
        whatsapp_path = r"C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2401.3.0_x64__cv1g1gvanyjgm\WhatsApp.exe"
        os.system(whatsapp_path)
        return "WhatsApp"
    elif "open explorer" in command:
        os.system("explorer.exe")
        return "File Explorer"
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com/")
        return "YouTube"
    elif "open chrome" in command:
        # Replace with the actual path to your Chrome executable
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.system(chrome_path)
        return "Google Chrome"
    elif "open vmware" in command:
        # Replace with the actual path to your VMware executable
        vmware_path = r"C:\Program Files (x86)\VMware\VMware Workstation\vmware.exe"
        os.system(vmware_path)
        return "VMware"
    elif "open firefox" in command:
        # Replace with the actual path to your Firefox executable
        firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        os.system(firefox_path)
        return "Mozilla Firefox"
    elif "open command prompt" in command:
        os.system("start cmd")
        return "Command Prompt"
    elif "open vs code" in command:
        vscode_path = r"P:\Microsoft VS Code\Code.exe"
        os.system(vscode_path)
        return "Visual Studio Code"
    else:
        return "Unknown Application"

def set_female_voice(engine):
    voices = engine.getProperty('voices')
    female_voice = None

    # Check for "Zira" in the voice name
    for voice in voices:
        if "zira" in voice.name.lower():
            female_voice = voice
            break

    if female_voice:
        engine.setProperty('voice', female_voice.id)
        print("Female voice set successfully.")
    else:
        print("No female voice found.")

def speak(text):
    engine = pyttsx3.init()
    set_female_voice(engine)  # Set the voice to Zira
    engine.say(text)
    engine.runAndWait()

def get_voice_input():
    try:
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            speak("What can I do for you?")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=6)

        print("Processing...")

        # Recognize speech using Google Speech Recognition
        command = recognizer.recognize_google(audio).lower()
        return command

    except sr.UnknownValueError:
        error_message = "Could not understand audio. Please say again."
        print(error_message)
        speak(error_message)
        return None  # Signal that understanding failed
    except sr.RequestError as e:
        error_message = f"Could not request results from Google Speech Recognition service; {e}"
        print(error_message)
        speak(error_message)
        return None  # Signal that understanding failed
    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        speak(error_message)
        return None  # Signal that understanding failed

def voice_command():
    while True:
        command = get_voice_input()

        if command:
            application_name = open_application(command)

            if application_name != "Unknown Application":
                success_message = f"{application_name} opened successfully."
                print(success_message)
                speak(success_message)
                break
            else:
                error_message = "Command not recognized. Please try again."
                print(error_message)
                speak(error_message)

# Call the function to open applications based on voice command
voice_command()
