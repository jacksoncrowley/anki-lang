import os
from gtts import gTTS
import epitran
import urllib.request

def text_to_speech(word, language='hu'):
    """
    Convert text to speech     
    :param word: The word to convert to speech
    :param language: The language code (default is 'hu' for Hungarian)
    :param output_file: The name of the output MP3 file
    """
    tts = gTTS(text=word, lang=language, slow=False)
    output_file = f"temp/{word}.mp3"
    tts.save(output_file)
    print(f"Audio saved as {output_file}")

def word_to_ipa(word, language_code="hun-Latn"):
    epi = epitran.Epitran(language_code)
    ipa = epi.transliterate(word)
    return ipa

def download_image(url, file_path):
    try:
        urllib.request.urlretrieve(url, file_path)
        print(f"Image downloaded successfully to {file_path}")
        return True
    except Exception as e:
        print(f"Error downloading image: {e}")
        return False

###
word=input("Enter word: ")

text_to_speech(word)
word_to_ipa(word)

image=input("Enter link to image: ")
download_image(image, f"temp/{word}.jpg")