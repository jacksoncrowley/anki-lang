import yaml
import epitran
import genanki
from gtts import gTTS
import urllib.request

def load_config(config_file):
    with open(config_file, "r") as yamlfile:
        return yaml.load(yamlfile, Loader=yaml.FullLoader)
    

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

def new_card(deck, model, word, ipa, image, audio):
    my_note = genanki.Note(
    model=model,
    fields=[word, ipa, image, audio])
    deck.add_note(my_note)

def interactive_loop():
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

def parse_word_image_csv(csv):
    word_image_pairs = []
    with open(csv, 'r', newline='') as csvfile:
        reader = csvfile.readlines()
        for row in reader:
            word_image_pairs.append(row.split(", "))
    return word_image_pairs


def process_inputs(deck, model,package, word_image_pairs):
    for word, image in word_image_pairs:
        text_to_speech(word)
        ipa = word_to_ipa(word)
        download_image(image, f"images/{word}.jpg")
        new_card(deck, model, word, ipa, f"<img src={word}.jpg>", f"[sound:{word}.mp3]")
        package.media_files.append(f"images/{word}.jpg")
        package.media_files.append(f"audio/{word}.mp3")

