# import libraries
import sys
import nltk
nltk.download(['stopwords','punkt', 'wordnet', 'averaged_perceptron_tagger'])
import pandas as pd
import sqlalchemy
import numpy as np
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

def tokenize(text):
    tokenizer = RegexpTokenizer(r'\w+')
    lemmatizer = WordNetLemmatizer()
    tokens = tokenizer.tokenize(text.lower())
    stop_words = stopwords.words("english")
    filtered_words = [w for w in tokens if not w in stop_words]
    clean_words = [lemmatizer.lemmatize(tok).strip() for tok in filtered_words] 
    return clean_words

def preprocess_data(database_path): 
    # load data from database and preprocess
    engine = sqlalchemy.create_engine(database_path)#'sqlite:///../data/db.db')
    df = pd.read_sql_table("DisasterResponse", engine)
    X = df["message"] 
    Y = df.iloc[:,3:]

    #remove child Alone
    Y = Y.drop("child_alone", axis = 1)
    target_cols = Y.columns
    Y = pd.get_dummies(Y, columns = ["genre"]).values

    print(Y.shape)
    print(X.shape)

    #create dictionary matrix and apply term frequency transformation 
    vectorizer = CountVectorizer(tokenizer=tokenize)
    #generate tfidf from vector matrix
    tfidf = TfidfTransformer()
    X = vectorizer.fit_transform(X)
    X = tfidf.fit_transform(X)
    
    #check dimensionality and consistency
    print(type(X))
    print(X.shape)
    print(X.data)
    print(type(Y))
    print(Y.shape)
    
    return X,Y





