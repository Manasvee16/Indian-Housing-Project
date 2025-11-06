import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
# Make sure your utils.py file is in src/utils/ and has a load_object function
from src.utils.utils import load_object 

class PredictPipeline:
    def __init__(self):
        pass 

    def predict(self, features):
        try:
            # Standard folder name is 'artifacts' (lowercase)
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        
        except Exception as e:
            raise CustomException(e, sys) 

class CustomData:
    def __init__(self, 
                 lcr : float, 
                 lpz : float, 
                 ia : float, 
                 wp : float, 
                 pl : float, 
                 rph : float, 
                 age : float, 
                 dis : float, 
                 ha : float, 
                 tax : float, 
                 ptratio : float, 
                 ld : float, 
                 lip : float,    
            ):

        self.lcr = lcr
        self.lpz = lpz 
        self.ia = ia
        self.wp = wp 
        self.pl = pl
        self.rph = rph 
        self.age = age 
        self.dis = dis 
        self.ha = ha
        self.tax = tax
        self.ptratio = ptratio 
        self.lip = lip
        self.ld = ld 

    def get_data_as_dataframe(self):
        """
        This function maps the new form names (lcr, lpz) back to the 
        original model column names (crim, zn) so the preprocessor can work.
        """
        try:
            custom_data_input_dict = {
                # Original Model Column : [New Form Variable]
                "crim": [self.lcr],
                "zn": [self.lpz],
                "indus": [self.ia],
                "chas": [self.wp],
                "nox": [self.pl],
                "rm": [self.rph],
                "age": [self.age],
                "dis": [self.dis],
                "rad": [self.ha],
                "tax": [self.tax],
                "ptratio": [self.ptratio],
                "b": [self.ld],       # Map ld back to 'b'
                "lstat": [self.lip]  # Map lip back to 'lstat'
            }
            
            df = pd.DataFrame(custom_data_input_dict)
            return df
            
        except Exception as e:
            raise CustomException(e,sys)