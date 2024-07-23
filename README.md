# ANKI-LANG for assisted flash card generation for language learning

The output anki deck technically only contains the most recent session, but so long as it was generated with the exact same input information (seed, name), this entry will be added to the deck already in your library.

# To-do
inputs: 
- input word:
    - generate text-to-speech audio clip [x]
    - generate international phonetic alphabet string [x]

- input image url:
 - download image from url [x]

create new anki card with word on the front and the image, tts, and ipa on the back[x]

add multiple cards in one session [x]

Architecture:
- add from saved list []
- verify word/phrase is valid [ ]
- check for pre-existing deck templates [ ]
- put all functions in a module file [ ]
- config file for:
    - anki presets [ ]
    - language [ ]
    - paths [ ]
- pip installable [ ]
- nice CLI interface [ ]