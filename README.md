# ANKI-LANG for assisted flash card generation for language learning
`anki-lang` takes a series of word/image pairs and generates a new anki flash card deck, or otherwise updates a pre-existing one.

**The user must input a word in their chosen language as well as a url image link that they have chosen.** Choosing the image is important to create a personal link to the word.

This project is heavily inspired by the book *Fluent Forever* by Gabriel Wyner. The principle is simple: a barrier to language learning is the automatic translating into our native language. We can work our way around this by finding a word or phrase, and associating with it the sound, the phonetic pronounciation (international phonetic alphabet), and an image. 

# Features
input word as string [ ]:
- generate text-to-speech (tts) audio clip [x]
- generate international phonetic alphabet (ipa) string [x]

input image url [ ]:
- download image from url [x]
- distinguish between internal links/pre-downloaded files and urls? [ ]

create new anki card with word on the front and the image, tts, and ipa on the back[x]

interactive mode [x]
- run with `-i`, will open a session that asks for a word, then an image, and repeats until the user types "q"

bulk import mode from file [x]
- run with `-b`, will read a csv file where the lines are organised as `word, image-url`

config file [ ]
- anki deck presets [x]
    - generate anki deck presets if doesn't exist [ ]
- find smart way to store the anki model info [ ]
- language settings [ ]
- file paths [ ]

# Usage notes
The output anki deck technically only contains the most recent session, but so long as it was generated with the exact same input information (seed, name), this entry will be added to the deck already in your library.