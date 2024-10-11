Le rendu final se trouve dans le fichier exercice.ipynb.


Projet effectué en collaboration avec Yann Furrer le 11 Octobre.


### Analyse des Résultats de Classification des E-mails Spam
Dans ce projet, nous avons comparé deux modèles pour détecter les e-mails spam : Naïve Bayes et SVM. Voici les résultats clés :

#### 1. Vectorisation TF-IDF
Nous avons transformé notre jeu de données en une matrice TF-IDF avec 5571 échantillons et 7613 mots uniques. Cela montre que le corpus contient une bonne diversité lexicale, essentielle pour une classification précise.

#### 2. Séparation des Données
Les données ont été divisées en un ensemble d'entraînement de 4456 échantillons et un ensemble de test de 1115 échantillons. Cette séparation est cruciale pour évaluer la performance des modèles sur des données qu'ils n'ont jamais vues.

#### 3. Performance de Naïve Bayes
Précision : 96 % pour les e-mails "non spam" et 100 % pour les "spam".
Rappel : 100 % pour les "non spam" mais seulement 78 % pour les "spam".
F1-score : 0.98 pour "non spam" et 0.88 pour "spam".
La précision globale est de 96.8%. Bien que le modèle soit bon pour identifier les e-mails "non spam", il en laisse passer certains qui sont en fait "spam".

#### 4. Performance de SVM
Le modèle SVM a obtenu une précision de 98.1%, montrant une meilleure capacité à classer les e-mails, en particulier ceux marqués "spam". Cela signifie qu'il est plus efficace pour ce type de données.

#### 5. Validation Croisée
Naïve Bayes a des scores autour de 96.8%, ce qui est bon mais pas exceptionnel.
SVM a des scores d'environ 97.7%, confirmant qu'il est plus stable et performant.
Conclusion
En résumé, le modèle SVM est plus efficace pour détecter les e-mails spam, avec une précision supérieure à celle de Naïve Bayes. Bien que ce dernier soit un bon modèle de base, il a des limites, surtout en ce qui concerne l'identification des e-mails spam. L'analyse démontre que le SVM est le meilleur choix pour ce type de classification, tandis que Naïve Bayes peut être utilisé dans des cas plus simples. Pour améliorer les performances, il pourrait être intéressant d'explorer d'autres modèles ou d'ajuster les hyperparamètres.
