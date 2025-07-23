import win32com.client
def speak_text(text):
    """Converts the given text to speech using Windows SAPI."""
    try:
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(text)
    except Exception as e:
        print(f"An error occurred: {e}")
list1 = ["habiba", "hunain", "laraib", "ishmal"]
for names in list1:
    speak_text(f"Shoutout to {names}")


    