import os
import sys
import numpy as np
from src.logger import logging
from src.exception import CustomException
# Make sure your utils.py file is in src/utils/ and has a load_object function
from src.utils.utils import load_object

# Hardcoded scaling statistics from training data (removes scikit-learn dependency)
# Extracted from Artifacts/train_data.csv training set
FEATURE_MEANS = np.array([
    3.6091246287128715,
    11.569306930693068,
    10.985049504950496,
    0.07178217821782178,
    0.5564841584158416,
    6.315891089108911,
    68.55643564356437,
    3.8081950495049504,
    9.356435643564357,
    404.0321782178218,
    18.318316831683166,
    356.27834158415845,
    12.457351485148516,
])

FEATURE_STDS = np.array([
    8.875058224913126,
    23.152480822861172,
    6.89461758261083,
    0.25844695944787016,
    0.11770447451827175,
    0.7094517563306172,
    27.994922140912426,
    2.1312264279567033,
    8.589721087186096,
    166.17265514913421,
    2.228700928767628,
    91.56653276201261,
    7.110381022008366,
])

class PredictPipeline:
    def __init__(self):
        pass 

    def predict(self, features):
        try:
            # Standard folder name is 'artifacts' (lowercase)
            model_path = os.path.join("artifacts", "model.pkl")
            
            model = load_object(file_path=model_path)
            
            # Apply standardization using hardcoded training statistics
            # This replaces the scikit-learn StandardScaler
            data_scaled = (features - FEATURE_MEANS) / FEATURE_STDS
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
        This function creates a 2D numpy array instead of pandas DataFrame
        to reduce dependencies and memory footprint.
        """
        try:
            # Create numpy array with shape (1, 13) for single prediction
            data_array = np.array([[
                self.lcr,
                self.lpz,
                self.ia,
                self.wp,
                self.pl,
                self.rph,
                self.age,
                self.dis,
                self.ha,
                self.tax,
                self.ptratio,
                self.ld,
                self.lip
            ]], dtype=np.float64)
            
            return data_array
            
        except Exception as e:
            raise CustomException(e,sys)