import re
import yaml
import epitran
import genanki
from gtts import gTTS
import urllib.request

def load_config(config_file):
    with open(config_file, "r") as yamlfile:
        return yaml.load(yamlfile, Loader=yaml.FullLoader)
    

def text_to_speech(word, language_code):
    """
    Convert a string to a text-to-speech audio file using gTTS
    """
    tts = gTTS(text=word, lang=language_code, slow=False)
    output_file = f"audio/{word}.mp3"
    tts.save(output_file)
    print(f"Audio saved as {output_file}")

def word_to_ipa(word, language_code):
    """
    Convert a string to an international phonetic alphabet (IPA) string using epitran
    """
    epi = epitran.Epitran(language_code)
    ipa = epi.transliterate(word)
    return ipa

def sanitize_filename(file_path):
    """
    replace spaces with underscores and remove invalid characters from filenames
    """
    sanitized_path = file_path.replace(" ", "_")
    sanitized_path = re.sub(r'[<>:"/\\|?*]', '', sanitized_path)
    return sanitized_path


def download_image(url, file_path):
    """
    Download a corresponding image from a url and save it as {file_path} (typically the word)
    """
    try:
        urllib.request.urlretrieve(url, file_path)
        print(f"Image downloaded successfully to {file_path}")
        return True
    except Exception as e:
        print(f"Error downloading image: {e}")
        return False

def new_card(deck, model, word, ipa, image, audio):
    """
    Create a new flash card in a given {deck} using a given {model}.
    Takes four inputs: the word, the image file, the ipa string, and the tts file
    """
    my_note = genanki.Note(
    model=model,
    fields=[word, ipa, image, audio])
    deck.add_note(my_note)

def interactive_loop():
    """
    Interactive CLI session, continually asking for word, then url, then repeat
    Returns a list of [word, image] pairs
    """
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
    """
    Bulk import word/image pairs from a csv, seperated by ", " and newlines
    Returns a list of [word, image] pairs
    """
    word_image_pairs = []
    with open(csv, 'r', newline='') as csvfile:
        reader = csvfile.readlines()
        for row in reader:
            word_image_pairs.append(row.split(", "))
    return word_image_pairs


def process_inputs(deck, model,package, word_image_pairs, gtts, epitran):
    """
    From a given set of word/image pairs, create a card for each entry
    """
    for word, image in word_image_pairs:
        text_to_speech(word, gtts)
        ipa = word_to_ipa(word, epitran)
        download_image(image, f"images/{sanitize_filename(word)}.jpg")
        new_card(deck, model, word, ipa, f"<img src={sanitize_filename(word)}.jpg>", f"[sound:{word}.mp3]")
        package.media_files.append(f"images/{sanitize_filename(word)}.jpg")
        package.media_files.append(f"audio/{word}.mp3")

