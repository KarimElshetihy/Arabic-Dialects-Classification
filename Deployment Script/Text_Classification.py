import os
# Data Preparing Tools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_selection import chi2
from sklearn.metrics import classification_report

# Machine Learning Algorithms
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

# To save the models
import pickle as pk
import joblib as jb

path = "../Models/ML5/"

def load_models():
    models = {}
    for i, file in enumerate(os.listdir(path), 1):
        models['{}'.format(i)] = file

    
    return models


def predict(model, text):
    ''' Text preperation for prediction'''
    global path
    Model = jb.load(path+model)

    count_vect = CountVectorizer([])
    prediction = Model.predict(count_vect.transform([text]))

    return  prediction

