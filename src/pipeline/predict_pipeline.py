import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model_path = 'artifacts/model.pkl'
            preprocessor = load_object(file_path=preprocessor_path)
            model = load_object(file_path=model_path)
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e:
            logging.info('Exception occured in prediction pipeline')
            raise CustomException(e,sys)
        

class CustomData:
    def __init__(self,
                 levy:float,
                 manufacturer: str,
                 year:float,
                 category:str,
                 leather_interior:int,
                 fuel_type:str,
                 engine_volume:float,
                 mileage:int,
                 cylinders:float,
                 gear_box_type:str,
                 drive_wheels:str,
                 doors:str,
                 wheel:str,
                 color:str,
                 airbags:int,
                 turbo:int):
        
        self.levy = levy
        self.manufacturer = manufacturer
        self.year = year
        self.category = category
        self.leather_interior = leather_interior
        self.fuel_type = fuel_type
        self.engine_volume = engine_volume
        self.mileage = mileage
        self.cylinders = cylinders
        self.gear_box_type = gear_box_type
        self.drive_wheels = drive_wheels
        self.doors = doors
        self.wheel = wheel
        self.color = color
        self.airbags = airbags
        self.turbo = turbo

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'levy':[self.levy],
                'manufacturer':[self.manufacturer],
                'year':[self.year],
                'category':[self.category],
                'leather_interior':[self.leather_interior],
                'fuel_type':[self.fuel_type],
                'engine_volume':[self.engine_volume],
                'mileage':[self.mileage],
                'cylinders':[self.cylinders],
                'gear_box_type':[self.gear_box_type],
                'drive_wheels':[self.drive_wheels],
                'doors': [self.doors],
                'wheel': [self.wheel],
                'color': [self.color],
                'airbags': [self.airbags],
                'turbo': [self.turbo]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)
            