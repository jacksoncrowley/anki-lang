import os
import genanki
from gtts import gTTS
import epitran
import urllib.request

my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Word'},
    {'name': 'IPA'},
    {'name': 'Image'},
    {'name': 'Audio'}
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Word}}',
      'afmt': '{{FrontSide}}<hr id="answer">IPA: {{IPA}}<br>{{Image}}<br>{{Audio}}',
    },
  ])

my_deck = genanki.Deck(
  2059400110,
  'Hungarian Words')

my_package = genanki.Package(my_deck)

def text_to_speech(word, language='hu'):
    """
    Convert text to speech     
    :param word: The word to convert to speech
    :param language: The language code (default is 'hu' for Hungarian)
    :param output_file: The name of the output MP3 file
    """
    tts = gTTS(text=word, lang=language, slow=False)
    output_file = f"audio/{word}.mp3"
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

def new_card(word, ipa, image, audio):
    my_note = genanki.Note(
    model=my_model,
    fields=[word, ipa, image, audio])
    my_deck.add_note(my_note)

###
word=input("Enter word: ")
text_to_speech(word)
ipa=word_to_ipa(word)

image=input("Enter link to image: ")
download_image(image, f"images/{word}.jpg")

new_card(word, ipa, f"<img src={word}.jpg>", f"[sound:{word}.mp3]")
my_package.media_files = [f"images/{word}.jpg",f"audio/{word}.mp3"]
my_package.write_to_file('output.apkg')