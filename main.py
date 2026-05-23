'''
In this file we are going to load the data and develop MLR code in oops concept
'''
import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score,root_mean_squared_error
import sys
import warnings
warnings.filterwarnings("ignore")
import pickle


class Student_Performance_Project:
    def __init__(self,path):
        try:
            self.path = path
            self.df = pd.read_csv(self.path)
            print(self.df)
            #print(f"checking is there null values : {self.df.isnull().sum()}")
            self.df['Extracurricular Activities'] = self.df['Extracurricular Activities'].map({'Yes':1, 'No':0}).astype(int)
            self.X = self.df.iloc[:, :-1] #independent
            self.y = self.df.iloc[:, -1] #dependent
            self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(self.X,self.y,test_size=0.2,random_state=42)
            print(f"Training dataset size : {len(self.X_train)} : {len(self.y_train)}")
            print(f"Testing dataset size : {len(self.X_test)} : {len(self.y_test)}")
        except Exception as e:
            er_type,er_msg,er_line = sys.exc_info()
            print(f"Error in Line Number: {er_line.tb_lineno} : due to : {er_type} and reason was : {er_msg}")

    def training(self):
        try:
            self.Training_Data = pd.DataFrame(self.X_train)
            self.Training_Data["y_train"] = self.y_train
            self.reg = LinearRegression()
            self.reg.fit(self.X_train,self.y_train)
            self.y_train_predictions = self.reg.predict(self.X_train)
            self.Training_Data['y_train_predictions'] = self.y_train_predictions
            # Train Accuracy manually
            numerator = 0
            denominator = 0
            for i in self.Training_Data.index:
                numerator = numerator + (self.Training_Data['y_train'][i]-self.Training_Data['y_train_predictions'][i])**2
                denominator = denominator + ((self.Training_Data['y_train'][i]-self.Training_Data['y_train'].mean())**2)
            r2_score_value_manually = 1-numerator/denominator
            print(f"Train accuracy manually : {r2_score_value_manually}")
            print(f"Train Accuracy : {r2_score(self.y_train,self.y_train_predictions)}")
            print(f"Train Loss : {root_mean_squared_error(self.y_train,self.y_train_predictions)}")


        except Exception as e:
            er_type,er_msg,er_line = sys.exc_info()
            print(f"Error in Line Number: {er_line.tb_lineno} : due to : {er_type} and reason was : {er_msg}")


    def testing(self):
        try:
            self.Testing_Data = pd.DataFrame(self.X_test)
            self.Testing_Data["y_test"] = self.y_test
            self.y_test_predictions = self.reg.predict(self.X_test)
            self.Testing_Data['y_test_predictions'] = self.y_test_predictions
            # Test Accuracy manually
            numerator = 0
            denominator = 0
            for i in self.Testing_Data.index:
                numerator = numerator + (self.Testing_Data['y_test'][i] - self.Testing_Data['y_test_predictions'][i]) ** 2
                denominator = denominator + ((self.Testing_Data['y_test'][i] - self.Testing_Data['y_test'].mean())**2)
                r2_score_value_manually = 1-numerator/denominator
            print(f"Test accuracy manually : {r2_score_value_manually}")
            print(f" Test loss Manually : {np.sqrt(s / len(self.Testing_Data)-1)}")
            print(f"Test Accuracy : {r2_score(self.y_test, self.y_test_predictions)}")
            print(f"Test Loss : {root_mean_squared_error(self.y_test, self.y_test_predictions)}")
        except Exception as e:
            er_type,er_msg,er_line = sys.exc_info()
            print(f"Error in Line Number: {er_line.tb_lineno} : due to : {er_type} and reason was : {er_msg}")


    def check_own_data(self ):
        try:
            Hours_Studied=7
            Previous_Scores=99
            Extracurricular_Activities=1
            Sleeping_Hours=9
            Sample_Question_papers_Practiced=1
            print(f"Test point Predictions : {self.reg.predict([[Hours_Studied,Previous_Scores,Extracurricular_Activities,Sleeping_Hours,Sample_Question_papers_Practiced]])[0]}")


        except Exception as e:
            er_type,er_msg,er_line = sys.exc_info()
            print(f"Error in Line Number: {er_line.tb_lineno} : due to : {er_type} and reason was : {er_msg}")

    def saving_model(self):
        try:
            with open("Model.pkl","wb") as f:
                pickle.dump(self.reg,f)
            print(f"==========Load and check==========")
            with open("Model.pkl","rb") as t:
                model = pickle.load(t)
                Hours_Studied = 7
                Previous_Scores = 99
                Extracurricular_Activities = 1
                Sleeping_Hours = 9
                Sample_Question_papers_Practiced = 1
                print(f"Loaded model predictions :{model.predict([[Hours_Studied,Previous_Scores,Extracurricular_Activities,Sleeping_Hours,Sample_Question_papers_Practiced]])[0]}")



        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            print(f"Error in Line Number: {er_line.tb_lineno} : due to : {er_type} and reason was : {er_msg}")

if __name__ == '__main__':
    try:
        path = "Student_Performance.csv"
        obj = Student_Performance_Project(path)
        obj.training()
        obj.testing()
        obj.check_own_data()
        obj.saving_model()
    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        print(f"Error in Line Number: {er_line.tb_lineno} : due to : {er_type} and reason was : {er_msg}")


