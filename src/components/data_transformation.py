import sys
import numpy as np
import pandas as pd
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.utils import save_object

from src.exception import CustomException
from src.logger import logging
import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifact', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_features = ['reading score', 'writing score']
            cat_features = ['gender', 
                            'race/ethnicity', 
                            'parental level of education', 
                            'lunch', 
                            'test preparation course'
                            ]
            numerical_pipeline = Pipeline(
                steps = [
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )
            categorical_pipeline = Pipeline(
                steps = [
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('onehot', OneHotEncoder()),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )
            logging.info('numerical columns scaled')
            logging.info('categorical columns encoded')

            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline", numerical_pipeline, numerical_features),
                    ("categorical_pipeline", categorical_pipeline, cat_features)
                ]
            )
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info('train and test data loaded')
            preprocessor_obj = self.get_data_transformer_object()
            target_column_name = 'math score'
            
            input_feature_train_df = train_df.drop(target_column_name, axis=1)
            target_column_train_df = train_df[target_column_name]
            input_feature_test_df = test_df.drop(target_column_name, axis=1)
            target_column_test_df = test_df[target_column_name]
            logging.info('train and test data split into input features and target column')

            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)
            logging.info('train and test data transformed')
            
            train_arr = np.c_[input_feature_train_arr, target_column_train_df]
            test_arr = np.c_[input_feature_test_arr, target_column_test_df]
            logging.info('train and test data merged')
            
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            ) 
        except Exception as e:
            raise CustomException(e,sys)
        

