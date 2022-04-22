from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import nltk 

def NTLK_NER(filtered_speech):
    stop_words = set(stopwords.words("english"))
    filtered_sentence = [w for w in filtered_speech if not w in stop_words]
    filtered_sentence = []

    for w in filtered_speech:
        if w not in stop_words:
            filtered_sentence.append(w)
            print(filtered_sentence)
    # NER (Natural Entity Recognition)
    tagged_sentences = nltk.pos_tag(filtered_sentence)
    chunks = nltk.ne_chunk(tagged_sentences)
    named_entities = []
    for tagged_tree in chunks:
        if hasattr(tagged_tree, "label"):
            entity_name = ''.join(c[0] for c in tagged_tree.leaves())
            entity_type = tagged_tree.label()
            named_entities.append((entity_name, entity_type))
            print(named_entities)
    return named_entities









