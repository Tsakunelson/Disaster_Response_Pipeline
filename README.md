# Disaster_Response_Pipeline
Disaster Response pipeline project

## Installation
- Anaconda 4.5.11 distribution
- Python 3.6
- Download NLTK with ['stopwords','punkt', 'wordnet', 'averaged_perceptron_tagger']

## Project Motivation

Model, Build and Deploy a framework to enhance accurate reponse from target organizations, given streams of messages 
by civilians in natural disaster sites. This project has 2 main objectives:

- Identify and structure incoming messages from natural disaster victims.
- Automatically Classify the messages into categories to enhance accurate response in real time. 
- Formulate a mechanism which allows the classified message to be forwarded to a specific response team(police, fire squad, ambulance etc.)

## File Descriptions 
This repository consists of three main folders:
  - The 'app' folder; contains all the frontend files (go.html and master.html) for deployment using plotly/bootstrap
  - The 'data' folder; contains the data sources and the the resultant cleaned database 'DisasterResponse.db' (will later be loaded into firebase) gotten from preprocessing in "process_data.py" 
  - The 'models' folder contains the classifier "train_classifier.py" and resultand saved model 'best_disaster_response_model.p' 

## Interacting With the Project


## Authors, Licensing, Acknowledgements

