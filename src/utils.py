import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score

def save_object(obj, file_path):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as f_obj:
            dill.dump(obj, f_obj)

    except Exception as e:
        raise CustomException(e, sys)
    

def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        model_report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]

            model.fit(X_train, y_train)

            y_train_predicted = model.predict(X_train)

            y_test_predicted = model.predict(X_test)

            test_model_score = r2_score(y_test, y_test_predicted)

            model_report[list(models.keys())[i]] = test_model_score
            
        return model_report
    except Exception as e:
        raise CustomException(e, sys)