import os
import genanki
import argparse
from src import modules

## load config file
config = modules.load_config("config.yaml")

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

my_deck = genanki.Deck(config["Deck"]["seed"], config["Deck"]["name"])
my_package = genanki.Package(my_deck)

os.makedirs("audio", exist_ok=True)
os.makedirs("images", exist_ok=True)
###

def main():
    parser = argparse.ArgumentParser(description="Word/Image Pair Learning Tool")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-b", "--bulk", type=str, help="Run in bulk import mode")
    group.add_argument("-i", "--interactive", action="store_true", help="Run in interactive mode")
    args = parser.parse_args()
    
    # Get input from user
    if args.interactive:
        print("Anki-Lang Semi-automated flash card generator!")
        word_image_pairs = modules.interactive_loop()

    # else read from file
    
    # Process all the inputs
    print("\nProcessing all inputs:")
    modules.process_inputs(my_deck, my_model, my_package, word_image_pairs)
    
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