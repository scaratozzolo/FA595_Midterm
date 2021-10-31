import nltk
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# get frequency
def word_freq(text):
    tokenizer = nltk.RegexpTokenizer(r"\w+") # remove punctuation
    words = tokenizer.tokenize(text)
    freq = nltk.FreqDist(words)
    out = [(i, j) for i, j in freq.items()]
    return out


# lemmatize
def wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

def word_lem(text):
    lemmatizer = WordNetLemmatizer()
    out = [lemmatizer.lemmatize(w, wordnet_pos(w)) for w in nltk.word_tokenize(text)]
    return out