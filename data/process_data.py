# coding:UTF-8

"""

Requirements pip install nltk for NLP processing
             pip install sqlalchemy to create sqlite a database engine
"""

import sys
import re
import pandas as pd
import numpy as np
#from sklearn.feature_extraction.text import TfidfTransformer
#import nltk
from sqlalchemy import create_engine
import sqlite3



def load_data(messages_filepath, categories_filepath):
    """
    Input: Twitter messages csv file path and class categories csv file path
    Output: Pandas dataframe of both files merged  
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, on='id')
    return df

def clean_data(df):
    """
    Input: df ==> Merged message and categories dataframe
    Output: cleaned dataframe 
    """
    categories = df.categories.str.split(";", expand=True)
    
    #create column labels
    first_row = categories.loc[0]
    categories_colnames = [x.split("-")[0] for x in first_row]
    categories.columns = categories_colnames
    
    #convert category values to just numbers 0 or 1
    for column in categories:
        categories[column] = categories[column].apply(str)
        categories[column] = categories[column].apply(lambda x: x.split("-")[1])
        categories[column] = pd.to_numeric(categories[column])
        
    #replace the categories column with the cleaned category dataframe
    df = df.drop("categories", axis=1)
    df = pd.concat([df,categories], axis=1)       
    
    #remove duplicate columns
    df = df.drop_duplicates()
    
    return df


def save_data(df, database_filename):
    """
    Input: df ==> the cleaned twitter message and classes
           database_filename ==> Path to store the resulting database
    """
    engine = create_engine("sqlite:///" +str(database_filename)+ ".db") 
    print("before error..............")
    df.to_sql('DisasterResponse', engine, if_exists="replace", index=False)
    return True  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        res = save_data(df, database_filepath)
        print(res)
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
