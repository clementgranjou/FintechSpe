from sklearn.feature_extraction.text import TfidfVectorizer

# Ton corpus
corpus = [
    "Le chat aime le lait.",
    "Le chien aime les os.",
    "Le chat et le chien sont des animaux domestiques."
]

# Initialiser le vectoriseur TF-IDF
vectorizer = TfidfVectorizer()

# Calculer la matrice TF-IDF
X = vectorizer.fit_transform(corpus)

# Afficher la matrice sous forme dense
print(X.toarray())

# Afficher les mots associés aux colonnes
print(vectorizer.get_feature_names_out())
