from Speech_recon import takeCommand
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import nltk 

def query():
    # Tokenize
    tokenized_language = word_tokenize(takeCommand())
    # Lemmatiation
    Lemmatizer = WordNetLemmatizer()
    lem_sentance = [Lemmatizer.lemmatize(word) for word in tokenized_language]
    return lem_sentance















