# Car Price Prediction - Anjali Ramesh

The dataset is obtained from [Kaggle](https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge).

#### **Objective** - Predict the `Price` of a car (Regression Analysis)

**Independent Features** - The original dataset has 17 independent features (including the `ID` column)

`ID`: Unique identifier for each car entry (integer)

`Levy`: Tax or fee applied to the car (object) 

`Manufacturer`: The manufacturer or brand of the car (object) 

`Model`: The model name of the car (object) 

`Prod. year`: The production year of the car (integer) 

`Category`: The category or type of the car (object) 

`Leather interior`: Indicates whether the car has a leather interior or not (object) 

`Fuel type`: The type of fuel used by the car (object) 

`Engine volume`: The engine displacement or volume of the car (object) 

`Mileage`: The distance traveled by the car (object) 

`Cylinders`: The number of cylinders in the car's engine (float) 

`Gear box type`: The type of gearbox used in the car (object) 

`Drive wheels`: The type of drive wheels (object) 

`Doors`: The number of doors in the car (object) 

`Wheel`: The type of wheel (object) 

`Color`: The color of the car (object) 

`Airbags`: The number of airbags in the car (integer) 


## Approach for the project

Data Ingestion :
In Data Ingestion phase the data is first read as csv.
Then the data is split into training and testing and saved as csv file.

Data Transformation :
In this phase a ColumnTransformer Pipeline is created.
for Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
This preprocessor is saved as pickle file.

Model Training :
In this phase base model is tested . The best model found was random forest regressor.
After this hyperparameter tuning is performed on random forest, catboost and xgboost.
A final VotingRegressor is created which will combine prediction of catboost, xgboost and random forest models.
This model is saved as pickle file.

Prediction Pipeline :
This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

Flask App creation :
Flask app is created with User Interface to predict the car prices inside a Web Application.


## AWS Deployment Link:

AWS Elastic Beanstalk link : http://mlproject-env.eba-sci3j2gu.us-east-2.elasticbeanstalk.com/

### Screenshot of the UI

![](https://imgur.com/UsoR5jw.png)

## Exploratory Data Analysis

Notebook - [link](https://github.com/anjaliramesh-datascience/car-price-prediction/blob/main/notebook/Data%20Preprocessing%20and%20EDA.ipynb)

## Model Training

Notebook - [link](https://github.com/anjaliramesh-datascience/car-price-prediction/blob/main/notebook/Model%20Training.ipynb)
