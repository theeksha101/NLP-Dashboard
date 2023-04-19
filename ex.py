import spacy
from spacy import displacy

global doc

nlp = spacy.load('en_core_web_sm')

def docs():
    doc = nlp("i love Python Inc")
    return doc


print(displacy.render(docs(), style='ent'))
