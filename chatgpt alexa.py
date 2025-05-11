import os
import speech_recognition as sr
import pyttsx3
import openai

# Temporary setup for the environment variable (Replace with your actual key)
os.environ['OPENAI_API_KEY'] = 'YOUR OPENAI API KEY'

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Retrieve the OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# Verify that the key has been set
if openai.api_key is None:
    raise ValueError("OpenAI API key not found. Make sure it is set as an environment variable.")


# Function to convert text to speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()


# Function to get a response from OpenAI's GPT
def get_gpt_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.9
    )
    return response.choices[0].text.strip()


# Function to listen for a command
def listen_for_command():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that. Please repeat.")
        return None
    except sr.RequestError as e:
        speak(f"Could not request results from the speech recognition service; {e}")
        return None


def main():
    speak("How can I help you today?")

    while True:
        command = listen_for_command()
        if command:
            if 'exit' in command or 'quit' in command:
                speak("Goodbye!")
                break
            response = get_gpt_response(command)
            speak(response)


if __name__ == "__main__":
    main()
