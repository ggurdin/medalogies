"""
Given a directory of text files, containing texts separated by newlines,
takes that text data and trains word embeddings
"""

import os
import spacy
from gensim.models import Word2Vec


def train_embeddings(directory, output_file):
    nlp = spacy.load('en_core_web_sm')
    tokens = []
    for filename in os.listdir(directory):
        with open('dataset/' + filename, 'r') as f:
            lines = f.readlines()
            file_tokens = []
            for line in lines:
                review_token = [token.text for token in nlp.tokenizer(line) if not token.is_space]
                file_tokens.append(review_token)
            tokens.extend(file_tokens)
    w2v = Word2Vec(tokens, window=10, sg=1)
    w2v.wv.save_word2vec_format(output_file)
