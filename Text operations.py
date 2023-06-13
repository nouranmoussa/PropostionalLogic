import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag

def extract_verbs(paragraph):
    # Parse the paragraph into sentences and words
    sentences = sent_tokenize(paragraph)
    words = [word_tokenize(sentence) for sentence in sentences]
    # Tag the words with their part of speech (POS)
    tagged_words = [pos_tag(sentence) for sentence in words]
    # Extract the verbs from the tagged words
    verbs = []
    for tagged_sentence in tagged_words:
        for word, tag in tagged_sentence:
            if tag.startswith('V'): #V is the tag for verbs
                verbs.append(word)
    # Return the list of verbs
    replace_words_with_operators(sentences)
    return verbs

# Function asks the user to assign a symbol for each verb (verbs corresponding to sentence)
def assign_symbols_to_verbs(verbs):
    symbols = {}
    for verb in verbs:
        symbol = input(f'Enter a symbol for "{verb}": ')
        symbols[verb] = symbol
    return symbols

def replace_words_with_operators(sentences):
    # change words to operators
    word_to_op = {
        'not': '!',
        'and': '^',
        'or': 'v',
        'implies' or 'if': '>',
        'if and only if' : '<>'
    }
    # Replace words with operators
    for word, op in word_to_op.items():
        for sentence in sentences:
            sentence = sentence.replace(word, op)
    # Return the sentence with replaced words
    return sentence



paragraph = "If today is Tuesday, then I have a test in English or Science. If my English Professor is absent, then I will not have a test in English. Today is Tuesday and my English Professor is absent. Therefore I have a test in Science."
sentences = sent_tokenize(paragraph)
replace_words_with_operators(sentences)
print (sentences)
verbs = extract_verbs(paragraph)
symbols = assign_symbols_to_verbs(verbs)
for verb, symbol in symbols.items():
    print(f'{verb}: {symbol}')