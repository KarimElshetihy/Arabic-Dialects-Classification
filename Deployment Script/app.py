from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import os
# Data Preparing Tools
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

# Machine Learning Algorithms
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

# To save the models
import pickle as pk
import joblib as jb
import Text_Classification as classifier
# from tensorflow.keras.models import load_model
import pickle as pk
import os
import sys


MainUI,_ = loadUiType('main.ui')

class Main(QMainWindow, MainUI):
    
    model_selection = str()
    image = None

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.handle_UI()
        self.handle_drop_menu()
        self.handle_buttons()


    def handle_UI(self):
        self.setWindowTitle('Text Classification Project')
        self.setFixedSize(1003,579)


    def handle_drop_menu(self):
        self.models_dict = classifier.load_models()
        self.model_selection = list(self.models_dict.values())[0]
        self.model_menu.addItems(list(self.models_dict.values()))
        self.image_display.setPixmap(QPixmap('image.jpg'))  #####
        

    def handle_buttons(self):
        
        ''' File Handling Buttons '''
        self.model_menu.currentIndexChanged.connect(self.selection_change)
        self.exit.clicked.connect(QApplication.instance().quit)
        self.classify.clicked.connect(self.predict_result)
        

    def selection_change(self,i):
        text = self.model_menu.currentText()
        self.model_selection = text


    def predict_result(self):
        res = classifier.predict(self.model_selection)
        self.result.setText(res)
        
    

    
def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()