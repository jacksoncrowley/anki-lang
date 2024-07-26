# ANKI-LANG for assisted flash card generation for language learning
`anki-lang` takes a series of word/image pairs and generates a new anki flash card deck, or otherwise updates a pre-existing one.

**The user must input a word in their chosen language as well as a url image link that they have chosen.** Choosing the image is important to create a personal link to the word.

This project is heavily inspired by the book *Fluent Forever* by Gabriel Wyner. The principle is simple: a barrier to language learning is the automatic translating into our native language. We can work our way around this by finding a word or phrase, and associating with it the sound, the phonetic pronounciation (international phonetic alphabet), and an image. 

## Usage
- Clone the repository
- Create the conda environment from the `environment.yaml` with:
```
conda env create --name anki-lang --file environment.yml
```
- Create a `config.yaml` file of your own:
```
Deck:
  seed: 2059400110
  name: Hungarian Words

Language:
  epitran: "hun-Latn"
  gtts: "hu"
```

- The name and seed need to be kept constant so that anki can recognise subsequent file imports as belonging ot the same deck. Generate a 10-digit random integer for the seed in python with:

```
int(random.random()*1e10) 
```

- Find the language codes for the two programs: [epitran](https://pypi.org/project/epitran/) which generates the phonetic alphabet string, and [gtts](https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang) which does the text-to-speech

- Run the script using either:
    - `python anki-lang.py -i` for the interactive mode
    - `python anki-lang.py -b $MY_CSV.csv` for the bulk import mode from a csv file, with rows organised as `word, url`. 

- audio and image files will be saved in folders named audio/ and images/ in the root directory from where `anki-lang.py` is called. 

- an output named `output.apkg` will be saved in the root directory, to be imported into anki.

> USAGE NOTES:
>
> The output anki deck technically only contains the most recent session, but so long as it was generated with the exact same input information (seed, name), this entry will be added to the deck already in your library.

## (eventual) to-do
- [ ] Generate config file somehow
- [ ] More user control over output folders and files