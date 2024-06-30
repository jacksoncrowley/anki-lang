import os
import sys
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
            'qfmt': '''
                <div class="card">
                    <div class="word">{{Word}}</div>
                </div>
                
                <style>
                    .card {
                        font-family: Arial, sans-serif;
                        font-size: 40px;
                        text-align: center;
                        color: black;
                        background-color: white;
                    }
                    .word {
                        font-size: 60px;
                        color: #333;
                        margin-top: 50px;
                    }
                </style>
            ''',
            'afmt': '''
                <div class="card">
                    <div class="word">{{Word}}</div>
                    <hr id="answer">
                    <div class="ipa">IPA: {{IPA}}</div>
                    <div class="image">{{Image}}</div>
                    <div class="audio">{{Audio}}</div>
                </div>
                
                <style>
                    .card {
                        font-family: Arial, sans-serif;
                        font-size: 30px;
                        text-align: center;
                        color: black;
                        background-color: white;
                    }
                    .word {
                        font-size: 50px;
                        color: #333;
                        margin-top: 20px;
                    }
                    .ipa {
                        font-size: 35px;
                        color: #666;
                        margin: 20px 0;
                    }
                    .image img {
                        max-width: 60%;
                        height: auto;
                        margin: 20px 0;
                    }
                    .audio {
                        margin: 20px 0;
                    }
                </style>
            ''',
        },
    ])

my_deck = genanki.Deck(
  2059400110,
  'Hungarian Words')

my_package = genanki.Package(my_deck)

os.makedirs("audio", exist_ok=True)
os.makedirs("images", exist_ok=True)

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

def input_loop():
    word_image_pairs = []
    while True:
        word = input("Enter word (or 'quit' to finish): ").strip().lower()
        if word in ['quit', 'exit', 'q']:
            break

        image = input("Enter link to image: ").strip()
        if image in ['quit', 'exit', 'q']:
            break

        word_image_pairs.append((word, image))
        print("\n--- Next Word ---\n")
    return word_image_pairs

def process_inputs(word_image_pairs):
    for word, image in word_image_pairs:
        text_to_speech(word)
        ipa = word_to_ipa(word)
        download_image(image, f"images/{word}.jpg")
        new_card(word, ipa, f"<img src={word}.jpg>", f"[sound:{word}.mp3]")
        my_package.media_files.append(f"images/{word}.jpg")
        my_package.media_files.append(f"audio/{word}.mp3")

###

def main():
    print("Anki semi-automated flash card generator.")
    
    # Get input from user
    word_image_pairs = input_loop()
    
    # Process all the inputs
    print("\nProcessing all inputs:")
    process_inputs(word_image_pairs)
    
    # Continue with additional operations
    print("\nFinished processing all inputs.")
    print("Writing out deck to output.apkg...")
    
    # Write to file
    my_package.write_to_file('output.apkg')
    
    print("\nNew cards created added to output.apkg.")
    print("Before importing into Anki, remember to export your old deck. Just in case!")

if __name__ == "__main__":
    my_package.media_files = []  # Initialize the media_files list
    main()