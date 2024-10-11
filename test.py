import spacy

nlp = spacy.load('fr_core_news_sm')

texte = "Les chats sont les animaux les plus mignons."

doc = nlp(texte)

# Lemmatisation
lemmes = [token.lemma_ for token in doc]

# Suppression des stop words
tokens_sans_stop = [token.text for token in doc if not token.is_stop]

# Normalisation (minuscules)
tokens_minuscules = [token.text.lower() for token in doc]

print("Lemmatisation :", lemmes)
print("Tokens sans stop words :", tokens_sans_stop)
print("Tokens en minuscules :", tokens_minuscules)
